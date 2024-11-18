#include <stdio.h>
#include <omp.h>

int main(int argc, char *argv[]) {
    int n; // кількість потоків

    // Починаємо паралельну область
    #pragma omp parallel num_threads(n) private(tid)
    {
        int tid = omp_get_thread_num(); // Отримуємо номер потоку
        int num_threads = omp_get_num_threads(); // Загальна кількість потоків

        // Виводимо інформацію про номери
        printf("I am thread %d from %d threads! Available processors: %d\n", tid, num_threads, omp_get_num_procs());

        // Розділяємо паралельну область на секції
        #pragma omp sections
        {
            // Перша секція
            #pragma omp section
            {
                printf("Hello from section 1, thread %d\n", tid);
            }

            // Друга секція
            #pragma omp section
            {
                printf("Hello from section 2, thread %d\n", tid);
            }

            // Третя секція
            #pragma omp section
            {
                printf("Hello from section 3, thread %d\n", tid);
            }
        }
    }

    return 0;
}