/*
 * IT302 DCCN Lab - Question 12.1
 * HTTP Socket Client for Web Page Download (HTTP GET)
 * Connects to an HTTP server over Port 80, requests a page, and saves the response.
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

    char host[64] = "example.com";
    char path[128] = "/";
    int port = 80;

    printf("--- 12.1 HTTP Socket Web Page Download (GET) ---\n");
    printf("Target Host: %s, Port: %d, Path: %s\n", host, port, path);

    // 1. Resolve host
    struct hostent *server = gethostbyname(host);
    if (!server) {
        printf("Error: Could not resolve host %s\n", host);
        return 1;
    }

    // 2. Create Socket
    int sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd < 0) {
        perror("Socket failed");
        return 1;
    }

    struct sockaddr_in serv_addr;
    memset(&serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    memcpy(&serv_addr.sin_addr.s_addr, server->h_addr_list[0], server->h_length);
    serv_addr.sin_port = htons(port);

    // 3. Connect to HTTP server
    printf("Connecting to %s...\n", host);
    if (connect(sock_fd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        perror("Connection failed");
        CLOSE_SOCK(sock_fd);
        return 1;
    }
    printf("[+] Connected to HTTP server.\n");

    // 4. Construct and Send HTTP GET Request
    char request[512];
    snprintf(request, sizeof(request),
             "GET %s HTTP/1.1\r\n"
             "Host: %s\r\n"
             "User-Agent: C-Socket-HTTP-Client/1.0\r\n"
             "Connection: close\r\n\r\n",
             path, host);

    send(sock_fd, request, (int)strlen(request), 0);
    printf("[+] HTTP GET Request sent:\n%s\n", request);

    // 5. Receive HTTP Response and Save to File
    FILE *fp = fopen("downloaded_page.html", "wb");
    char buffer[BUFFER_SIZE];
    int total_bytes = 0, bytes_received;

    printf("[+] Receiving HTTP Response...\n");
    while ((bytes_received = recv(sock_fd, buffer, sizeof(buffer), 0)) > 0) {
        if (fp) fwrite(buffer, 1, bytes_received, fp);
        total_bytes += bytes_received;
        // Print preview to console
        fwrite(buffer, 1, bytes_received, stdout);
    }

    if (fp) {
        fclose(fp);
        printf("\n\n[+] Download Complete! Total bytes: %d\n", total_bytes);
        printf("[+] Saved web page to 'downloaded_page.html'.\n");
    }

    CLOSE_SOCK(sock_fd);
#ifdef _WIN32
    WSACleanup();
#endif
    return 0;
}

