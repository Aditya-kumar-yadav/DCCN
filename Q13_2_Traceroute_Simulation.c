/*
 * IT302 DCCN Lab - Question 13.2
 * Simulation of TRACEROUTE Command in C
 * Simulates hop-by-hop packet routing with increasing TTL (1, 2, 3...),
 * intermediate router ICMP Time Exceeded responses, 3 probe latency samples, and route completion.
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#ifdef _WIN32
  #include <windows.h>
  #define SLEEP_MS(ms) Sleep(ms)
#else
  #include <unistd.h>
  #define SLEEP_MS(ms) usleep((ms) * 1000)
#endif

// Simulated hop router addresses
const char *simulated_hops[] = {
    "172.16.8.1",       // Hop 1: Lab Default Gateway
    "172.16.13.1",      // Hop 2: Campus Core Switch
    "136.232.33.117",   // Hop 3: ISP Border Router
    "49.44.59.153",     // Hop 4: National Backbone Router
    "72.14.243.188",    // Hop 5: Peering Exchange
    "142.250.143.138"   // Hop 6: Target Destination
};

int main(void) {
    char target[128];
    int max_hops = 10;
    int total_sim_hops = sizeof(simulated_hops) / sizeof(simulated_hops[0]);

    srand((unsigned int)time(NULL));

    printf("--- 13.2 TRACEROUTE Simulation ---\n");
    printf("Enter destination hostname or IP (e.g. google.com): ");
    if (scanf("%127s", target) != 1) return 1;

    printf("\nTracing route to %s over a maximum of %d hops:\n\n", target, max_hops);
    printf("  Hop     RTT 1      RTT 2      RTT 3    IP Address\n");
    printf("  --------------------------------------------------------\n");

    int base_latency = 1;

    for (int ttl = 1; ttl <= max_hops; ttl++) {
        SLEEP_MS(300); // Simulate network round-trip delay

        int hop_idx = ttl - 1;
        if (hop_idx >= total_sim_hops) {
            break;
        }

        // Generate 3 probe latencies
        int rtt1 = base_latency + (rand() % 5);
        int rtt2 = base_latency + (rand() % 5);
        int rtt3 = base_latency + (rand() % 5);

        // Simulate occasional packet drop (timeout)
        int timeout_hop = (ttl == 5 && (rand() % 4 == 0));

        if (timeout_hop) {
            printf("  %2d        *          *          *      Request timed out.\n", ttl);
        } else {
            printf("  %2d     %3d ms     %3d ms     %3d ms    %s\n",
                   ttl, rtt1, rtt2, rtt3, simulated_hops[hop_idx]);
        }

        base_latency += 7 + (rand() % 8); // Latency increases as distance grows

        // Check if destination reached
        if (hop_idx == total_sim_hops - 1) {
            printf("\nTrace complete. Destination reached in %d hops.\n", ttl);
            return 0;
        }
    }

    printf("\nTrace complete.\n");
    return 0;
}

