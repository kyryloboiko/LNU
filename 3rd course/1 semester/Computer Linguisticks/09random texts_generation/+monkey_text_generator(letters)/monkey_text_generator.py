import json

import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Label import Label
import dash_table as dt
import dash_core_components as dcc
import webbrowser as web
import dash_html_components as html
import numpy as np
import math
from numpy.core.fromnumeric import size
import pandas as pd
import logging
import random
import os

needed_chars = []
charArr = []
symbArr = []

currChar = 0

while len(charArr) < 45000:
    currChar += 1
    if (chr(currChar).isalpha()):
        charArr.append(chr(currChar))

currSymb = 0

tempArr = []

while len(tempArr) < 1000 + 1:
    currSymb += 1
    if (not(chr(currSymb).isalpha())    and chr(currSymb).isprintable()):
        tempArr.append(chr(currSymb))

symbArr = tempArr[16:26]+tempArr[1:16] +tempArr[26:]

needed_chars = charArr + symbArr

logging.getLogger("werkzeug").setLevel(logging.ERROR)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Text generator'
app.layout = html.Div([
    dbc.Row([dbc.Col(
        dbc.Card([
            dbc.CardHeader("Main generation parameters"),
            dbc.CardBody([
                html.Label("M"),
                dbc.Input(id='M', type="number", min="1", max="46000", # max int
                          style={"margin-left": "2%", "margin-right": "2%", "width": "40%", "display": "inline-block"}),
                html.Label("L"),
                dbc.Input(id='l', type="number", min="1",
                          style={"margin-left": "2%", "width": "40%", "display": "inline-block"}),
                html.Br(),
                html.Label("f0"),
                dbc.Input(id='f0', type="number", max="1", min="0", value='0',
                          style={"margin-left": "2%", "width": "40%", "display": "inline-block"})
            ])
        ]), width=3),
        dbc.Col(
            dbc.Card([
                dbc.CardHeader("Options"),
                dbc.CardBody(
                    [
                        html.Div(
                            dcc.RadioItems(
                                options=[
                                    {"label": "equal", "value": "eq"},
                                    {"label": "random", "value": "rand"},
                                    {"label": "barrier", "value": "bar"},
                                    {"label": "log", "value": "log"},
                                ],
                                id="options",
                                value="eq"
                            ), style={"margin-right": "2%", "float": "left"}),
                        html.Div(
                            [
                                dbc.Input(id='C', min="1", type="number", placeholder="C:barrier", value="",
                                          style={"height": "40%"}),
                                dbc.Input(id='A', type="number", placeholder="A:log", value="", style={"height": "40%"})
                            ]
                            , style={"float": "left", "width": "20%"})
                    ]
                )
            ])

            , width=5),
        dbc.Col(
            html.Div(
                [dbc.Button("Generate & Save", id="generate_save_btn", style={"margin-top": "45%"}, disabled=True),
                 dcc.Checklist(
                     id='multiprocess_computing',
                     options=[
                         {'label': 'multiprocessing', 'value': 'enable'}
                     ],
                     value=''
                 )],
                style={"float": "left", "width": "50%"}
            )
            , width=3)
    ]
    )
    ,
    html.Br(),
    dbc.Row([dbc.Col(dt.DataTable(id="table",
                                  editable=True,
                                  # filter_action="native",
                                  sort_action="native",
                                  style_cell={
                                      'textAlign': 'center',
                                      'whiteSpace': 'auto',
                                      'height': 'auto',
                                      'minWidth': 95, 'maxWidth': 95, 'width': 95
                                  },
                                  fixed_rows={"headers": True},
                                  style_table={"height": "80%", "overflowY": "auto"},
                                  columns=[{"name": i, "id": i} for i in
                                           ["rank", "unicode", "character", "probability"]]
                                  ), width=4)
                , dbc.Col(dbc.Card([
            dbc.CardHeader("Preview 1000 elements according to the set parameters"),
            dbc.CardBody(dcc.Textarea(id="text",
                                      placeholder="",
                                      value="",
                                      style={"height": "100%", "width": "100%"},
                                      rows=19))
        ]), width=8)]),
    html.Br(),
    dbc.Row(
        [
            dbc.Col(
                [
                    dcc.Checklist(
                        id='enable_histogram',
                        options=[
                            {'label': 'enable histogram', 'value': 'enable'}
                        ],
                        value=''
                    ),
                    dcc.RadioItems(id='hist_option',
                                   options=[
                                       {"label": "linear", "value": "lin"},
                                       {"label": "log", "value": "log"}
                                   ],
                                   value="lin"
                                   ),
                    dcc.Graph(
                        id="histogram",
                    )
                ]

                , width=12)
        ]
    )

], style={"padding": "1%"})

