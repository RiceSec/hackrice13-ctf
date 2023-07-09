#include <stdio.h>
#include <string.h>

char rot13(char c) {
    if ('a' <= c && c <= 'z') {
        return (c - 'a' + 13) % 26 + 'a';
    } else if ('A' <= c && c <= 'Z') {
        return (c - 'A' + 13) % 26 + 'A';
    } else {
        return c;
    }
}

int main() {
    char buf[100];
    puts("Please enter the flag:");
    scanf("%99s", buf);
    for (char *p = buf; *p; p++) {
        *p = rot13(*p);
    }
    if (strcmp("unpxevpr{1_gu1Ax_gu15_5gE1At_u@5_e0gGrq}", buf) == 0) {
        puts("Wow! You found the flag!");
    } else {
        puts("Nope!");
    }
    return 0;
}
