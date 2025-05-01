#include <mpi.h>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <numeric>

using namespace std;

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int world_size;
    int world_rank;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    const int n = 100000;
    double *x = new double[n];
    double *y = new double[n];

    srand(time(NULL) + world_rank);
    for (int i = 0; i < n; i++) {
        x[i] = rand() % 100;
        y[i] = rand() % 100;
    }

    double local_sum = 0;
    for (int i = world_rank; i < n; i += world_size) {
        local_sum += x[i] * y[i];
    }

    MPI_Barrier(MPI_COMM_WORLD);

    double global_sum;
    MPI_Reduce(&local_sum, &global_sum, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    if (world_rank == 0) {
        cout << "Scalar product = " << global_sum << endl;
    }

    delete[] x;
    delete[] y;

    MPI_Finalize();
    return 0;
}