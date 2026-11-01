/*
 * IT302 DCCN Lab - Question 6
 * Program to translate a dotted decimal IPv4 address into a 32-bit binary and integer address.
 */

#include <stdio.h>

void print_binary8(unsigned int n) {
    for (int i = 7; i >= 0; i--) {
        putchar((n & (1 << i)) ? '1' : '0');
    }
}

int main(void) {
    char ip[32];
    unsigned int o1, o2, o3, o4;

    printf("Enter IPv4 Address in dotted decimal (e.g. 192.168.1.1): ");
    if (scanf("%31s", ip) != 1) return 1;

    if (sscanf(ip, "%u.%u.%u.%u", &o1, &o2, &o3, &o4) != 4 ||
        o1 > 255 || o2 > 255 || o3 > 255 || o4 > 255) {
        printf("Error: Invalid dotted decimal address!\n");
        return 1;
    }

    unsigned int addr32 = (o1 << 24) | (o2 << 16) | (o3 << 8) | o4;

    printf("\n--- Conversion Results ---\n");
    printf("Dotted Decimal  : %u.%u.%u.%u\n", o1, o2, o3, o4);
    printf("32-bit Binary   : ");
    print_binary8(o1); putchar(' ');
    print_binary8(o2); putchar(' ');
    print_binary8(o3); putchar(' ');
    print_binary8(o4); putchar('\n');
    printf("Continuous Bits : ");
    print_binary8(o1); print_binary8(o2); print_binary8(o3); print_binary8(o4);
    putchar('\n');
    printf("32-bit Unsigned : %u\n", addr32);
    printf("32-bit Hex      : 0x%08X\n", addr32);

    return 0;
}

