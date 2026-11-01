/*
 * IT302 DCCN Lab - Question 9.3
 * Error Detection: Cyclic Redundancy Check (CRC) using Modulo-2 Division (XOR)
 */

#include <stdio.h>
#include <string.h>

void xor_division(char *dividend, const char *divisor, char *remainder) {
    int n = (int)strlen(dividend);
    int k = (int)strlen(divisor);
    char temp[256];
    strcpy(temp, dividend);

    for (int i = 0; i <= n - k; i++) {
        if (temp[i] == '1') {
            for (int j = 0; j < k; j++) {
                temp[i + j] = (temp[i + j] == divisor[j]) ? '0' : '1';
            }
        }
    }
    // Copy the last (k - 1) bits as the remainder
    strncpy(remainder, &temp[n - k + 1], k - 1);
    remainder[k - 1] = '\0';
}

int main(void) {
    char data[128], gen[32], dividend[256], rem[32], codeword[256], rx[256], rx_rem[32];

    printf("--- 9.3 Cyclic Redundancy Check (CRC) ---\n");
    printf("Enter data bits (e.g. 100100): ");
    if (scanf("%127s", data) != 1) return 1;

    printf("Enter generator polynomial (e.g. 1101): ");
    if (scanf("%31s", gen) != 1) return 1;

    int gen_len = (int)strlen(gen);
    int data_len = (int)strlen(data);

    // Prepare dividend: data appended with (gen_len - 1) zeros
    strcpy(dividend, data);
    for (int i = 0; i < gen_len - 1; i++) {
        dividend[data_len + i] = '0';
    }
    dividend[data_len + gen_len - 1] = '\0';

    // Calculate CRC remainder at sender
    xor_division(dividend, gen, rem);

    // Transmitted codeword = data + remainder
    strcpy(codeword, data);
    strcat(codeword, rem);

    printf("\n[Sender] CRC Checksum (Remainder): %s\n", rem);
    printf("[Sender] Transmitted Codeword     : %s\n", codeword);

    // Receiver Check
    printf("\n[Receiver] Enter received codeword (or test with %s): ", codeword);
    if (scanf("%255s", rx) != 1) return 1;

    xor_division(rx, gen, rx_rem);

    // Check if remainder is all zeros
    int has_error = 0;
    for (int i = 0; i < gen_len - 1; i++) {
        if (rx_rem[i] != '0') {
            has_error = 1;
            break;
        }
    }

    printf("[Receiver] Remainder after division: %s\n", rx_rem);
    if (has_error) {
        printf("[Receiver] Status: ERROR DETECTED! Remainder is non-zero.\n");
    } else {
        printf("[Receiver] Status: NO ERROR DETECTED. Codeword accepted.\n");
    }

    return 0;
}

