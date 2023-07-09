#include <stdio.h>
#include <string.h>

int main() {
    char response[100];

    puts("Please enter some text:");
    gets(response);

    int quacks = 0;
    char *s = response;
    // look for the next quack
    while ((s = strstr(s, "quack"))) {
        s += 5; // skip past the quack
        quacks++;
    }

    printf("There were a total of %u quacks in your text!\n", quacks);

    return 0;
}