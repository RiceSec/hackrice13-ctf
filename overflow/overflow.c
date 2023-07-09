#include <stdio.h>
#include <string.h>
#include <stdbool.h>

void print_file(char *filename) {
    FILE *f = fopen(filename, "r");
    if (f) {
        int c;
        while ((c = fgetc(f)) != EOF) {
            putc(c, stdout);
        }
        fclose(f);
    }
}

int main() {
    char command[128];
    char username[128];

    puts("Please enter your username:");
    gets(username);

    if (strcmp(username, "admin") == 0) {
        puts("Sorry, remote logins are disabled for the admin account.");
        return 0;
    }

    printf("Welcome, %s. Run 'help' to see a list of available commands.\n", username);

    while (true) {
        puts("Please enter a command:");
        gets(command);

        if (memcmp(command, "help", 4) == 0) {
            puts("Available commands:");
            puts("  help          - prints this list");
            puts("  list          - lists files on the system");
            puts("  read FILENAME - prints the contents of a file");
            puts("  exit          - exits");
        } else if (memcmp(command, "list", 4) == 0) {
            puts("Files:");
            puts("  flag.txt");
            puts("  lecture.txt");
        } else if (memcmp(command, "read ", 5) == 0) {
            char *filename = command + 5;
            if (memcmp(filename, "flag.txt", 8) == 0) {
                if (strcmp(username, "admin") == 0) {
                    print_file("flag.txt");
                } else {
                    printf("Sorry, the user '%s' cannot read 'flag.txt'.\n", username);
                }
            } else if (memcmp(filename, "lecture.txt", 11) == 0) {
                print_file("lecture.txt");
            } else {
                puts("Unknown file.");
            }
        } else if (memcmp(command, "exit", 4) == 0) {
            return 0;
        } else {
            puts("Unknown command!");
        }
    }
}