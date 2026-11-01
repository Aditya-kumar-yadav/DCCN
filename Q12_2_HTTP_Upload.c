/*
 * IT302 DCCN Lab - Question 12.2
 * HTTP Socket Client for Web Page / Data Upload (HTTP POST)
 * Connects to an HTTP server, uploads payload with Content-Length & Content-Type,
 * and prints the server's acknowledgment response.
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
  #include <netdb.h>
  #include <unistd.h>
  #define CLOSE_SOCK(s) close(s)
#endif

#define BUFFER_SIZE 4096

int main(void) {
#ifdef _WIN32
    WSADATA wsa;
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) return 1;
#endif

    const char *host = "httpbin.org";
    const char *path = "/post";
    int port = 80;

    // Payload to upload
    const char *payload = "title=DCCN+Lab+Assignment&author=Aryan&status=Submitted";
    int payload_len = (int)strlen(payload);

    printf("--- 12.2 HTTP Socket Web Page Data Upload (POST) ---\n");
    printf("Target Host: %s:%d, Path: %s\n", host, port, path);
    printf("Uploading Payload: \"%s\" (%d bytes)\n", payload, payload_len);

    // 1. Resolve host
    struct hostent *server = gethostbyname(host);
    if (!server) {
        printf("Error: Could not resolve host %s\n", host);
        return 1;
    }

    // 2. Create socket
    int sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd < 0) {
        perror("Socket creation failed");
        return 1;
    }

    struct sockaddr_in serv_addr;
    memset(&serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    memcpy(&serv_addr.sin_addr.s_addr, server->h_addr_list[0], server->h_length);
    serv_addr.sin_port = htons(port);

    // 3. Connect to server
    printf("Connecting to %s...\n", host);
    if (connect(sock_fd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        perror("Connection failed");
        CLOSE_SOCK(sock_fd);
        return 1;
    }
    printf("[+] Connected to server.\n");

    // 4. Construct HTTP POST request header and body
    char request[1024];
    snprintf(request, sizeof(request),
             "POST %s HTTP/1.1\r\n"
             "Host: %s\r\n"
             "User-Agent: C-Socket-HTTP-Upload/1.0\r\n"
             "Content-Type: application/x-www-form-urlencoded\r\n"
             "Content-Length: %d\r\n"
             "Connection: close\r\n\r\n"
             "%s",
             path, host, payload_len, payload);

    send(sock_fd, request, (int)strlen(request), 0);
    printf("[+] HTTP POST Upload Request Sent:\n%s\n", request);

    // 5. Receive Server Response
    char buffer[BUFFER_SIZE];
    int bytes_received;
    printf("[+] Server Response:\n----------------------------------------\n");
    while ((bytes_received = recv(sock_fd, buffer, sizeof(buffer) - 1, 0)) > 0) {
        buffer[bytes_received] = '\0';
        printf("%s", buffer);
    }
    printf("\n----------------------------------------\n");
    printf("[+] Upload and response reception completed successfully.\n");

    CLOSE_SOCK(sock_fd);
#ifdef _WIN32
    WSACleanup();
#endif
    return 0;
}

