#include <stdio.h>
#include <stdint.h>

extern uint32_t makeNBO(uint32_t num);

int main() {
    uint32_t input_values[] = {0x12345678, 0xAABBCCDD, 0x11223344, 0x99887766, 0x55667788};
    printf("Original number: 0x%x, Swapped number: 0x%x\n", input_values[0], makeNBO(input_values[0]));
    printf("Original number: 0x%x, Swapped number: 0x%x\n", input_values[1], makeNBO(input_values[1]));
    printf("Original number: 0x%x, Swapped number: 0x%x\n", input_values[2], makeNBO(input_values[2]));
    printf("Original number: 0x%x, Swapped number: 0x%x\n", input_values[3], makeNBO(input_values[3]));
    printf("Original number: 0x%x, Swapped number: 0x%x\n", input_values[4], makeNBO(input_values[4]));

    return 0;
}
