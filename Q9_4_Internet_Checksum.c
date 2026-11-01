/*
 * IT302 DCCN Lab - Question 9.4
 * Error Detection: Internet Checksum Method (16-bit One's Complement Addition)
 * As used in IPv4, TCP, and UDP headers (RFC 1071).
 */

#include <stdio.h>

unsigned short compute_checksum(const unsigned short *words, int n) {
    unsigned int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += words[i];
        // Fold 32-bit sum into 16 bits (end-around carry)
        while (sum >> 16) {
            sum = (sum & 0xFFFF) + (sum >> 16);
        }
    }
    return (unsigned short)(~sum & 0xFFFF); // One's complement
}

int verify_checksum(const unsigned short *words, int n, unsigned short checksum) {
    unsigned int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += words[i];
        while (sum >> 16) {
            sum = (sum & 0xFFFF) + (sum >> 16);
        }
    }
    sum += checksum;
    while (sum >> 16) {
        sum = (sum & 0xFFFF) + (sum >> 16);
    }
    return (unsigned short)(~sum & 0xFFFF) == 0;
}

int main(void) {
    int n;
    unsigned short data[16];

    printf("--- 9.4 Internet Checksum (16-bit Words) ---\n");
    printf("Enter number of 16-bit words (e.g. 3): ");
    if (scanf("%d", &n) != 1 || n <= 0 || n > 16) return 1;

    printf("Enter %d words in hexadecimal (e.g. 4500 003c 1c46):\n", n);
    for (int i = 0; i < n; i++) {
        unsigned int val;
        printf("  Word %d: 0x", i + 1);
        scanf("%x", &val);
        data[i] = (unsigned short)(val & 0xFFFF);
    }

    unsigned short checksum = compute_checksum(data, n);
    printf("\n[Sender] Calculated 16-bit Checksum: 0x%04X\n", checksum);

    // Receiver Verification
    printf("\n--- Receiver Verification ---\n");
    printf("Enter received checksum (or press matching: 0x%04X): 0x", checksum);
    unsigned int rx_chk;
    scanf("%x", &rx_chk);

    if (verify_checksum(data, n, (unsigned short)(rx_chk & 0xFFFF))) {
        printf("[Receiver] Status: NO ERROR DETECTED. Sum is 0xFFFF (~Sum = 0x0000).\n");
    } else {
        printf("[Receiver] Status: ERROR DETECTED! Checksum verification failed.\n");
    }

    return 0;
}

