/*
 * IT302 DCCN Lab - Question 13.1
 * Simulation of PING Command in C
 * Simulates sending ICMP Echo Requests, calculating RTT with realistic latency,
 * packet loss, and generating summary statistics (min/max/avg RTT).
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

int main(void) {
    char target[128];
    int count = 4;
    int bytes = 32;
    int ttl = 64;

    srand((unsigned int)time(NULL));

    printf("--- 13.1 PING Command Simulation ---\n");
    printf("Enter target hostname or IP (e.g. google.com): ");
    if (scanf("%127s", target) != 1) return 1;

    printf("\nPinging %s with %d bytes of data:\n\n", target, bytes);

    int sent = 0, received = 0;
    int min_rtt = 9999, max_rtt = 0, sum_rtt = 0;

    for (int seq = 1; seq <= count; seq++) {
        sent++;
        SLEEP_MS(500); // Simulate transmission interval

        // Simulate 10% packet drop chance
        int drop = (rand() % 10 == 0);

        if (drop) {
            printf("Request timed out.\n");
        } else {
            // Simulate RTT between 20ms and 80ms
            int rtt = 20 + (rand() % 61);
            received++;
            sum_rtt += rtt;
            if (rtt < min_rtt) min_rtt = rtt;
            if (rtt > max_rtt) max_rtt = rtt;

            printf("Reply from %s: bytes=%d time=%dms TTL=%d (icmp_seq=%d)\n",
                   target, bytes, rtt, ttl, seq);
        }
    }

    int lost = sent - received;
    double loss_percent = ((double)lost / sent) * 100.0;

    printf("\n--- Ping statistics for %s ---\n", target);
    printf("    Packets: Sent = %d, Received = %d, Lost = %d (%.0f%% loss),\n",
           sent, received, lost, loss_percent);

    if (received > 0) {
        double avg_rtt = (double)sum_rtt / received;
        printf("Approximate round trip times in milli-seconds:\n");
        printf("    Minimum = %dms, Maximum = %dms, Average = %.1fms\n",
               min_rtt, max_rtt, avg_rtt);
    }

    return 0;
}

