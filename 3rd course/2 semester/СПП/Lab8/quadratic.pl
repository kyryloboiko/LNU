quadratic(A, B, C):- 
    D is B*B - 4 * A * C,(
    D < 0 -> write('Is Complex'),nl, false;

    D =:= 0 -> 
    R1 is (- B + sqrt(D))/ (2 * A),
    write(R1), nl ;

    D > 0 ->
    R1 is (- B + sqrt(D))/ (2 * A),
    R2 is (- B - sqrt(D))/ (2 * A),

    write(R1), nl,
    write(R2)).
