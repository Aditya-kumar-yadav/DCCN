/*
 * IT302 DCCN Lab - Question 5
 * Program to determine whether an IPv4 address is in Class A, B, C, D, or E.
 */

#include <stdio.h>

int main(void) {
    char ip[32];
    int o1, o2, o3, o4;

    printf("Enter IPv4 Address (e.g. 192.168.1.1): ");
    if (scanf("%31s", ip) != 1) return 1;

    if (sscanf(ip, "%d.%d.%d.%d", &o1, &o2, &o3, &o4) != 4 ||
        o1 < 0 || o1 > 255 || o2 < 0 || o2 > 255 ||
        o3 < 0 || o3 > 255 || o4 < 0 || o4 > 255) {
        printf("Invalid IPv4 address format!\n");
        return 1;
    }

    printf("\n--- IP Classification Result ---\n");
    printf("IP Address : %d.%d.%d.%d\n", o1, o2, o3, o4);

    if (o1 >= 0 && o1 <= 127) {
        printf("Class      : Class A\n");
        printf("Subnet Mask: 255.0.0.0\n");
        printf("Network ID : %d.0.0.0\n", o1);
        printf("Host ID    : 0.%d.%d.%d\n", o2, o3, o4);
    } else if (o1 >= 128 && o1 <= 191) {
        printf("Class      : Class B\n");
        printf("Subnet Mask: 255.255.0.0\n");
        printf("Network ID : %d.%d.0.0\n", o1, o2);
        printf("Host ID    : 0.0.%d.%d\n", o3, o4);
    } else if (o1 >= 192 && o1 <= 223) {
        printf("Class      : Class C\n");
        printf("Subnet Mask: 255.255.255.0\n");
        printf("Network ID : %d.%d.%d.0\n", o1, o2, o3);
        printf("Host ID    : 0.0.0.%d\n", o4);
    } else if (o1 >= 224 && o1 <= 239) {
        printf("Class      : Class D (Multicast)\n");
    } else {
        printf("Class      : Class E (Experimental / Reserved)\n");
    }

    return 0;
}

