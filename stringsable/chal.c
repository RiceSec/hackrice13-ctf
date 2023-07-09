#include <stdio.h>
#include <string.h>

int main() {
    char buf[100];
    puts("Please enter the flag:");
    scanf("%99s", buf);
    if (strcmp("hackrice{c@N_duCk5_3aT_5tr1nG_ch335e}", buf) == 0) {
        puts("Wow! You found the flag!");
    } else {
        puts("Nope!");
    }
    return 0;
}
