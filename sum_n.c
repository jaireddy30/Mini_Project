// sum_n.c
// Reads a single integer n from stdin and prints the sum of first n natural numbers.
#include <stdio.h>

int main() {
    long long n;
    if (scanf("%lld", &n) != 1) {
        printf("Error: expected an integer\\n");
        return 1;
    }
    if (n < 0) {
        printf("Error: n must be non-negative\\n");
        return 2;
    }
    long long sum = n * (n + 1) / 2;
    printf("Sum of first %lld natural numbers is %lld\\n", n, sum);
    return 0;
}