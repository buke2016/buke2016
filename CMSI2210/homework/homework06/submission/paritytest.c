// test_parity.c

#include <stdio.h>

extern unsigned char paritygen(unsigned char data);

int main() {
    unsigned char data = 0b10110010;
    unsigned char parity = paritygen(data);
    
    printf("Data: %d = 0b", data);
    
    // Print binary representation
    for(int i = 7; i >= 0; i--) {
        printf("%d", (data >> i) & 1); 
    }
    
    printf("\nParity Bit: %d\n", parity);
    
    return 0;
}
