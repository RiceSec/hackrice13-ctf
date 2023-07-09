
#include <stdio.h>

int main() {
    char x[11] = {0x41, 's', 'M'};
    
    x[3] = 0x5F;
    x[0] = '@';
    x[4] = 0x31;
    x[5] = 's';

    if (15 % 2 == 1) {
        x[6] = '3';
        x[8] = 0x45;
    } else {
        x[6] = 122;   
    }
    if (1)
        x[9] = 122;
    x[7] = '_';
    
    
    x[10] = '*';
    printf("%s", x);
    return 0; 
}
