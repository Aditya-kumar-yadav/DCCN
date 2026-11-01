# IT302 - Data Communication and Computer Networks (DCCN) Lab Assignment

This repository contains short, crisp C implementations for all practical coding problems and detailed text documentation for all theoretical/experimental questions as specified in `IT302 DCCNLAB ASSIGNMENT.pdf`.

---

## Index of Files & Mapping to Questions

| Ques No. | Main Tag / Topic | Type | Filename(s) | Description |
|---|---|---|---|---|
| **Q1** | Lab Network Topology & IP Pools | Text | [`Q1_Lab_Network_Topology.txt`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q1_Lab_Network_Topology.txt) | Detailed study of star/tree topology, interfaces (NIC, lo), switches, routers, and IP pools (RFC 1918). |
| **Q2** | Networking Commands & Delay | Text | [`Q2_Networking_Commands_and_Delays.txt`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q2_Networking_Commands_and_Delays.txt) | PING, TRACEROUTE, Telnet remote login, nodal delay components, and latency analysis. |
| **Q3** | Ping Statistics & RTT | Text | [`Q3_Ping_Statistics.txt`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q3_Ping_Statistics.txt)<br>• [`Q3_1_Ping_Google.txt`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q3_1_Ping_Google.txt)<br>• [`Q3_2_Ping_Facebook.txt`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q3_2_Ping_Facebook.txt)<br>• [`Q3_3_Ping_BitMesra.txt`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q3_3_Ping_BitMesra.txt) | Real measured ping success/loss statistics and round-trip times for google.com, facebook.com, and bitmesra.ac.in. |
| **Q4** | Route Tracing | Text | [`Q4_Trace_Route.txt`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q4_Trace_Route.txt)<br>• [`Q4_1_Trace_Google.txt`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q4_1_Trace_Google.txt)<br>• [`Q4_2_Trace_Facebook.txt`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q4_2_Trace_Facebook.txt)<br>• [`Q4_3_Trace_BitMesra.txt`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q4_3_Trace_BitMesra.txt) | Hop-by-hop traceroute paths to google.com, facebook.com, and bitmesra.ac.in. |
| **Q5** | IPv4 Class Determination | C Code | [`Q5_IP_Class_Determination.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q5_IP_Class_Determination.c) | Determines whether an IP is Class A, B, C, D, or E, extracting NetID and HostID. |
| **Q6** | Dotted Decimal to 32-bit Address | C Code | [`Q6_Dotted_Decimal_To_32Bit.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q6_Dotted_Decimal_To_32Bit.c) | Translates dotted decimal IP into 32-bit binary string, 32-bit unsigned integer, and Hex format. |
| **Q7** | Bit Stuffing and De-stuffing | C Code | [`Q7_Bit_Stuffing_Destuffing.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q7_Bit_Stuffing_Destuffing.c) | Stuffs '0' after five consecutive '1's, wraps with `01111110` flag, and reconstructs original data. |
| **Q8** | Character Stuffing & De-stuffing | C Code | [`Q8_Character_Stuffing_Destuffing.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q8_Character_Stuffing_Destuffing.c) | Frames message between `DLE STX` and `DLE ETX`, escaping internal `DLE` tokens. |
| **Q9.1** | Error Detection: Single Parity | C Code | [`Q9_1_Single_Parity.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q9_1_Single_Parity.c) | Even and Odd parity generator and receiver verification. |
| **Q9.2** | Error Detection: 2D Parity | C Code | [`Q9_2_Two_Dimension_Parity.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q9_2_Two_Dimension_Parity.c) | Longitudinal Redundancy Check (LRC) & VRC matrix with error localization & correction. |
| **Q9.3** | Error Detection: CRC | C Code | [`Q9_3_CRC.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q9_3_CRC.c) | Cyclic Redundancy Check using polynomial modulo-2 binary division (XOR). |
| **Q9.4** | Error Detection: Internet Checksum | C Code | [`Q9_4_Internet_Checksum.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q9_4_Internet_Checksum.c) | 16-bit one's complement addition and verification as used in IPv4/TCP headers. |
| **Q10** | Error Correction: Hamming Code | C Code | [`Q10_Hamming_Code.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q10_Hamming_Code.c) | Hamming (7,4) code generator, syndrome calculation, bit error detection & correction. |
| **Q11** | Socket Programming & Client-Server | Text & C | • [`Q11_Socket_Programming_Model.txt`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q11_Socket_Programming_Model.txt)<br>• [`Q11_1_Socket_Server.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q11_1_Socket_Server.c)<br>• [`Q11_2_Socket_Client.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q11_2_Socket_Client.c) | Study of socket architecture and cross-platform TCP server/client implementation. |
| **Q12** | HTTP Sockets: Upload & Download | C Code | • [`Q12_1_HTTP_Download.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q12_1_HTTP_Download.c)<br>• [`Q12_2_HTTP_Upload.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q12_2_HTTP_Upload.c) | HTTP client downloading webpage via GET and uploading payload via POST socket request. |
| **Q13** | Simulation: PING & TRACEROUTE | C Code | • [`Q13_1_Ping_Simulation.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q13_1_Ping_Simulation.c)<br>• [`Q13_2_Traceroute_Simulation.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q13_2_Traceroute_Simulation.c) | Simulates ICMP echo latency, packet loss, TTL hop decrement, and route discovery. |
| **Q14** | DHCP Server Simulation | C Code | [`Q14_DHCP_Server_Simulation.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q14_DHCP_Server_Simulation.c) | Simulates DHCP DORA 4-way handshake, IP pool leasing, and client release. |
| **Q15.1** | Routing: Dijkstra's Algorithm | C Code | [`Q15_1_Dijkstra_Routing.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q15_1_Dijkstra_Routing.c) | Link-state shortest path routing table generation (OSPF). |
| **Q15.2** | Routing: Distance Vector Algorithm | C Code | [`Q15_2_Distance_Vector_Routing.c`](file:///c:/Users/AryanSachin/Desktop/DCCN/Q15_2_Distance_Vector_Routing.c) | Bellman-Ford iterative routing table convergence (RIP). |

---

## Compilation Instructions

All C code files are self-contained and support standard C (C99 / C11).
They can be compiled with GCC, Clang, or MSVC:

### Linux / macOS:
```bash
gcc -Wall -O2 Q5_IP_Class_Determination.c -o Q5
gcc -Wall -O2 Q11_1_Socket_Server.c -o Q11_server
gcc -Wall -O2 Q11_2_Socket_Client.c -o Q11_client
```

### Windows (MinGW GCC):
```cmd
gcc -Wall -O2 Q5_IP_Class_Determination.c -o Q5.exe
gcc -Wall -O2 Q11_1_Socket_Server.c -o Q11_server.exe -lws2_32
gcc -Wall -O2 Q11_2_Socket_Client.c -o Q11_client.exe -lws2_32
```

