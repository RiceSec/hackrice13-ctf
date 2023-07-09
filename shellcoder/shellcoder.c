#include <stdio.h>

int main() {
    char shellcode[1024];
    puts("Please enter shellcode:");
    fgets(shellcode, 1024, stdin);

    // Call the shellcode as a function
    ((void(*)())shellcode)();
    
    return 0;
}