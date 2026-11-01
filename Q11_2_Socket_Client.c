/*
 * IT302 DCCN Lab - Question 11.2
 * Implementation of TCP Socket Client (Client - Server Model)
 * Connects to server on 127.0.0.1:8080, sends a message, and reads the reply.
 * Cross-platform: Compiles on both Windows (Winsock) and Linux (POSIX).
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef _WIN32
  #include <winsock2.h>
  #include <ws2tcpip.h>
  #pragma comment(lib, "ws2_32.lib")
  #define CLOSE_SOCK(s) closesocket(s)
#else
  #include <sys/socket.h>
  #include <netinet/in.h>
  #include <arpa/inet.h>
  #include <unistd.h>
  #define CLOSE_SOCK(s) close(s)
#endif

#define SERVER_IP "127.0.0.1"
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

    int sock_fd;
    struct sockaddr_in server_addr;
    char buffer[BUFFER_SIZE] = {0};
    char message[256];

    // 1. Create socket
    if ((sock_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Socket creation failed");
        return 1;
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = inet_addr(SERVER_IP);

    printf("Connecting to TCP Server at %s:%d...\n", SERVER_IP, PORT);

    // 2. Connect to server
    if (connect(sock_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection to server failed. Ensure server is running first!");
        CLOSE_SOCK(sock_fd);
        return 1;
    }

    printf("[+] Connected to server successfully!\n");

    // 3. Send message
    printf("Enter message to send to server: ");
    if (!fgets(message, sizeof(message), stdin)) return 1;
    message[strcspn(message, "\r\n")] = '\0';

    send(sock_fd, message, (int)strlen(message), 0);
    printf("[+] Message sent.\n");

    // 4. Receive reply
    int bytes_read = recv(sock_fd, buffer, sizeof(buffer) - 1, 0);
    if (bytes_read > 0) {
        buffer[bytes_read] = '\0';
        printf("[Server Response]: %s\n", buffer);
    }

    // 5. Cleanup
    CLOSE_SOCK(sock_fd);
#ifdef _WIN32
    WSACleanup();
#endif
    printf("[+] Socket closed.\n");
    return 0;
}

