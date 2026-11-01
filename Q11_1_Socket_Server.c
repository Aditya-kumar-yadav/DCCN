/*
 * IT302 DCCN Lab - Question 11.1
 * Implementation of TCP Socket Server (Client - Server Model)
 * Listens on port 8080, receives a message from the client, and sends a reply.
 * Cross-platform: Compiles on both Windows (Winsock) and Linux (POSIX).
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef _WIN32
  #include <winsock2.h>
  #include <ws2tcpip.h>
  #pragma comment(lib, "ws2_32.lib")
  typedef int socklen_t;
  #define CLOSE_SOCK(s) closesocket(s)
#else
  #include <sys/socket.h>
  #include <netinet/in.h>
  #include <arpa/inet.h>
  #include <unistd.h>
  #define CLOSE_SOCK(s) close(s)
#endif

#define PORT 8080
#define BUFFER_SIZE 1024

int main(void) {
#ifdef _WIN32
    WSADATA wsa;
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
        printf("WSAStartup failed.\n");
        return 1;
    }
#endif

    int server_fd, client_fd;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);
    char buffer[BUFFER_SIZE] = {0};

    // 1. Create socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Socket creation failed");
        return 1;
    }

    // 2. Bind to IP and Port
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        CLOSE_SOCK(server_fd);
        return 1;
    }

    // 3. Listen for incoming connections
    if (listen(server_fd, 3) < 0) {
        perror("Listen failed");
        CLOSE_SOCK(server_fd);
        return 1;
    }

    printf("========================================\n");
    printf("TCP Server listening on port %d...\n", PORT);
    printf("Waiting for client connection...\n");
    printf("========================================\n");

    // 4. Accept client connection
    client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &client_len);
    if (client_fd < 0) {
        perror("Accept failed");
        CLOSE_SOCK(server_fd);
        return 1;
    }

    printf("[+] Client connected from %s:%d\n", 
           inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));

    // 5. Receive message from client
    int bytes_read = recv(client_fd, buffer, sizeof(buffer) - 1, 0);
    if (bytes_read > 0) {
        buffer[bytes_read] = '\0';
        printf("[Client Message]: %s\n", buffer);
    }

    // 6. Send response to client
    const char *reply = "Hello from TCP Server! Message received successfully.";
    send(client_fd, reply, (int)strlen(reply), 0);
    printf("[+] Reply sent to client.\n");

    // 7. Cleanup
    CLOSE_SOCK(client_fd);
    CLOSE_SOCK(server_fd);
#ifdef _WIN32
    WSACleanup();
#endif
    printf("[+] Connection closed.\n");
    return 0;
}

