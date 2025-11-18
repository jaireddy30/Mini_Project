// even_odd.c
// Reads a single integer from stdin and prints whether it is Even or Odd.
#include <stdio.h>

int main() {
    int num;
    if (scanf("%d", &num) != 1) {
        printf("Error: expected an integer\\n");
        return 1;
    }
    if (num % 2 == 0) {
        printf("%d is Even.\\n", num);
    } else {
        printf("%d is Odd.\\n", num);
    }
    return 0;
}