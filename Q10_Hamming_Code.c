/*
 * IT302 DCCN Lab - Question 10
 * Program to perform Error Detection and Correction using Hamming Code (7, 4).
 * 4 data bits (d1, d2, d3, d4) encoded into 7-bit codeword with 3 parity bits (p1, p2, p4).
 */

#include <stdio.h>

int main(void) {
    int data[4];      // d1, d2, d3, d4
    int code[8];      // 1-indexed: code[1] to code[7]
    int rx[8];        // received codeword
    int s1, s2, s4, error_pos;

    printf("--- Error Correction using Hamming Code (7, 4) ---\n");
    printf("Enter 4 data bits (separated by spaces, e.g. 1 0 1 1): ");
    for (int i = 0; i < 4; i++) {
        if (scanf("%d", &data[i]) != 1) return 1;
    }

    // Placing data bits at positions 3, 5, 6, 7
    code[3] = data[0]; // d1
    code[5] = data[1]; // d2
    code[6] = data[2]; // d3
    code[7] = data[3]; // d4

    // Calculating even parity bits at powers of 2: 1, 2, 4
    code[1] = code[3] ^ code[5] ^ code[7]; // p1 covers 1, 3, 5, 7
    code[2] = code[3] ^ code[6] ^ code[7]; // p2 covers 2, 3, 6, 7
    code[4] = code[5] ^ code[6] ^ code[7]; // p4 covers 4, 5, 6, 7

    printf("\n[Sender] Parity Bits: p1 = %d, p2 = %d, p4 = %d\n", code[1], code[2], code[4]);
    printf("[Sender] Transmitted 7-bit Codeword: ");
    for (int i = 1; i <= 7; i++) printf("%d", code[i]);
    printf("\n  (Bit order: p1 p2 d1 p4 d2 d3 d4)\n");

    // Receiver Simulation
    printf("\n[Receiver] Enter 7 received bits (separated by spaces): ");
    for (int i = 1; i <= 7; i++) {
        scanf("%d", &rx[i]);
    }

    // Calculate syndrome bits
    s1 = rx[1] ^ rx[3] ^ rx[5] ^ rx[7];
    s2 = rx[2] ^ rx[3] ^ rx[6] ^ rx[7];
    s4 = rx[4] ^ rx[5] ^ rx[6] ^ rx[7];

    error_pos = (s4 * 4) + (s2 * 2) + (s1 * 1);

    if (error_pos == 0) {
        printf("\n[Receiver] Status: NO ERROR DETECTED! Codeword is correct.\n");
    } else {
        printf("\n[Receiver] Status: ERROR DETECTED at bit position %d!\n", error_pos);
        rx[error_pos] = 1 - rx[error_pos]; // Correct the erroneous bit
        printf("[Receiver] Corrected Codeword: ");
        for (int i = 1; i <= 7; i++) printf("%d", rx[i]);
        printf("\n[Receiver] Recovered Data Bits: %d %d %d %d\n", rx[3], rx[5], rx[6], rx[7]);
    }

    return 0;
}

