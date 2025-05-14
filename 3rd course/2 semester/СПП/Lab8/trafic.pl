trafic_light:-
    write('Enter light (green, orange, red) or exit'), read(X),
    (X == 'exit' -> write('Exiting program...'), nl, false;
     X == 'red' -> write('Stop'), nl;
     X == 'orange' -> write('Wait'), nl ;
     X == 'green' -> write('Go'), nl;
     write('Invalid input'), nl),
    trafic_light.
