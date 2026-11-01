/*
 * IT302 DCCN Lab - Question 7
 * Program to perform Bit Stuffing and De-stuffing (HDLC / Framing).
 * Rule: After five consecutive 1s, a '0' is stuffed at sender and removed at receiver.
 */

#include <stdio.h>
#include <string.h>

#define FLAG "01111110"

void bit_stuff(const char *in, char *out) {
    int count = 0, j = 0;
    for (int i = 0; in[i] != '\0'; i++) {
        out[j++] = in[i];
        if (in[i] == '1') {
            count++;
            if (count == 5) {
                out[j++] = '0'; // Stuff '0'
                count = 0;
            }
        } else {
            count = 0;
        }
    }
    out[j] = '\0';
}

void bit_destuff(const char *in, char *out) {
    int count = 0, j = 0;
    for (int i = 0; in[i] != '\0'; i++) {
        out[j++] = in[i];
        if (in[i] == '1') {
            count++;
            if (count == 5) {
                if (in[i + 1] == '0') {
                    i++; // Skip the stuffed '0'
                }
                count = 0;
            }
        } else {
            count = 0;
        }
    }
    out[j] = '\0';
}

int main(void) {
    char data[256], stuffed[512], destuffed[256];

    printf("Enter binary data string (e.g. 01111110111110): ");
    if (scanf("%255s", data) != 1) return 1;

    // Validate binary string
    for (int i = 0; data[i] != '\0'; i++) {
        if (data[i] != '0' && data[i] != '1') {
            printf("Error: Input must only contain '0' and '1'!\n");
            return 1;
        }
    }

    bit_stuff(data, stuffed);
    bit_destuff(stuffed, destuffed);

    printf("\n--- Bit Stuffing & De-stuffing Results ---\n");
    printf("Original Data   : %s\n", data);
    printf("Stuffed Payload : %s\n", stuffed);
    printf("Transmitted Frame: %s %s %s\n", FLAG, stuffed, FLAG);
    printf("De-stuffed Data : %s\n", destuffed);
    printf("Integrity Match : %s\n", (strcmp(data, destuffed) == 0) ? "SUCCESS" : "FAILED");

    return 0;
}

