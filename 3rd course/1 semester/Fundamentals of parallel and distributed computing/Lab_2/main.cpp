#include <iostream>
#include <omp.h>
#include <cstdlib> 
#include <ctime>   

#define N1 150 
#define N2 350 

void calculate_sum(int matrix_size, int num_threads, int schedule_type) {
    int matrix[matrix_size][matrix_size];
    int i, j, sum;
    double start_time, end_time;

    srand(15000);
    for (i = 0; i < matrix_size; i++) {
        for (j = 0; j < matrix_size; j++) {
            matrix[i][j] = rand() % 100 + 1;
        }
    }

    omp_set_num_threads(num_threads);

    sum = 0;
    start_time = omp_get_wtime();

    #pragma omp parallel for private(j) reduction(+:sum) schedule(dynamic, 100)
    for (i = 0; i < matrix_size; i++) {
        int max = matrix[i][0];
        int thread_num = omp_get_thread_num();
        if (schedule_type == 2) {
            printf("[%d]: calculation of the iteration number %d.\n", thread_num + 1, i);
        }
        for (j = 1; j < matrix_size; j++) {
            if (matrix[i][j] > max) {
                max = matrix[i][j];
            }
        }
        sum += max;
    }

    end_time = omp_get_wtime();

    std::cout << "Matrix size: " << matrix_size << " x " << matrix_size << std::endl;
    std::cout << "Sum of maximum row elements of a matrix: " << sum << std::endl;
    std::cout << "Program execution time with " << omp_get_max_threads() << " threads: " << end_time - start_time << " seconds" << std::endl;
}

int main() {
    calculate_sum(N1, 4, 1);

    calculate_sum(N2, 2, 2);

    return 0;
}
