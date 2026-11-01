# IT302 - Data Communication and Computer Networks (DCCN) Lab Assignment

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Portal-38bdf8?style=for-the-badge&logo=github&logoColor=white)](https://aditya-kumar-yadav.github.io/DCCN/)
[![Repo](https://img.shields.io/badge/GitHub-Repository-1e293b?style=for-the-badge&logo=github)](https://github.com/Aditya-kumar-yadav/DCCN)

🌐 **Live Deployed Web Portal**: **[https://aditya-kumar-yadav.github.io/DCCN/](https://aditya-kumar-yadav.github.io/DCCN/)**

> ⚡ **1-Click Copy All**: Open the web portal and click **⚡ ONE-CLICK COPY ALL (Q1–Q15)** to copy all 15 experiments, problem statements, and complete C solutions directly into your clipboard in 1 click! Individual question copy buttons (Q1 to Q15) are also provided.

This repository contains short, crisp C implementations for all practical coding problems and text documentation for all theoretical/empirical questions from the **IT302 DCCN Lab Assignment** (`IT302 DCCNLAB ASSIGNMENT.pdf`).

Click on any **Main Question Tag** below to directly view or open that question's file.

---

## 📋 Quick Navigation Index

| Ques No. | Main Question Tag (Click to Open) | Type | Direct File Link | Description |
|:---:|---|:---:|---|---|
| **Q1** | [Lab Network Topology, Interfaces, Routers, Switches & IP Pools](Q1_Lab_Network_Topology.txt) | Text | [`Q1_Lab_Network_Topology.txt`](Q1_Lab_Network_Topology.txt) | Network topology, physical/virtual interfaces, switch CAM tables, routers, RFC 1918 pools. |
| **Q2** | [Networking Commands (PING, TRACEROUTE), Telnet & Delay Measurement](Q2_Networking_Commands_and_Delays.txt) | Text | [`Q2_Networking_Commands_and_Delays.txt`](Q2_Networking_Commands_and_Delays.txt) | ICMP Echo, TTL expiration, Telnet (port 23) vs SSH, and nodal delay breakdown. |
| **Q3** | [Ping Tool Round-Trip Time & Success/Failure Statistics](Q3_Ping_Statistics.txt) | Text | [`Q3_Ping_Statistics.txt`](Q3_Ping_Statistics.txt) | Real measured ping latency, packet loss, and RTT for Google, Facebook, and BIT Mesra. |
| ↳ **3.1** | [Ping Statistics for google.com](Q3_1_Ping_Google.txt) | Text | [`Q3_1_Ping_Google.txt`](Q3_1_Ping_Google.txt) | 4 probes sent, 0% loss, Avg RTT = 38ms. |
| ↳ **3.2** | [Ping Statistics for facebook.com](Q3_2_Ping_Facebook.txt) | Text | [`Q3_2_Ping_Facebook.txt`](Q3_2_Ping_Facebook.txt) | 4 probes sent, 0% loss, Avg RTT = 58ms. |
| ↳ **3.3** | [Ping Statistics for bitmesra.ac.in](Q3_3_Ping_BitMesra.txt) | Text | [`Q3_3_Ping_BitMesra.txt`](Q3_3_Ping_BitMesra.txt) | 4 probes sent, 25% loss (firewall throttling), Avg RTT = 150ms. |
| **Q4** | [Trace Route Path Analysis for Web Destinations](Q4_Trace_Route.txt) | Text | [`Q4_Trace_Route.txt`](Q4_Trace_Route.txt) | Hop-by-hop router discovery and latency progression across local, campus, and WAN. |
| ↳ **4.1** | [Route Trace to google.com](Q4_1_Trace_Google.txt) | Text | [`Q4_1_Trace_Google.txt`](Q4_1_Trace_Google.txt) | 7 hops to Google AS15169 edge PoP. |
| ↳ **4.2** | [Route Trace to facebook.com](Q4_2_Trace_Facebook.txt) | Text | [`Q4_2_Trace_Facebook.txt`](Q4_2_Trace_Facebook.txt) | 9 active hops to Meta AS32934 infrastructure. |
| ↳ **4.3** | [Route Trace to bitmesra.ac.in](Q4_3_Trace_BitMesra.txt) | Text | [`Q4_3_Trace_BitMesra.txt`](Q4_3_Trace_BitMesra.txt) | 10 hops over international transit carriers (Arelion / Sucuri Anycast). |
| **Q5** | [IPv4 Class Determination (Class A, B, C, D, E)](Q5_IP_Class_Determination.c) | C Code | [`Q5_IP_Class_Determination.c`](Q5_IP_Class_Determination.c) | Determines IP class, subnet mask, NetID, and HostID. |
| **Q6** | [Translate Dotted Decimal IP to 32-bit Address](Q6_Dotted_Decimal_To_32Bit.c) | C Code | [`Q6_Dotted_Decimal_To_32Bit.c`](Q6_Dotted_Decimal_To_32Bit.c) | Converts dotted decimal IP to 32-bit binary, unsigned integer, and Hex format. |
| **Q7** | [Bit Stuffing and De-stuffing (HDLC Framing)](Q7_Bit_Stuffing_Destuffing.c) | C Code | [`Q7_Bit_Stuffing_Destuffing.c`](Q7_Bit_Stuffing_Destuffing.c) | Stuffs '0' after five consecutive 1s with `01111110` flag delimiter framing. |
| **Q8** | [Character Stuffing and De-stuffing (Byte Stuffing)](Q8_Character_Stuffing_Destuffing.c) | C Code | [`Q8_Character_Stuffing_Destuffing.c`](Q8_Character_Stuffing_Destuffing.c) | Frames message with `DLE STX` / `DLE ETX` and escapes internal `DLE` characters. |
| **Q9.1** | [Single Parity Checking Method](Q9_1_Single_Parity.c) | C Code | [`Q9_1_Single_Parity.c`](Q9_1_Single_Parity.c) | Error detection using even and odd single parity bits. |
| **Q9.2** | [Two-Dimensional Parity Checking Method](Q9_2_Two_Dimension_Parity.c) | C Code | [`Q9_2_Two_Dimension_Parity.c`](Q9_2_Two_Dimension_Parity.c) | 2D matrix parity (LRC & VRC) with single-bit error localization and correction. |
| **Q9.3** | [Cyclic Redundancy Check (CRC) Method](Q9_3_CRC.c) | C Code | [`Q9_3_CRC.c`](Q9_3_CRC.c) | Modulo-2 binary polynomial division (XOR) for CRC remainder and verification. |
| **Q9.4** | [Internet Checksum Method](Q9_4_Internet_Checksum.c) | C Code | [`Q9_4_Internet_Checksum.c`](Q9_4_Internet_Checksum.c) | 16-bit one's complement addition and verification as used in IPv4/TCP headers. |
| **Q10** | [Error Correction using Hamming Code Method](Q10_Hamming_Code.c) | C Code | [`Q10_Hamming_Code.c`](Q10_Hamming_Code.c) | Hamming (7, 4) code encoding, syndrome calculation, bit error detection & correction. |
| **Q11** | [Socket Programming & Client-Server Model Study](Q11_Socket_Programming_Model.txt) | Text | [`Q11_Socket_Programming_Model.txt`](Q11_Socket_Programming_Model.txt) | Architecture guide covering `socket()`, `bind()`, `listen()`, `accept()`, `connect()`. |
| ↳ **11.1** | [TCP Socket Server Implementation](Q11_1_Socket_Server.c) | C Code | [`Q11_1_Socket_Server.c`](Q11_1_Socket_Server.c) | Cross-platform TCP server listening on port 8080 and answering clients. |
| ↳ **11.2** | [TCP Socket Client Implementation](Q11_2_Socket_Client.c) | C Code | [`Q11_2_Socket_Client.c`](Q11_2_Socket_Client.c) | Cross-platform TCP client connecting to `127.0.0.1:8080` and sending messages. |
| **Q12.1** | [HTTP Socket Web Page Download (GET Request)](Q12_1_HTTP_Download.c) | C Code | [`Q12_1_HTTP_Download.c`](Q12_1_HTTP_Download.c) | HTTP client socket issuing `GET` request on port 80 and saving HTML page locally. |
| **Q12.2** | [HTTP Socket Web Page Data Upload (POST Request)](Q12_2_HTTP_Upload.c) | C Code | [`Q12_2_HTTP_Upload.c`](Q12_2_HTTP_Upload.c) | HTTP client socket sending `POST` request with `Content-Length` & payload data. |
| **Q13.1** | [Simulating PING Command](Q13_1_Ping_Simulation.c) | C Code | [`Q13_1_Ping_Simulation.c`](Q13_1_Ping_Simulation.c) | Simulates ICMP echo requests, latency variations, packet loss, and RTT stats. |
| **Q13.2** | [Simulating TRACEROUTE Command](Q13_2_Traceroute_Simulation.c) | C Code | [`Q13_2_Traceroute_Simulation.c`](Q13_2_Traceroute_Simulation.c) | Simulates hop-by-hop TTL decrement, 3 probe samples per hop, and route path display. |
| **Q14** | [Simulating DHCP Server](Q14_DHCP_Server_Simulation.c) | C Code | [`Q14_DHCP_Server_Simulation.c`](Q14_DHCP_Server_Simulation.c) | Simulates complete DORA workflow (Discover, Offer, Request, Ack) & IP pool management. |
| **Q15.1** | [Routing Table using Dijkstra's Algorithm](Q15_1_Dijkstra_Routing.c) | C Code | [`Q15_1_Dijkstra_Routing.c`](Q15_1_Dijkstra_Routing.c) | Link-State shortest path routing table generation (OSPF) with next-hop mapping. |
| **Q15.2** | [Routing Table using Distance Vector Algorithm](Q15_2_Distance_Vector_Routing.c) | C Code | [`Q15_2_Distance_Vector_Routing.c`](Q15_2_Distance_Vector_Routing.c) | Bellman-Ford iterative exchange and routing table convergence (RIP). |

---

## 🛠️ Compilation & Execution Guide

All C programs are self-contained and written in standard C99/C11. Socket programs (Q11 & Q12) feature cross-platform compatibility (`#ifdef _WIN32` for Windows Winsock and POSIX for Linux/macOS).

### On Linux / macOS (GCC / Clang):
```bash
# General algorithms (Q5, Q6, Q7, Q8, Q9.x, Q10, Q13.x, Q14, Q15.x)
gcc -Wall -O2 Q5_IP_Class_Determination.c -o Q5
gcc -Wall -O2 Q7_Bit_Stuffing_Destuffing.c -o Q7
gcc -Wall -O2 Q10_Hamming_Code.c -o Q10
gcc -Wall -O2 Q14_DHCP_Server_Simulation.c -o Q14
gcc -Wall -O2 Q15_1_Dijkstra_Routing.c -o Q15_1

# TCP Client-Server (Q11)
gcc -Wall -O2 Q11_1_Socket_Server.c -o Q11_server
gcc -Wall -O2 Q11_2_Socket_Client.c -o Q11_client

# Run server in one terminal: ./Q11_server
# Run client in another terminal: ./Q11_client

# HTTP Web Sockets (Q12)
gcc -Wall -O2 Q12_1_HTTP_Download.c -o Q12_1
gcc -Wall -O2 Q12_2_HTTP_Upload.c -o Q12_2
```

### On Windows (MinGW GCC):
```cmd
# General programs
gcc -Wall -O2 Q5_IP_Class_Determination.c -o Q5.exe
gcc -Wall -O2 Q7_Bit_Stuffing_Destuffing.c -o Q7.exe

# Sockets (must link with ws2_32)
gcc -Wall -O2 Q11_1_Socket_Server.c -o Q11_server.exe -lws2_32
gcc -Wall -O2 Q11_2_Socket_Client.c -o Q11_client.exe -lws2_32
gcc -Wall -O2 Q12_1_HTTP_Download.c -o Q12_1.exe -lws2_32
gcc -Wall -O2 Q12_2_HTTP_Upload.c -o Q12_2.exe -lws2_32
```
