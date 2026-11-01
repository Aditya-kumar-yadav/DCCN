/*
 * IT302 DCCN Lab - Question 9.1
 * Error Detection: Single Parity Checking Method (Even & Odd Parity)
 */

#include <stdio.h>
#include <string.h>

int count_ones(const char *bits) {
    int count = 0;
    for (int i = 0; bits[i] != '\0'; i++) {
        if (bits[i] == '1') count++;
    }
    return count;
}

int main(void) {
    char data[64], tx_code[65], rx_code[65];
    int choice;

    printf("--- 9.1 Single Parity Check ---\n");
    printf("Enter binary data bits (e.g. 1011001): ");
    if (scanf("%63s", data) != 1) return 1;

    printf("Select Parity Scheme (1: Even Parity, 2: Odd Parity): ");
    if (scanf("%d", &choice) != 1) return 1;

    int ones = count_ones(data);
    char parity_bit;

    if (choice == 1) { // Even parity
        parity_bit = (ones % 2 == 0) ? '0' : '1';
    } else {           // Odd parity
        parity_bit = (ones % 2 == 0) ? '1' : '0';
    }

    // Sender codeword
    strcpy(tx_code, data);
    int len = (int)strlen(data);
    tx_code[len] = parity_bit;
    tx_code[len + 1] = '\0';

    printf("\n[Sender] Parity Bit Added : %c\n", parity_bit);
    printf("[Sender] Transmitted Code : %s\n", tx_code);

    // Receiver check
    printf("\n[Receiver] Enter received codeword (or test with %s): ", tx_code);
    if (scanf("%64s", rx_code) != 1) return 1;

    int rx_ones = count_ones(rx_code);
    int error = 0;
    if (choice == 1) {
        error = (rx_ones % 2 != 0);
    } else {
        error = (rx_ones % 2 == 0);
    }

    if (error) {
        printf("[Receiver] Status: ERROR DETECTED! Parity check failed.\n");
    } else {
        printf("[Receiver] Status: NO ERROR DETECTED. Data accepted.\n");
    }

    return 0;
}

