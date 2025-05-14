#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char** argv) {
    int rank, size, i;
    double a = 0.0, b = 1.0;

    int n = 1000000, local_n;
    double h, local_a, local_b, local_sum = 0.0, total_sum = 0.0;

    double *x_values;
    MPI_Request request;
    MPI_Status status;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    h = (b - a) / n;
    local_n = n / size;

    local_a = a + rank * local_n * h;
    local_b = local_a + local_n * h;

    if (rank == size - 1) {
        local_n += n % size;
    }

    x_values = (double*)malloc((local_n + 1) * sizeof(double));
    for (i = 0; i <= local_n + 1; i++) {
        x_values[i] = local_a + i * h;
    }

    local_sum = 0.5 * h * (cos(local_a) + cos(local_b));
    for (i = 1; i < local_n; i++) {
        local_sum += h * cos(x_values[i]);
    }

    printf("Process %d: local sum = %f\n", rank, local_sum);

    if (rank != 0) {
        MPI_Isend(&local_sum, 1, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD, &request);
        MPI_Wait(&request, &status);
    } else {
        total_sum = local_sum;
        printf("Process 0: starting sum = %f\n", total_sum);

        for (i = 1; i < size; i++) {
            MPI_Irecv(&local_sum, 1, MPI_DOUBLE, i, 0, MPI_COMM_WORLD, &request);
            MPI_Wait(&request, &status);
            printf("Process 0: gained sum from process %d = %f\n", i, local_sum);
            total_sum += local_sum;
        }

        printf("Total area under curve: %f\n", total_sum);
    }

    free(x_values);

    MPI_Finalize();
    return 0;
}