/*
 * IT302 DCCN Lab - Question 14
 * Simulation of DHCP (Dynamic Host Configuration Protocol) Server
 * Simulates DORA Workflow: Discover -> Offer -> Request -> Acknowledge.
 * Manages IP Address Pool, Client Leases, Gateway, DNS, and Subnet Mask.
 */

#include <stdio.h>
#include <string.h>

#define POOL_SIZE 8
#define SUBNET_MASK "255.255.255.0"
#define DEFAULT_GATEWAY "192.168.1.1"
#define DNS_SERVER "8.8.8.8"
#define LEASE_TIME 3600 // seconds

typedef struct {
    char ip[16];
    char mac[18];
    int allocated;
} Lease;

Lease ip_pool[POOL_SIZE];

void init_pool(void) {
    for (int i = 0; i < POOL_SIZE; i++) {
        snprintf(ip_pool[i].ip, sizeof(ip_pool[i].ip), "192.168.1.%d", 100 + i);
        ip_pool[i].mac[0] = '\0';
        ip_pool[i].allocated = 0;
    }
}

void display_pool(void) {
    printf("\n=== Current DHCP IP Pool & Leases ===\n");
    printf("%-5s | %-16s | %-18s | %-10s\n", "Index", "IP Address", "Client MAC", "Status");
    printf("---------------------------------------------------------\n");
    for (int i = 0; i < POOL_SIZE; i++) {
        printf("%-5d | %-16s | %-18s | %-10s\n",
               i + 1,
               ip_pool[i].ip,
               ip_pool[i].allocated ? ip_pool[i].mac : "None",
               ip_pool[i].allocated ? "LEASED" : "AVAILABLE");
    }
    printf("=========================================================\n");
}

void allocate_ip(const char *mac) {
    // 1. Check if MAC already holds a lease
    for (int i = 0; i < POOL_SIZE; i++) {
        if (ip_pool[i].allocated && strcmp(ip_pool[i].mac, mac) == 0) {
            printf("\n[!] Client %s already holds lease for IP: %s\n", mac, ip_pool[i].ip);
            return;
        }
    }

    // 2. Find first free IP
    int free_idx = -1;
    for (int i = 0; i < POOL_SIZE; i++) {
        if (!ip_pool[i].allocated) {
            free_idx = i;
            break;
        }
    }

    if (free_idx == -1) {
        printf("\n[-] DHCP Server Error: IP pool exhausted! No IP available.\n");
        return;
    }

    // 3. Simulate DORA 4-way handshake
    printf("\n--- Simulating DHCP DORA Exchange ---\n");
    printf("1. [Client -> Broadcast] DHCP DISCOVER (Looking for DHCP Server from MAC %s)\n", mac);
    printf("2. [Server -> Client   ] DHCP OFFER    (Offering IP: %s)\n", ip_pool[free_idx].ip);
    printf("3. [Client -> Server   ] DHCP REQUEST  (Requesting lease for %s)\n", ip_pool[free_idx].ip);
    printf("4. [Server -> Client   ] DHCP ACK      (Confirmed IP Lease)\n");

    // Commit lease
    ip_pool[free_idx].allocated = 1;
    strncpy(ip_pool[free_idx].mac, mac, sizeof(ip_pool[free_idx].mac) - 1);

    printf("\n[+] Lease Granted successfully!\n");
    printf("    Assigned IP    : %s\n", ip_pool[free_idx].ip);
    printf("    Subnet Mask    : %s\n", SUBNET_MASK);
    printf("    Default Gateway: %s\n", DEFAULT_GATEWAY);
    printf("    DNS Server     : %s\n", DNS_SERVER);
    printf("    Lease Duration : %d seconds\n", LEASE_TIME);
}

void release_ip(const char *mac) {
    for (int i = 0; i < POOL_SIZE; i++) {
        if (ip_pool[i].allocated && strcmp(ip_pool[i].mac, mac) == 0) {
            ip_pool[i].allocated = 0;
            ip_pool[i].mac[0] = '\0';
            printf("\n[+] DHCP RELEASE received: IP %s released by MAC %s.\n", ip_pool[i].ip, mac);
            return;
        }
    }
    printf("\n[-] No active lease found for MAC: %s\n", mac);
}

int main(void) {
    init_pool();
    int choice;
    char mac[18];

    printf("==========================================\n");
    printf("       DHCP SERVER SIMULATION SYSTEM      \n");
    printf("==========================================\n");

    while (1) {
        printf("\n1. Request IP Address (DORA Workflow)\n");
        printf("2. Release IP Address (DHCP RELEASE)\n");
        printf("3. View IP Pool and Lease Status\n");
        printf("4. Exit\n");
        printf("Enter your choice (1-4): ");
        if (scanf("%d", &choice) != 1) break;

        switch (choice) {
            case 1:
                printf("Enter Client MAC Address (e.g. AA:BB:CC:DD:EE:01): ");
                scanf("%17s", mac);
                allocate_ip(mac);
                break;
            case 2:
                printf("Enter Client MAC Address to Release: ");
                scanf("%17s", mac);
                release_ip(mac);
                break;
            case 3:
                display_pool();
                break;
            case 4:
                printf("Exiting DHCP Server Simulation.\n");
                return 0;
            default:
                printf("Invalid selection!\n");
        }
    }
    return 0;
}

