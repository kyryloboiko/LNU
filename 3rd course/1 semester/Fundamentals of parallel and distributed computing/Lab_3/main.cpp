#include <stdio.h>
#include <math.h>
#include <omp.h>

int main(int argc, char **argv) {
    int N = 1000;
    double sum = 0.0;
    double term, factorial;
    int i, method;

    printf("Choose synchronization method: \n1 - atomic operations\n2 - locks\n");
    scanf("%d", &method);

    if (method == 1) {
        #pragma omp parallel for private(term, factorial) shared(sum)
        for (i = 1; i <= N; i++) {
            factorial = 1.0;
            for (int j = 1; j <= i; j++) {
                factorial *= j;
            }
            term = pow(-1.0, i) / factorial;
            #pragma omp atomic
            sum += term;
        }
    } else if (method == 2) {
        omp_lock_t lock;
        omp_init_lock(&lock);
        #pragma omp parallel for private(term, factorial) shared(sum, lock)
        for (i = 1; i <= N; i++) {
            factorial = 1.0;
            for (int j = 1; j <= i; j++) {
                factorial *= j;
            }
            term = pow(-1.0, i) / factorial;
            omp_set_lock(&lock);
            sum += term;
            omp_unset_lock(&lock);
        }
        omp_destroy_lock(&lock);
    } else {
        printf("Invalid choice.\n");
        return 1;
    }

    printf("The result of a row is: %.15f\n", sum);

    double result = (1 - exp(1)) / exp(1);
    printf("Theoretic result: %.15f\n", result);

    return 0;
}
