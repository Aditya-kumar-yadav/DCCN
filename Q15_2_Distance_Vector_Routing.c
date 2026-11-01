/*
 * IT302 DCCN Lab - Question 15.2
 * Routing Table Implementation using Distance Vector Routing Algorithm
 * Based on the Bellman-Ford Equation: D_x(y) = min_v { c(x, v) + D_v(y) }
 * (RIP - Routing Information Protocol)
 */

#include <stdio.h>

#define MAX_NODES 10
#define INF 9999

struct RouteEntry {
    int dist[MAX_NODES];
    int next_hop[MAX_NODES];
} routing_table[MAX_NODES];

int main(void) {
    int n;
    int cost[MAX_NODES][MAX_NODES];

    printf("--- 15.2 Distance Vector Routing (Bellman-Ford) ---\n");
    printf("Enter number of routers/nodes (max %d): ", MAX_NODES);
    if (scanf("%d", &n) != 1 || n <= 0 || n > MAX_NODES) return 1;

    printf("Enter link cost matrix (%d x %d, enter %d for no direct link):\n", n, n, INF);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &cost[i][j]);
            if (i == j) cost[i][j] = 0;
            // Initial distance vector is the direct link cost
            routing_table[i].dist[j] = cost[i][j];
            routing_table[i].next_hop[j] = (cost[i][j] != INF && i != j) ? j : i;
        }
    }

    // Iterative Distance Vector exchange until convergence
    int updated;
    int iteration = 0;
    do {
        updated = 0;
        iteration++;
        for (int i = 0; i < n; i++) {           // For each router i
            for (int j = 0; j < n; j++) {       // For each destination j
                for (int k = 0; k < n; k++) {   // Check path via neighbor k
                    if (cost[i][k] != INF && routing_table[k].dist[j] != INF) {
                        int new_dist = cost[i][k] + routing_table[k].dist[j];
                        if (new_dist < routing_table[i].dist[j]) {
                            routing_table[i].dist[j] = new_dist;
                            routing_table[i].next_hop[j] = k;
                            updated = 1;
                        }
                    }
                }
            }
        }
    } while (updated);

    printf("\nRouting tables converged in %d iteration(s).\n", iteration);

    // Display Converged Routing Tables for each router
    for (int i = 0; i < n; i++) {
        printf("\n============================================\n");
        printf("      CONVERGED ROUTING TABLE: ROUTER %d    \n", i);
        printf("============================================\n");
        printf(" Destination | Total Cost | Next Hop Router \n");
        printf("--------------------------------------------\n");
        for (int j = 0; j < n; j++) {
            if (routing_table[i].dist[j] == INF) {
                printf("      %2d     |  UNREACH   |        --       \n", j);
            } else {
                printf("      %2d     |    %4d    |        %2d       \n",
                       j, routing_table[i].dist[j], routing_table[i].next_hop[j]);
            }
        }
        printf("============================================\n");
    }

    return 0;
}

