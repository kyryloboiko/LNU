#include <stdio.h>
#include <omp.h>

int main(int argc, char *argv[]) {
    int n = 5;
    int tid;

    #pragma omp parallel num_threads(n) private(tid)
    {
        int tid = omp_get_thread_num(); 
        int num_threads = omp_get_num_threads();

        printf("I am thread %d from %d threads! Available processors: %d\n", tid, num_threads, omp_get_num_procs());

        #pragma omp sections
        {
            #pragma omp section
            {
                printf("Hello from section 1, thread %d\n", tid);
            }

            #pragma omp section
            {
                printf("Hello from section 2, thread %d\n", tid);
            }

            #pragma omp section
            {
                printf("Hello from section 3, thread %d\n", tid);
            }
        }
    }

    return 0;
}