import random
import plotly.express as px
from dash.dependencies import Output, Input, State


@app.callback(Output("histogram", "figure"), [Input("table", "derived_virtual_data"),
                                              Input("hist_option", "value"), Input("enable_histogram", "value")])
def update_histogram(table, option, enable):
    if enable != ['enable'] or not table:
        return {}
    # if data is None or l is None:
    #     return dash.no_update
    log = None
    if option == "lin":
        log = False
    else:
        log = True
    df = pd.DataFrame(data=table)
    # post_probability=[]
    # for row in table:
    #     if row['character']=="space":
    #         post_probability.append(data.count(" ")/float(l))
    #         continue
    #     post_probability.append(data.count(row['character'])/float(l))

    # df["post_probability"]=post_probability

    if df['character'][0] == 'space':
        df = df.drop(0, axis=0)

    fig = px.bar(df, x="rank", y="probability",
                 barmode='overlay', hover_data=["character"], labels={"value": "probability"}, log_x=log)

    return fig


@app.callback(Output("generate_save_btn", "disabled"),
              [Input("l", "value"), Input("table", "data")])
def generation_valid(l, table):
    if str(l) == "" or l is None or not table:
        return True
    else:
        return False


import multiprocessing
import concurrent.futures


def process_function(chr, prob, l):
    # do processing data
    text = random.choices(chr, weights=prob, k=int(l))
    return text


import codecs


@app.callback(Output("generate_save_btn", "color"),
              [Input("generate_save_btn", "n_clicks")],
              [State("M", "value"), State("l", "value"), State("table", "data"), State("options", "value"),
               State("C", "value"), State("A", "value"), State("f0", "value"),
               State("multiprocess_computing", "value")])
def ganerate_and_save(n, M, l, table, options, C, A, f0, enable_mp):
    if n is None:
        return dash.no_update

    # generating
    if float(f0) != 0:
        table[0]["character"] = " "
    chr = []
    prob = []
    for row in table:
        chr.append(row["character"])
        prob.append(float(row['probability']))

    text = ""
    if (enable_mp):
        # concurate 
        cc = multiprocessing.cpu_count()
        with concurrent.futures.ProcessPoolExecutor(max_workers=cc) as executor:
            futures = []
            for i in range(cc):
                futures.append(
                    executor.submit(process_function, chr, prob, int(float(l) / float(cc))))  # make length int()

            for future in concurrent.futures.as_completed(futures):
                part_text = future.result()
                text = [*text, *part_text]
    else:
        # sequential
        text = random.choices(chr, weights=prob, k=int(l))

    # saving
    name = 'M' + str(M) + '_L' + str(l) + '_space' + str(f0) + '_' + str(options)
    if options == "bar":
        name += str(C)
    if options == "log":
        name += str(A)
    if not os.path.exists('output'):
        os.makedirs('output')
    file = codecs.open('output/' + name + '.txt', "w", "utf-8-sig")
    file.write("".join(text))
    file.close()

    return dash.no_update


@app.callback(Output("text", "value"), [Input("table", "data"), Input("f0", "value")])
def preview(table, f0):
    if table is None:
        return dash.no_update
    elif not table:
        return ""

    l = 1000
    if float(f0) != 0:
        table[0]["character"] = " "
    chr = []
    prob = []
    for row in table:
        chr.append(row["character"])
        prob.append(float(row['probability']))
    text = random.choices(chr, weights=prob, k=int(l))
    return "".join(text)


