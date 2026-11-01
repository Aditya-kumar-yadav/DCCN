/*
 * IT302 DCCN Lab - Question 15.1
 * Routing Table Implementation using Dijkstra's Shortest Path Algorithm
 * (Link State Routing Protocol - e.g. OSPF)
 */

#include <stdio.h>

#define MAX_NODES 10
#define INF 9999

int main(void) {
    int n, src;
    int cost[MAX_NODES][MAX_NODES];
    int dist[MAX_NODES];
    int visited[MAX_NODES] = {0};
    int next_hop[MAX_NODES];

    printf("--- 15.1 Dijkstra's Link-State Routing Table ---\n");
    printf("Enter number of routers/nodes (max %d): ", MAX_NODES);
    if (scanf("%d", &n) != 1 || n <= 0 || n > MAX_NODES) return 1;

    printf("Enter adjacency cost matrix (%d x %d, enter %d for no direct link):\n", n, n, INF);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &cost[i][j]);
            if (i == j) cost[i][j] = 0;
        }
    }

    printf("Enter source router ID (0 to %d): ", n - 1);
    if (scanf("%d", &src) != 1 || src < 0 || src >= n) return 1;

    // Initialization
    for (int i = 0; i < n; i++) {
        dist[i] = cost[src][i];
        if (cost[src][i] != INF && i != src) {
            next_hop[i] = i; // Direct neighbor is initial next hop
        } else {
            next_hop[i] = -1;
        }
    }
    visited[src] = 1;
    dist[src] = 0;
    next_hop[src] = src;

    // Dijkstra's Algorithm
    for (int count = 1; count < n; count++) {
        int min_dist = INF, u = -1;

        // Pick unvisited node with minimum distance
        for (int i = 0; i < n; i++) {
            if (!visited[i] && dist[i] < min_dist) {
                min_dist = dist[i];
                u = i;
            }
        }

        if (u == -1 || min_dist == INF) break;
        visited[u] = 1;

        // Relax neighbors of u
        for (int v = 0; v < n; v++) {
            if (!visited[v] && cost[u][v] != INF && (dist[u] + cost[u][v] < dist[v])) {
                dist[v] = dist[u] + cost[u][v];
                next_hop[v] = next_hop[u]; // Next hop remains the same as that to reach u
            }
        }
    }

    // Display Routing Table for Source Router
    printf("\n============================================\n");
    printf("      ROUTING TABLE FOR ROUTER %d (OSPF)    \n", src);
    printf("============================================\n");
    printf(" Destination | Total Cost | Next Hop Router \n");
    printf("--------------------------------------------\n");
    for (int i = 0; i < n; i++) {
        if (dist[i] == INF) {
            printf("      %2d     |  UNREACH   |        --       \n", i);
        } else {
            printf("      %2d     |    %4d    |        %2d       \n", i, dist[i], next_hop[i]);
        }
    }
    printf("============================================\n");

    return 0;
}

