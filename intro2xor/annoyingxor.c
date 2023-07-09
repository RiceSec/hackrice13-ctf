#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char* partialXOR(char arr[], int start, int end, char key) {
    char* result = (char*)malloc(sizeof(char) * 11); 
    for (int i = start; i < end; i++) {
        result[i - start] = arr[i] ^ key;
    }
    result[end - start] = '\0'; 
    return result;
}

int main() {
    char input[64];
    printf("What is the password?");
    scanf("%63s", input); 
    int input_size = strlen(input);
    if (input_size < 30) {
        printf("Wrong password.\n"); 
        exit(1); 
    }
    char result[31];
    char* seg_1 = partialXOR(input, 0, 10, 0x0A);
    char* seg_2 = partialXOR(input, 10, 20, 0x27);
    char* seg_3 = partialXOR(input, 20, 30, 0x6F);
    strcpy(result, seg_1); 
    strcat(result, seg_2);
    strcat(result, seg_3);
    char key[] = {
        0x7D, 0x62, 0x65, 0x63, 0x79, 0x79, 0x69, 0x6B, 0x78, 0x6F,
        0x43, 0x48, 0x41, 0x41, 0x4B, 0x5E, 0x6E, 0x49, 0x40, 0x68,
        0x0A, 0x0C, 0x04, 0x0A, 0x50, 0x01, 0x00, 0x0B, 0x02, 0x0A,
        0x00
    };
    if (strcmp(result, key) == 0) {
        system("cat flag.txt");
    } else {
        printf("Wrong password.\n");
    }
    free(seg_1);
    free(seg_2);
    free(seg_3);

    return 0;
}