# min_A=0
# max_A=1
# log10_Mfactorial=0
# @app.callback([Output("A","min"),Output("A","max")],[Input("M","value"),Input("f0","value"),Input("options","value")])
# def update_A(M,f0,options):
#     if options=="log":           
#         global min_A
#         global max_A
#         global log10_Mfactorial
#         log10_Mfactorial=0
#         #log10_Mfactorial=math.log10(math.factorial(int(M))) #simplify factorial!   
#         for j in range(int(M)):
#             log10_Mfactorial+=math.log10(j+1)

#         min_A=(1-float(f0))/float(M)
#         max_A=(1-float(f0))/(float(M)-log10_Mfactorial/math.log10(float(M)))

#         out=[]
#         out.append(min_A,max_A)
#         return out

from unidecode import unidecode as ud


@app.callback([Output("table", "data"), Output("A", "min"), Output("A", "max")],
              [Input("M", "value"), Input("options", "value"), Input("C", "value"), Input("A", "value"),
               Input("f0", "value")])
def update_m(M, options, C, A, f0):
    if str(M) == "" or M is None or f0 is None:
        return [], dash.no_update, dash.no_update

    data = {"rank": [], "unicode": [], "character": [], "probability": []}
    prob_accuracy = 7
    min_A = dash.no_update
    max_A = dash.no_update

    if options == "rand":
        ri = [round(np.random.rand(), prob_accuracy) for _ in range(int(M))]
        s = sum(ri)
        li = []
        li.append(float(f0))
        for j in range(int(M)):
            li.append(round((ri[j] / s) * (1.0 - float(f0)), prob_accuracy))
        data['probability'] = li

    if options == "eq":
        li = []
        li.append(float(f0))
        data["probability"] = li + [round((1.0 - float(f0)) / (int(M)), prob_accuracy) for _ in range(int(M))]

    if options == "bar":
        if C == "" or C is None:
            return [], dash.no_update, dash.no_update

        a = ((float(C) - 1.0) / (float(C) + 1.0)) * ((2.0 * (1.0 - float(f0))) / (float(M) * (float(M) - 1.0)))
        f1 = (2.0 * float(C) * (1.0 - float(f0))) / (float(M) * (float(C) + 1.0))

        li = []
        li.append(float(f0))
        li.append(round(f1, prob_accuracy))

        f = f1
        for j in range(int(M) - 1):
            f -= a
            li.append(round(f, prob_accuracy))

        data["probability"] = li

    if options == "log":

        # log10_Mfactorial=math.log10(math.factorial(int(M))) #simplify factorial!
        log10_Mfactorial = 0
        for j in range(int(M)):
            log10_Mfactorial += math.log10(j + 1)

        min_A = round((1 - float(f0)) / float(M), 5)
        max_A = round((1 - float(f0)) / (float(M) - log10_Mfactorial / math.log10(float(M))), 5)
        if (A == "" or A is None or A < min_A or A > max_A):
            return [], min_A, max_A

        B = (float(M) * float(A) - (1.0 - float(f0))) / log10_Mfactorial

        li = []
        li.append(float(f0))
        for j in range(int(M)):
            f = float(A) - (float(B) * math.log10(j + 1))
            li.append(round(f, prob_accuracy))

        data["probability"] = li

    k = 0
    i = 32
    while len(data["character"]) != (int(M) + 1):
        data['character'].append(needed_chars[i - 33])  # char generator
        data['unicode'].append(ord(needed_chars[i - 33]))
        data["rank"].append(i - 32 - k)
        i += 1

    data['character'][0] = "space"
    if (float(f0) == 0):
        data['character'].pop(0)
        data['unicode'].pop(0)
        data["rank"].pop(0)
        data["probability"].pop(0)

    if (data['character'][0] == 'space'):
        data['unicode'][0] = 32

    data = pd.DataFrame(data=data)

    return data.to_dict("records"), min_A, max_A


if __name__ == "__main__":
    web.open("http://127.0.0.1:8050/")
    app.run_server(debug=False)
