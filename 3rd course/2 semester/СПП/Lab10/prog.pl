:- use_module(library(csv)).

% --- Підозрілі акаунти ---
suspicious_account(jane).
suspicious_account(ivan).

% --- Підозрілі країни ---
suspicious_country('NorthKorea').
suspicious_country('China').
suspicious_country('Afghanistan').
suspicious_country('Belarus').

% --- Підозрілі типи ---
suspicious_type(gambling).

% --- Умова підозрілої транзакції ---
suspicious_transaction(T) :-
    transaction(T, Account, Amount, Time, Country, Type),
    (
        suspicious_account(Account);
        (Amount > 20000, Time = night);
        suspicious_country(Country);
        suspicious_type(Type)
    ).

% --- Пропуск заголовка CSV ---
read_transactions(File) :-
    csv_read_file(File, Rows, [functor(row)]),
    exclude(is_header_row, Rows, DataRows),
    maplist(convert_to_transaction, DataRows).

is_header_row(row('T', _, _, _, _, _)).

% --- Перетворення рядка на факт ---
convert_to_transaction(row(T, Account, AmountRaw, Time, Country, Type)) :-
    (   number(AmountRaw)
    ->  Amount = AmountRaw
    ;   atom_number(AmountRaw, Amount)
    ),
    assertz(transaction(T, Account, Amount, Time, Country, Type)).
