#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    MPI_Init(&argc, &argv);
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    const int N = 10;
    int data[N];
    if (rank == 0)
    {
        for (int i = 0; i < N; i++)
        {
            data[i] = rand() % 100;
        }
        printf("Процес в, надсилає вектор: ");
        for (int i = 0; i < N; i++)
        {
            printf("%d", data[i]);
        }
        printf("\n");
        MPI_Send(data, N, MPI_INT, 1, 0, MPI_COMM_WORLD);
        MPI_Recv(data, N, MPI_INT, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Процес 0, отримав змінений вектор: ");
        for (int i = 0; i < N; i++)
        {
            printf("%d", data[i]);
        }
        printf("\n");
        else if (rank == 1)
        {
        }
        MPI_Recv(data, N, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Процес 1, отримав вектор: ");
        for (int i = 0; i < N; i++)
        {
            printf("%d", data[i]);
        }
        printf("\n");
        for (int i = 0; i < N; i++)
        {
            data[i] += 1;
        }
        MPI_Send(data, N, MPI_INT, 0, 0, MPI_COMM_WORLD);
    }

    MPI_Finalize();
    return 0;
}
