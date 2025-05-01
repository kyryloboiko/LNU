#include <mpi.h>
#include <iostream>
#include <cstring>

int main(int argc, char** argv) {
    int rank, size, newrank, newsize;
    char message[32] = "Привіт, МРІ!";

    MPI_Comm newcomm;
    MPI_Group oldgroup, newgroup;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    MPI_Comm_group(MPI_COMM_WORLD, &oldgroup);
    int ranks[2] = {1, 3};
    MPI_Group_incl(oldgroup, 2, ranks, &newgroup);
    MPI_Comm_create(MPI_COMM_WORLD, newgroup, &newcomm);

    MPI_Comm_size(newcomm, &newsize);
    MPI_Comm_rank(newcomm, &newrank);

    if (newcomm != MPI_COMM_NULL) {
        if (newrank == 0) {
            std::cout << "Введіть повідомлення (макс. 32 символи): ";
            std::cin >> message;
        }

        MPI_Bcast(message, 32, MPI_CHAR, 0, newcomm);
        
        if (newcomm != MPI_COMM_NULL) {
            std::cout << "Новий комунікатор: процес " << rank << " з rank" << newrank
            << " має доступ; розмір комунікатора: " << newsize << std::endl;
            std::cout << "Повідомлення: " << message << std::endl;
        }
    }
        
    if (rank == 0) {
        std::cout << "MPI_COMM_WORLD: процес " << rank << " з rank" << newrank
        << "; розмір комунікатора: " << size << std::endl;
        std::cout << "Новий комунікатор: немає доступу" << std::endl;
    }

    MPI_Group_free(&newgroup);
    MPI_Group_free(&oldgroup);

    if (newcomm != MPI_COMM_NULL) {
        MPI_Comm_free(&newcomm);
    }

    MPI_Finalize();
    return 0;
}