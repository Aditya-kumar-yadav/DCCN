import os
import html
import json

SECTIONS = [
    {
        "id": "q1",
        "num": "1",
        "tag": "Q1: Lab Network Topology, Interfaces, Routers & IP Pools",
        "clean_title": "Lab Network Topology, Interfaces, Routers & IP Pools",
        "badge": "Theory / Study",
        "unit": "Unit 1: Network Topology & Commands",
        "category": "theory",
        "summary": "Study of Lab Network Topology (Star/Mesh/Bus), Ethernet/Wireless/Loopback interfaces, Switch CAM tables, Routers, and RFC 1918 Private IP Address pools (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16).",
        "question": "1. To familiarize with the Lab Network Topology, Locating different interfaces, routers and switches. Studying different pools of IP addresses.",
        "files": [
            {"name": "Q1_Lab_Network_Topology.txt", "type": "txt", "title": "Network Topology & IP Pools Report"}
        ]
    },
    {
        "id": "q2",
        "num": "2",
        "tag": "Q2: Networking Commands (PING, TRACEROUTE), Telnet & Delay",
        "clean_title": "Networking Commands (PING, TRACEROUTE), Telnet & Delay",
        "badge": "Theory / Experimental",
        "unit": "Unit 1: Network Topology & Commands",
        "category": "theory",
        "summary": "Practical examination of PING (ICMP Type 8 Echo Request / Type 0 Reply), TRACEROUTE (TTL expiry, ICMP Type 11), Telnet (Port 23 cleartext) vs SSH (Port 22 encrypted), and 4 components of nodal delay: Processing, Queuing, Transmission, and Propagation delay.",
        "question": "2. To learn and observe the usage of different networking commands e.g. PING, TRACEROUTE. Learning remote login using telnet session. Measuring typical average delays between different locations of the network.",
        "files": [
            {"name": "Q2_Networking_Commands_and_Delays.txt", "type": "txt", "title": "Networking Commands & Delay Analysis"}
        ]
    },
    {
        "id": "q3",
        "num": "3",
        "tag": "Q3: Ping Tool Statistics & Round-Trip Times",
        "clean_title": "Ping Tool Statistics & Round-Trip Times",
        "badge": "Measurements",
        "unit": "Unit 1: Network Topology & Commands",
        "category": "theory",
        "summary": "Empirical measurement of round trip time (RTT) and packet loss for google.com (Avg RTT ~38ms, 0% loss), facebook.com (Avg RTT ~58ms, 0% loss), and bitmesra.ac.in (Avg RTT ~150ms, 25% loss due to ICMP rate limiting).",
        "question": "3. \"Ping\" is a tool used to determine if a server is responding and to estimate the round trip time of a message sent to that server. Use the ping command for the following URLs and record the success or failure statistics along with the average round trip time:\n a) google.com   b) facebook.com   c) bitmesra.ac.in",
        "files": [
            {"name": "Q3_Ping_Statistics.txt", "type": "txt", "title": "Consolidated Ping Statistics & Comparison"},
            {"name": "Q3_1_Ping_Google.txt", "type": "txt", "title": "3.1 Ping google.com"},
            {"name": "Q3_2_Ping_Facebook.txt", "type": "txt", "title": "3.2 Ping facebook.com"},
            {"name": "Q3_3_Ping_BitMesra.txt", "type": "txt", "title": "3.3 Ping bitmesra.ac.in"}
        ]
    },
    {
        "id": "q4",
        "num": "4",
        "tag": "Q4: Trace Route Path Analysis",
        "clean_title": "Trace Route Path Analysis",
        "badge": "Measurements",
        "unit": "Unit 1: Network Topology & Commands",
        "category": "theory",
        "summary": "Traceroute hop-by-hop path discovery and latency progression across local gateway, ISP backbone, and autonomous system (AS) borders to Google (AS15169, 7 hops), Facebook (AS32934, 9 hops), and BIT Mesra (Arelion/Sucuri, 10 hops).",
        "question": "4. Trace the route that is taken when you try to access:\n a) google.com   b) facebook.com   c) bitmesra.ac.in",
        "files": [
            {"name": "Q4_Trace_Route.txt", "type": "txt", "title": "Consolidated Traceroute Path Analysis"},
            {"name": "Q4_1_Trace_Google.txt", "type": "txt", "title": "4.1 Trace Route google.com"},
            {"name": "Q4_2_Trace_Facebook.txt", "type": "txt", "title": "4.2 Trace Route facebook.com"},
            {"name": "Q4_3_Trace_BitMesra.txt", "type": "txt", "title": "4.3 Trace Route bitmesra.ac.in"}
        ]
    },
    {
        "id": "q5",
        "num": "5",
        "tag": "Q5: IPv4 Class Determination",
        "clean_title": "IPv4 Class Determination",
        "badge": "C Code",
        "unit": "Unit 2: IP Addressing & Conversion",
        "category": "code",
        "summary": "Classifies IPv4 address by first octet: Class A (0-127, mask 255.0.0.0), Class B (128-191, mask 255.255.0.0), Class C (192-223, mask 255.255.255.0), Class D (224-239, Multicast), Class E (240-255, Experimental). Extracts NetID & HostID.",
        "compile": "gcc Q5_IP_Class_Determination.c -o Q5",
        "question": "5. Write a C/C++ program to determine if the IP address is in Class A, B, C, D, or E.",
        "files": [
            {"name": "Q5_IP_Class_Determination.c", "type": "c", "title": "IPv4 Class Identifier"}
        ]
    },
    {
        "id": "q6",
        "num": "6",
        "tag": "Q6: Dotted Decimal to 32-bit Address Translation",
        "clean_title": "Dotted Decimal to 32-bit Address Translation",
        "badge": "C Code",
        "unit": "Unit 2: IP Addressing & Conversion",
        "category": "code",
        "summary": "Converts dotted decimal IPv4 string (A.B.C.D) into a single 32-bit integer: (A<<24) | (B<<16) | (C<<8) | D. Prints full 32-bit binary representation, decimal integer, and Hexadecimal.",
        "compile": "gcc Q6_Dotted_Decimal_To_32Bit.c -o Q6",
        "question": "6. Write a C/C++ program to translate dotted decimal IP address into 32 bit address.",
        "files": [
            {"name": "Q6_Dotted_Decimal_To_32Bit.c", "type": "c", "title": "Dotted Decimal to 32-Bit Binary & Hex"}
        ]
    },
    {
        "id": "q7",
        "num": "7",
        "tag": "Q7: Bit Stuffing and De-stuffing",
        "clean_title": "Bit Stuffing and De-stuffing",
        "badge": "C Code",
        "unit": "Unit 3: Data Link Layer Framing",
        "category": "code",
        "summary": "HDLC Bit Framing: Sender scans data stream; whenever five consecutive '1's appear, a '0' is stuffed to prevent false flag pattern (01111110 / 0x7E). Receiver destuffs by removing '0' after five '1's.",
        "compile": "gcc Q7_Bit_Stuffing_Destuffing.c -o Q7",
        "question": "7. Write a C/C++ program to perform bit stuffing and de-stuffing.",
        "files": [
            {"name": "Q7_Bit_Stuffing_Destuffing.c", "type": "c", "title": "HDLC Bit Stuffing & Framing"}
        ]
    },
    {
        "id": "q8",
        "num": "8",
        "tag": "Q8: Character Stuffing and De-stuffing",
        "clean_title": "Character Stuffing and De-stuffing",
        "badge": "C Code",
        "unit": "Unit 3: Data Link Layer Framing",
        "category": "code",
        "summary": "Byte-Oriented Framing: Frames data with DLE STX (Start of Text) and DLE ETX (End of Text). If DLE character appears inside user payload, sender stuffs an additional DLE (DLE DLE). Receiver strips the stuffed DLE.",
        "compile": "gcc Q8_Character_Stuffing_Destuffing.c -o Q8",
        "question": "8. Write a C/C++ program to perform character stuffing and de-stuffing.",
        "files": [
            {"name": "Q8_Character_Stuffing_Destuffing.c", "type": "c", "title": "Byte Stuffing (DLE STX / DLE ETX)"}
        ]
    },
    {
        "id": "q9",
        "num": "9",
        "tag": "Q9: Error Detection Methods",
        "clean_title": "Error Detection Methods",
        "badge": "C Code (4 Methods)",
        "unit": "Unit 4: Error Detection & Correction",
        "category": "code",
        "summary": "4 Error Detection Algorithms: 1) Single Parity (Even/Odd bit), 2) 2D Parity Matrix (LRC & VRC - detects and locates 1-bit error), 3) Cyclic Redundancy Check CRC (Modulo-2 polynomial division with XOR), 4) Internet Checksum RFC 1071 (16-bit 1's complement sum).",
        "compile": "gcc Q9_1_Single_Parity.c -o Q9_1\ngcc Q9_2_Two_Dimension_Parity.c -o Q9_2\ngcc Q9_3_CRC.c -o Q9_3\ngcc Q9_4_Internet_Checksum.c -o Q9_4",
        "question": "9. Write a C/C++ program to perform error detection method using:\n - Single parity checking method\n - Two dimension parity checking method\n - Cyclic redundancy check (CRC) method\n - Internet checksum method",
        "files": [
            {"name": "Q9_1_Single_Parity.c", "type": "c", "title": "9.1 Single Parity Check (Even / Odd)"},
            {"name": "Q9_2_Two_Dimension_Parity.c", "type": "c", "title": "9.2 Two-Dimensional Parity Check (LRC & VRC)"},
            {"name": "Q9_3_CRC.c", "type": "c", "title": "9.3 Cyclic Redundancy Check (Modulo-2 XOR)"},
            {"name": "Q9_4_Internet_Checksum.c", "type": "c", "title": "9.4 Internet Checksum (RFC 1071)"}
        ]
    },
    {
        "id": "q10",
        "num": "10",
        "tag": "Q10: Error Correction using Hamming Code",
        "clean_title": "Error Correction using Hamming Code",
        "badge": "C Code",
        "unit": "Unit 4: Error Detection & Correction",
        "category": "code",
        "summary": "Hamming (7, 4) Code: 4 data bits (D7, D6, D5, D3) encoded with 3 parity bits (P1, P2, P4) at bit positions that are powers of 2. At receiver, syndrome bits S = s3 s2 s1 identify the exact corrupted bit position (1-7), flipping it back to correct the error.",
        "compile": "gcc Q10_Hamming_Code.c -o Q10",
        "question": "10. Write a C/C++ program to perform error correction using Hamming code method.",
        "files": [
            {"name": "Q10_Hamming_Code.c", "type": "c", "title": "Hamming (7, 4) Code Encoding & Correction"}
        ]
    },
    {
        "id": "q11",
        "num": "11",
        "tag": "Q11: Socket Programming & Client-Server Model",
        "clean_title": "Socket Programming & Client-Server Model",
        "badge": "Study & C Code",
        "unit": "Unit 5: Socket Programming & HTTP",
        "category": "code",
        "summary": "TCP Socket Programming Model: Server lifecycle: socket() -> bind() -> listen() -> accept() -> recv()/send() -> close(). Client lifecycle: socket() -> connect() -> send()/recv() -> close(). Cross-platform implementation (Winsock on Windows, POSIX on Linux).",
        "compile": "Linux:   gcc Q11_1_Socket_Server.c -o server && gcc Q11_2_Socket_Client.c -o client\nWindows: gcc Q11_1_Socket_Server.c -o server.exe -lws2_32 && gcc Q11_2_Socket_Client.c -o client.exe -lws2_32",
        "question": "11. Study and implement model for Socket Programming and Client - Server model.",
        "files": [
            {"name": "Q11_Socket_Programming_Model.txt", "type": "txt", "title": "Socket Programming Lifecycle & Theory"},
            {"name": "Q11_1_Socket_Server.c", "type": "c", "title": "11.1 TCP Socket Server (Cross-platform)"},
            {"name": "Q11_2_Socket_Client.c", "type": "c", "title": "11.2 TCP Socket Client (Cross-platform)"}
        ]
    },
    {
        "id": "q12",
        "num": "12",
        "tag": "Q12: HTTP Sockets: Web Page Upload & Download",
        "clean_title": "HTTP Sockets: Web Page Upload & Download",
        "badge": "C Code (2 Parts)",
        "unit": "Unit 5: Socket Programming & HTTP",
        "category": "code",
        "summary": "Raw HTTP Client Socket implementation over TCP port 80. 1) HTTP Download: constructs GET / HTTP/1.1 request, reads response headers and body, writes HTML to disk. 2) HTTP Upload: constructs POST / HTTP/1.1 with Content-Length & Content-Type, sends payload data.",
        "compile": "Linux:   gcc Q12_1_HTTP_Download.c -o Q12_1 && gcc Q12_2_HTTP_Upload.c -o Q12_2\nWindows: gcc Q12_1_HTTP_Download.c -o Q12_1.exe -lws2_32 && gcc Q12_2_HTTP_Upload.c -o Q12_2.exe -lws2_32",
        "question": "12. Create a socket for HTTP for web page upload and download.",
        "files": [
            {"name": "Q12_1_HTTP_Download.c", "type": "c", "title": "12.1 HTTP GET Web Page Downloader"},
            {"name": "Q12_2_HTTP_Upload.c", "type": "c", "title": "12.2 HTTP POST Web Page / Data Uploader"}
        ]
    },
    {
        "id": "q13",
        "num": "13",
        "tag": "Q13: Simulation of PING & TRACEROUTE Commands",
        "clean_title": "Simulation of PING & TRACEROUTE Commands",
        "badge": "C Code (2 Parts)",
        "unit": "Unit 6: Protocol Simulations",
        "category": "code",
        "summary": "1) PING Simulator: Sends simulated ICMP Echo Requests with sequence numbers, computes random realistic RTTs, simulates packet drop rate, prints min/avg/max/mdev stats. 2) TRACEROUTE Simulator: Increments TTL from 1 upwards, queries 3 probes per hop, displays IP hops and latencies until destination reached.",
        "compile": "gcc Q13_1_Ping_Simulation.c -o Q13_1\ngcc Q13_2_Traceroute_Simulation.c -o Q13_2",
        "question": "13. Write a code simulating PING and TRACEROUTE commands.",
        "files": [
            {"name": "Q13_1_Ping_Simulation.c", "type": "c", "title": "13.1 PING Command Simulator"},
            {"name": "Q13_2_Traceroute_Simulation.c", "type": "c", "title": "13.2 TRACEROUTE Command Simulator"}
        ]
    },
    {
        "id": "q14",
        "num": "14",
        "tag": "Q14: DHCP Server Simulation (DORA)",
        "clean_title": "DHCP Server Simulation (DORA)",
        "badge": "C Code",
        "unit": "Unit 6: Protocol Simulations",
        "category": "code",
        "summary": "Full DHCP Server Simulation implementing DORA exchange: 1) DHCPDISCOVER (client broadcast), 2) DHCPOFFER (server reserves IP from pool), 3) DHCPREQUEST (client requests offered IP), 4) DHCPACK (server binds MAC, assigns subnet mask, gateway, DNS, and lease time). Includes IP pool allocation and release.",
        "compile": "gcc Q14_DHCP_Server_Simulation.c -o Q14",
        "question": "14. Write a code simulating DHCP server.",
        "files": [
            {"name": "Q14_DHCP_Server_Simulation.c", "type": "c", "title": "DHCP Server Simulation (Discover, Offer, Request, Ack)"}
        ]
    },
    {
        "id": "q15",
        "num": "15",
        "tag": "Q15: Routing Table Implementation",
        "clean_title": "Routing Table Implementation",
        "badge": "C Code (2 Algorithms)",
        "unit": "Unit 7: Routing Algorithms",
        "category": "code",
        "summary": "1) Dijkstra's Algorithm: Link-State shortest path tree (OSPF) from source router using greedy distance relaxation, generates complete routing table with Next-Hop router. 2) Distance Vector Routing: Distributed Bellman-Ford algorithm (RIP) exchanging cost vectors with neighbors iteratively until convergence: D_x(y) = min_v { c(x,v) + D_v(y) }.",
        "compile": "gcc Q15_1_Dijkstra_Routing.c -o Q15_1\ngcc Q15_2_Distance_Vector_Routing.c -o Q15_2",
        "question": "15. Implement the routing table using:\n a) Dijkstra's algorithm.\n b) Distance vector Routing algorithm.",
        "files": [
            {"name": "Q15_1_Dijkstra_Routing.c", "type": "c", "title": "15.1 Dijkstra's Shortest Path Routing (OSPF)"},
            {"name": "Q15_2_Distance_Vector_Routing.c", "type": "c", "title": "15.2 Distance Vector Routing (Bellman-Ford / RIP)"}
        ]
    }
]

def read_file_content(path):
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def build_all_solutions_plain_text():
    divider_heavy = "=" * 80
    divider_light = "-" * 80
    lines = []
    lines.append(divider_heavy)
    lines.append("IT302 - DATA COMMUNICATION AND COMPUTER NETWORKS (DCCN) LAB")
    lines.append("COMPLETE ASSIGNMENT EXPERIMENTS & SOLUTIONS MANUAL (Q1 TO Q15)")
    lines.append(divider_heavy)
    lines.append("Repository : https://github.com/Aryan9891/DCCN-Lab-repo")
    lines.append("Live Portal: https://aryan9891.github.io/DCCN-Lab-repo/")
    lines.append("One-Click Copy: Available on both index.html and quiz.html")
    lines.append(divider_heavy)
    lines.append("")
    lines.append("TABLE OF CONTENTS / INDEX:")
    for s in SECTIONS:
        lines.append(f"  [Q{s['num']}] {s['clean_title']} ({s['badge']})")
    lines.append("")
    lines.append(divider_heavy)
    lines.append("")

    for s in SECTIONS:
        lines.append(divider_heavy)
        lines.append(f"QUESTION {s['num']}: {s['clean_title']}")
        lines.append(f"Unit: {s['unit']} | Category: {s['badge']}")
        lines.append(divider_heavy)
        lines.append("PROBLEM STATEMENT:")
        lines.append(s['question'])
        lines.append("")
        if "summary" in s:
            lines.append("CONCEPT / ALGORITHM SUMMARY:")
            lines.append(s["summary"])
            lines.append("")
        if "compile" in s:
            lines.append("COMPILATION INSTRUCTIONS:")
            lines.append(s["compile"])
            lines.append("")

        for idx, f in enumerate(s["files"], 1):
            fname = f["name"]
            ftitle = f["title"]
            fcontent = read_file_content(fname)
            lines.append(divider_light)
            lines.append(f"--- File {idx}/{len(s['files'])}: {fname} ({ftitle}) ---")
            lines.append(divider_light)
            lines.append(fcontent.strip())
            lines.append("")
        lines.append("")

    return "\n".join(lines)

def build_question_plain_text(s):
    divider_heavy = "=" * 80
    divider_light = "-" * 80
    lines = []
    lines.append(divider_heavy)
    lines.append(f"QUESTION {s['num']}: {s['clean_title']}")
    lines.append(f"Unit: {s['unit']} | Category: {s['badge']}")
    lines.append(divider_heavy)
    lines.append("PROBLEM STATEMENT:")
    lines.append(s['question'])
    lines.append("")
    if "summary" in s:
        lines.append("CONCEPT / SUMMARY:")
        lines.append(s["summary"])
        lines.append("")
    if "compile" in s:
        lines.append("COMPILATION COMMAND:")
        lines.append(s["compile"])
        lines.append("")

    for idx, f in enumerate(s["files"], 1):
        fname = f["name"]
        ftitle = f["title"]
        fcontent = read_file_content(fname)
        lines.append(divider_light)
        lines.append(f"--- File: {fname} ({ftitle}) ---")
        lines.append(divider_light)
        lines.append(fcontent.strip())
        lines.append("")

    return "\n".join(lines)

def generate_index_html(all_text, question_texts):
    current_unit = ""
    sidebar_items_html = ""
    sections_html = ""
    quick_copy_ribbon_html = ""

    # Build Quick Copy ribbon pills
    for s in SECTIONS:
        quick_copy_ribbon_html += f'''
        <div class="ribbon-chip" title="Click icon to copy, title to jump">
            <a href="#{s["id"]}" class="chip-link">Q{s["num"]}</a>
            <button class="chip-copy-btn" onclick="copyQuestion('{s["id"]}', event)" title="One-click copy Question {s["num"]} & code">📋</button>
        </div>
        '''

    for s in SECTIONS:
        if s["unit"] != current_unit:
            current_unit = s["unit"]
            sidebar_items_html += f'<div class="unit-header">{html.escape(current_unit)}</div>\n'
        
        sidebar_items_html += f'''
        <a href="#{s["id"]}" class="nav-item" onclick="highlightNav(this)">
            <span class="nav-tag">Q{s["num"]}</span>
            <span class="nav-title">{html.escape(s["clean_title"])}</span>
        </a>
        '''

        files_tabs_html = ""
        files_content_html = ""

        for idx, f in enumerate(s["files"]):
            fname = f["name"]
            ftitle = f["title"]
            ftype = f["type"]
            fcontent = read_file_content(fname)
            escaped_code = html.escape(fcontent)
            is_active = "active" if idx == 0 else ""
            tab_id = f"{s['id']}_tab_{idx}"
            content_id = f"{s['id']}_content_{idx}"

            lang_class = "language-c" if ftype == "c" else "language-none"

            files_tabs_html += f'''
            <button class="tab-btn {is_active}" onclick="switchTab('{s["id"]}', {idx})">
                {html.escape(ftitle)}
            </button>
            '''

            files_content_html += f'''
            <div id="{content_id}" class="tab-content {is_active}">
                <div class="code-header">
                    <span class="file-name">📄 <a href="{fname}" target="_blank">{html.escape(fname)}</a></span>
                    <div class="code-actions">
                        <button class="copy-btn" onclick="copyToClipboard('{content_id}_code', '{html.escape(fname)}')">📋 Copy Code Only</button>
                        <a href="{fname}" download class="download-btn">⬇ Download</a>
                    </div>
                </div>
                <pre class="code-block"><code id="{content_id}_code" class="{lang_class}">{escaped_code}</code></pre>
            </div>
            '''

        escaped_q = html.escape(s["question"]).replace("\n", "<br>")
        compile_html = ""
        if "compile" in s:
            compile_html = f'''
            <div class="compile-badge-box">
                <span class="compile-label">🛠️ GCC:</span>
                <code>{html.escape(s["compile"]).replace(chr(10), "<br>")}</code>
            </div>
            '''

        summary_html = ""
        if "summary" in s:
            summary_html = f'''
            <div class="concept-box">
                <strong>💡 Quick Concept / Key Note:</strong>
                <p>{html.escape(s["summary"])}</p>
            </div>
            '''

        sections_html += f'''
        <section id="{s["id"]}" class="question-card" data-category="{s.get("category", "code")}">
            <div class="card-header">
                <div class="card-title-group">
                    <span class="badge badge-{s["files"][0]["type"]}">{html.escape(s["badge"])}</span>
                    <h2 class="card-title">Q{s["num"]}: {html.escape(s["clean_title"])}</h2>
                </div>
                <div class="card-header-actions">
                    <button class="btn-copy-card" onclick="copyQuestion('{s["id"]}')" title="Copy Problem Statement + All Solution Code">
                        📋 Copy Question & Solution
                    </button>
                    <a href="#{s["id"]}" class="anchor-link" title="Direct link to this experiment">🔗</a>
                </div>
            </div>

            <div class="problem-box">
                <strong>Problem Statement:</strong>
                <p>{escaped_q}</p>
            </div>

            {summary_html}
            {compile_html}

            <div class="tabs-container">
                <div class="tab-buttons-bar">
                    {files_tabs_html}
                </div>
                {files_content_html}
            </div>
        </section>
        '''

    all_solutions_json = json.dumps(all_text).replace("</script>", "<\\/script>")
    question_texts_json = json.dumps(question_texts).replace("</script>", "<\\/script>")

    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IT302 DCCN Lab Assignment Solutions | 1-Click Copy All for Quiz</title>
    <meta name="description" content="One-click copy all DCCN lab experiments and complete C solutions for IT302 quiz preparation.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
    <style>
        :root {{
            --bg-color: #0b1120;
            --surface-color: #1e293b;
            --surface-card: #141e33;
            --surface-hover: #334155;
            --border-color: #334155;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent-blue: #38bdf8;
            --accent-cyan: #06b6d4;
            --accent-green: #4ade80;
            --accent-purple: #c084fc;
            --accent-amber: #fbbf24;
            --accent-rose: #f43f5e;
            --code-bg: #070d18;
            --sidebar-width: 320px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            line-height: 1.6;
            display: flex;
            min-height: 100vh;
        }}

        /* Sidebar Styling */
        #sidebar {{
            width: var(--sidebar-width);
            height: 100vh;
            background-color: var(--surface-color);
            border-right: 1px solid var(--border-color);
            position: fixed;
            top: 0;
            left: 0;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            z-index: 100;
        }}

        .sidebar-header {{
            padding: 18px 20px;
            border-bottom: 1px solid var(--border-color);
            background: linear-gradient(180deg, rgba(30,41,59,1) 0%, rgba(15,23,42,0.95) 100%);
        }}

        .sidebar-title {{
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--accent-blue);
            margin-bottom: 2px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .sidebar-subtitle {{
            font-size: 0.78rem;
            color: var(--text-secondary);
        }}

        .sidebar-quick-copy {{
            padding: 12px 16px;
            background: rgba(56, 189, 248, 0.05);
            border-bottom: 1px solid var(--border-color);
        }}

        .btn-sidebar-copy {{
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 10px 14px;
            background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
            color: #ffffff;
            border: 1px solid #38bdf8;
            border-radius: 8px;
            font-size: 0.85rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
            box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
        }}

        .btn-sidebar-copy:hover {{
            background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%);
            transform: translateY(-1px);
        }}

        .search-box {{
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
        }}

        .search-input {{
            width: 100%;
            padding: 9px 12px;
            background-color: var(--bg-color);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            color: var(--text-primary);
            font-size: 0.85rem;
            outline: none;
            transition: border-color 0.2s;
        }}

        .search-input:focus {{
            border-color: var(--accent-blue);
            box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
        }}

        .nav-list {{
            flex: 1;
            padding: 10px 0 30px;
        }}

        .unit-header {{
            padding: 14px 16px 6px;
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-weight: 700;
            color: var(--accent-amber);
        }}

        .nav-item {{
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 8px 16px;
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 0.82rem;
            transition: all 0.15s ease;
            border-left: 3px solid transparent;
        }}

        .nav-item:hover, .nav-item.active {{
            background-color: var(--surface-hover);
            color: var(--text-primary);
            border-left-color: var(--accent-blue);
        }}

        .nav-tag {{
            font-family: 'Fira Code', monospace;
            font-weight: 700;
            font-size: 0.72rem;
            color: var(--accent-blue);
            background: rgba(56, 189, 248, 0.12);
            padding: 2px 6px;
            border-radius: 4px;
            white-space: nowrap;
        }}

        .nav-title {{
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        /* Main Content Styling */
        #main {{
            margin-left: var(--sidebar-width);
            flex: 1;
            padding: 24px 40px 60px;
            max-width: 1250px;
        }}

        /* QUIZ STICKY MEGA BAR */
        .quiz-mega-banner {{
            position: sticky;
            top: 16px;
            z-index: 90;
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border: 2px solid #0284c7;
            border-radius: 12px;
            padding: 16px 20px;
            margin-bottom: 24px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4), 0 0 20px rgba(56, 189, 248, 0.15);
            backdrop-filter: blur(10px);
        }}

        .quiz-banner-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 12px;
        }}

        .quiz-banner-info {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .quiz-pulse-dot {{
            width: 10px;
            height: 10px;
            background-color: var(--accent-green);
            border-radius: 50%;
            display: inline-block;
            box-shadow: 0 0 10px var(--accent-green);
            animation: pulse 1.5s infinite;
        }}

        @keyframes pulse {{
            0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7); }}
            70% {{ transform: scale(1.1); box-shadow: 0 0 0 8px rgba(74, 222, 128, 0); }}
            100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); }}
        }}

        .quiz-banner-heading {{
            font-size: 1.05rem;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: 0.02em;
        }}

        .quiz-banner-sub {{
            font-size: 0.8rem;
            color: var(--accent-cyan);
            font-weight: 500;
        }}

        .quiz-banner-actions {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .btn-mega-copy {{
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: #ffffff;
            border: 1px solid #34d399;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 0.95rem;
            font-weight: 800;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
            box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35);
        }}

        .btn-mega-copy:hover {{
            background: linear-gradient(135deg, #34d399 0%, #10b981 100%);
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(16, 185, 129, 0.45);
        }}

        .btn-banner-action {{
            background-color: rgba(30, 41, 59, 0.9);
            color: var(--text-primary);
            border: 1px solid var(--border-color);
            padding: 8px 14px;
            border-radius: 6px;
            font-size: 0.82rem;
            font-weight: 600;
            text-decoration: none;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.15s;
        }}

        .btn-banner-action:hover {{
            background-color: var(--surface-hover);
            border-color: var(--accent-blue);
            color: var(--accent-blue);
        }}

        .quick-ribbon-bar {{
            display: flex;
            align-items: center;
            gap: 6px;
            overflow-x: auto;
            padding-top: 6px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
        }}

        .ribbon-label {{
            font-size: 0.75rem;
            text-transform: uppercase;
            font-weight: 700;
            color: var(--accent-amber);
            white-space: nowrap;
            margin-right: 4px;
        }}

        .ribbon-chip {{
            display: inline-flex;
            align-items: center;
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            overflow: hidden;
            font-size: 0.78rem;
            transition: border-color 0.15s;
        }}

        .ribbon-chip:hover {{
            border-color: var(--accent-blue);
        }}

        .chip-link {{
            color: #cbd5e1;
            text-decoration: none;
            padding: 4px 8px;
            font-weight: 600;
            font-family: 'Fira Code', monospace;
        }}

        .chip-link:hover {{
            color: var(--accent-blue);
            background: rgba(56, 189, 248, 0.1);
        }}

        .chip-copy-btn {{
            background: rgba(56, 189, 248, 0.15);
            border: none;
            border-left: 1px solid var(--border-color);
            color: var(--accent-blue);
            padding: 4px 6px;
            cursor: pointer;
            font-size: 0.75rem;
            transition: background 0.15s;
        }}

        .chip-copy-btn:hover {{
            background: var(--accent-blue);
            color: #0f172a;
        }}

        /* Hero Banner */
        .hero-banner {{
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 28px 32px;
            margin-bottom: 30px;
            position: relative;
            overflow: hidden;
        }}

        .hero-title {{
            font-size: 1.75rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 8px;
        }}

        .hero-desc {{
            color: var(--text-secondary);
            font-size: 0.95rem;
            max-width: 850px;
            margin-bottom: 20px;
        }}

        .hero-buttons {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s;
            cursor: pointer;
            border: 1px solid transparent;
        }}

        .btn-primary {{
            background-color: var(--accent-blue);
            color: #0f172a;
        }}

        .btn-primary:hover {{
            background-color: #7dd3fc;
            box-shadow: 0 4px 12px rgba(56, 189, 248, 0.3);
        }}

        .btn-secondary {{
            background-color: var(--surface-color);
            border-color: var(--border-color);
            color: var(--text-primary);
        }}

        .btn-secondary:hover {{
            background-color: var(--surface-hover);
        }}

        /* Question Cards */
        .question-card {{
            background-color: var(--surface-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 32px;
            scroll-margin-top: 100px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
            transition: border-color 0.2s;
        }}

        .question-card:hover {{
            border-color: #475569;
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 16px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 14px;
            gap: 14px;
            flex-wrap: wrap;
        }}

        .card-title-group {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .card-title {{
            font-size: 1.25rem;
            font-weight: 700;
            color: #ffffff;
        }}

        .card-header-actions {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .btn-copy-card {{
            background: rgba(56, 189, 248, 0.12);
            color: var(--accent-blue);
            border: 1px solid rgba(56, 189, 248, 0.3);
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.15s;
        }}

        .btn-copy-card:hover {{
            background: var(--accent-blue);
            color: #0f172a;
        }}

        .anchor-link {{
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 1.1rem;
            opacity: 0.6;
            transition: opacity 0.2s;
        }}

        .anchor-link:hover {{
            opacity: 1;
            color: var(--accent-blue);
        }}

        .badge {{
            font-size: 0.72rem;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 9999px;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }}

        .badge-c {{
            background: rgba(74, 222, 128, 0.15);
            color: var(--accent-green);
            border: 1px solid rgba(74, 222, 128, 0.3);
        }}

        .badge-txt {{
            background: rgba(192, 132, 252, 0.15);
            color: var(--accent-purple);
            border: 1px solid rgba(192, 132, 252, 0.3);
        }}

        .problem-box {{
            background-color: rgba(15, 23, 42, 0.6);
            border-left: 4px solid var(--accent-blue);
            padding: 12px 16px;
            border-radius: 4px;
            margin-bottom: 14px;
            font-size: 0.92rem;
            color: #cbd5e1;
        }}

        .problem-box strong {{
            color: var(--accent-blue);
            font-size: 0.82rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            display: block;
            margin-bottom: 4px;
        }}

        .concept-box {{
            background-color: rgba(251, 191, 36, 0.08);
            border-left: 4px solid var(--accent-amber);
            padding: 10px 14px;
            border-radius: 4px;
            margin-bottom: 14px;
            font-size: 0.88rem;
            color: #fde68a;
        }}

        .concept-box strong {{
            color: var(--accent-amber);
            font-size: 0.8rem;
            display: block;
            margin-bottom: 3px;
        }}

        .compile-badge-box {{
            display: flex;
            align-items: center;
            gap: 8px;
            background: rgba(0, 0, 0, 0.4);
            border: 1px dashed var(--border-color);
            padding: 6px 12px;
            border-radius: 6px;
            margin-bottom: 16px;
            font-size: 0.8rem;
            color: #94a3b8;
            font-family: 'Fira Code', monospace;
        }}

        .compile-label {{
            color: var(--accent-green);
            font-weight: 700;
        }}

        /* Tabs Styling */
        .tabs-container {{
            margin-top: 14px;
        }}

        .tab-buttons-bar {{
            display: flex;
            gap: 6px;
            overflow-x: auto;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 12px;
            padding-bottom: 2px;
        }}

        .tab-btn {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            padding: 8px 14px;
            font-size: 0.85rem;
            font-weight: 500;
            cursor: pointer;
            border-radius: 6px 6px 0 0;
            border-bottom: 2px solid transparent;
            transition: all 0.2s;
            white-space: nowrap;
        }}

        .tab-btn:hover {{
            color: var(--text-primary);
            background-color: rgba(255, 255, 255, 0.03);
        }}

        .tab-btn.active {{
            color: var(--accent-blue);
            border-bottom-color: var(--accent-blue);
            font-weight: 600;
            background-color: rgba(56, 189, 248, 0.08);
        }}

        .tab-content {{
            display: none;
        }}

        .tab-content.active {{
            display: block;
        }}

        .code-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #080d1a;
            padding: 8px 14px;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            border: 1px solid var(--border-color);
            border-bottom: none;
            font-size: 0.8rem;
        }}

        .file-name a {{
            color: var(--accent-blue);
            text-decoration: none;
            font-family: 'Fira Code', monospace;
        }}

        .file-name a:hover {{
            text-decoration: underline;
        }}

        .code-actions {{
            display: flex;
            gap: 8px;
        }}

        .copy-btn, .download-btn {{
            background-color: var(--surface-hover);
            color: var(--text-primary);
            border: 1px solid var(--border-color);
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.75rem;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.15s;
        }}

        .copy-btn:hover, .download-btn:hover {{
            background-color: var(--accent-blue);
            color: #0f172a;
        }}

        .code-block {{
            background-color: var(--code-bg) !important;
            border: 1px solid var(--border-color);
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
            padding: 16px !important;
            margin: 0 !important;
            max-height: 480px;
            overflow-y: auto;
            font-family: 'Fira Code', monospace !important;
            font-size: 0.85rem !important;
        }}

        /* Raw Text Modal */
        .modal-backdrop {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(4px);
            z-index: 1000;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}

        .modal-backdrop.open {{
            display: flex;
        }}

        .modal-box {{
            background: var(--surface-color);
            border: 2px solid var(--accent-blue);
            border-radius: 12px;
            width: 100%;
            max-width: 900px;
            height: 85vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
        }}

        .modal-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 14px 20px;
            background: #0f172a;
            border-bottom: 1px solid var(--border-color);
        }}

        .modal-header h3 {{
            font-size: 1.1rem;
            color: #ffffff;
        }}

        .modal-actions {{
            display: flex;
            gap: 10px;
            align-items: center;
        }}

        .modal-close {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            font-size: 1.3rem;
            cursor: pointer;
            padding: 2px 8px;
        }}

        .modal-close:hover {{
            color: #ffffff;
        }}

        .modal-textarea {{
            flex: 1;
            background: var(--code-bg);
            color: #e2e8f0;
            font-family: 'Fira Code', monospace;
            font-size: 0.85rem;
            padding: 16px;
            border: none;
            resize: none;
            outline: none;
            white-space: pre;
            overflow: auto;
        }}

        /* Toast Feedback */
        #toast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: #ffffff;
            padding: 12px 20px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 0.9rem;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 999;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        #toast.show {{
            transform: translateY(0);
            opacity: 1;
        }}

        /* Floating Quick Action Button */
        .floating-copy-btn {{
            position: fixed;
            bottom: 24px;
            left: 344px;
            background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
            color: #ffffff;
            border: 1px solid #38bdf8;
            padding: 10px 18px;
            border-radius: 9999px;
            font-weight: 700;
            font-size: 0.85rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            z-index: 85;
            transition: all 0.2s;
        }}

        .floating-copy-btn:hover {{
            transform: translateY(-2px);
            background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%);
        }}

        /* Responsive */
        @media (max-width: 900px) {{
            #sidebar {{
                display: none;
            }}
            #main {{
                margin-left: 0;
                padding: 16px;
            }}
            .floating-copy-btn {{
                left: 16px;
            }}
        }}
    </style>
</head>
<body>

    <!-- Left Sidebar -->
    <nav id="sidebar">
        <div class="sidebar-header">
            <div class="sidebar-title">⚡ IT302 DCCN LAB</div>
            <div class="sidebar-subtitle">Assignments & Source Codes</div>
        </div>
        <div class="sidebar-quick-copy">
            <button class="btn-sidebar-copy" onclick="copyAllSolutions()">
                📋 Copy All (Q1–Q15)
            </button>
        </div>
        <div class="search-box">
            <input type="text" id="search-input" class="search-input" placeholder="Search questions, CRC, IP, Dijkstra..." onkeyup="filterQuestions()">
        </div>
        <div class="nav-list" id="nav-list">
            {sidebar_items_html}
        </div>
    </nav>

    <!-- Main Content Area -->
    <main id="main">

        <!-- QUIZ STICKY MEGA BAR (Always accessible at top) -->
        <div class="quiz-mega-banner">
            <div class="quiz-banner-top">
                <div class="quiz-banner-info">
                    <span class="quiz-pulse-dot"></span>
                    <div>
                        <div class="quiz-banner-heading">DCCN LAB QUIZ ASSISTANT</div>
                        <div class="quiz-banner-sub">15 Experiments • Complete C Codes • Quick Copies Ready</div>
                    </div>
                </div>
                <div class="quiz-banner-actions">
                    <button class="btn-mega-copy" id="btn-mega-copy-main" onclick="copyAllSolutions()">
                        ⚡ ONE-CLICK COPY ALL (Q1–Q15)
                    </button>
                    <a href="quiz.html" class="btn-banner-action" title="Open lightweight exam view">
                        🎯 Quiz Mode
                    </a>
                    <a href="all_solutions.txt" download class="btn-banner-action" title="Download plain text file">
                        📥 Download .txt
                    </a>
                    <button class="btn-banner-action" onclick="openRawModal()" title="View and select raw text directly">
                        👁️ View Raw
                    </button>
                </div>
            </div>

            <!-- Quick copy ribbon for Q1 to Q15 -->
            <div class="quick-ribbon-bar">
                <span class="ribbon-label">Quick Copy:</span>
                {quick_copy_ribbon_html}
            </div>
        </div>

        <header class="hero-banner">
            <h1 class="hero-title">IT302 — Data Communication & Computer Networks</h1>
            <p class="hero-desc">
                Interactive laboratory portal containing complete C source code implementations, 
                measured network statistics (PING, Traceroute), and study reports.
                Everything is pre-compiled and ready for instant one-click copy during your lab quiz.
            </p>
            <div class="hero-buttons">
                <button class="btn btn-primary" onclick="copyAllSolutions()">
                    ⚡ Copy All Experiments & Solutions
                </button>
                <a href="quiz.html" class="btn btn-secondary">
                    🎯 Dedicated Quiz Mode
                </a>
                <a href="all_solutions.txt" download class="btn btn-secondary">
                    📄 all_solutions.txt
                </a>
                <a href="https://github.com/Aryan9891/DCCN-Lab-repo" target="_blank" class="btn btn-secondary">
                    ⭐ GitHub Repo
                </a>
            </div>
        </header>

        <div id="questions-container">
            {sections_html}
        </div>
    </main>

    <!-- Floating Quick Copy Button -->
    <button class="floating-copy-btn" onclick="copyAllSolutions()" title="One-click copy all 15 experiments">
        ⚡ Copy All (Q1–Q15)
    </button>

    <!-- Raw Text Modal (Foolproof fallback) -->
    <div id="raw-modal" class="modal-backdrop" onclick="closeModalOnBackdrop(event)">
        <div class="modal-box">
            <div class="modal-header">
                <h3>📄 All Experiments & Solutions (Plain Text)</h3>
                <div class="modal-actions">
                    <button class="btn btn-primary" onclick="copyModalText()">📋 Copy All Text</button>
                    <button class="btn btn-secondary" onclick="selectModalText()">Select All</button>
                    <button class="modal-close" onclick="closeRawModal()">✕</button>
                </div>
            </div>
            <textarea id="raw-textarea" class="modal-textarea" readonly></textarea>
        </div>
    </div>

    <!-- Toast Notification -->
    <div id="toast">✅ Copied to clipboard!</div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-c.min.js"></script>
    <script>
        const ALL_SOLUTIONS_TEXT = {all_solutions_json};
        const EXPERIMENT_TEXTS = {question_texts_json};

        function switchTab(sectionId, tabIndex) {{
            const card = document.getElementById(sectionId);
            const buttons = card.querySelectorAll('.tab-btn');
            const contents = card.querySelectorAll('.tab-content');

            buttons.forEach((btn, idx) => {{
                btn.classList.toggle('active', idx === tabIndex);
            }});

            contents.forEach((cnt, idx) => {{
                cnt.classList.toggle('active', idx === tabIndex);
            }});
        }}

        function copyText(text, successMsg) {{
            if (navigator.clipboard && window.isSecureContext) {{
                navigator.clipboard.writeText(text).then(() => {{
                    showToast(successMsg || "Copied to clipboard!");
                }}).catch(() => {{
                    fallbackCopy(text, successMsg);
                }});
            }} else {{
                fallbackCopy(text, successMsg);
            }}
        }}

        function fallbackCopy(text, successMsg) {{
            const ta = document.createElement("textarea");
            ta.value = text;
            ta.style.position = "fixed";
            ta.style.left = "-9999px";
            ta.style.top = "0";
            document.body.appendChild(ta);
            ta.focus();
            ta.select();
            try {{
                const ok = document.execCommand('copy');
                if (ok) {{
                    showToast(successMsg || "Copied to clipboard!");
                }} else {{
                    openRawModal();
                    showToast("Please press Ctrl+C to copy from the opened box");
                }}
            }} catch (err) {{
                openRawModal();
                showToast("Please press Ctrl+C to copy from the opened box");
            }}
            document.body.removeChild(ta);
        }}

        function copyAllSolutions() {{
            copyText(ALL_SOLUTIONS_TEXT, "✅ ALL 15 Experiments & Solutions Copied!");
            const btn = document.getElementById("btn-mega-copy-main");
            if (btn) {{
                const originalText = btn.innerHTML;
                btn.innerHTML = "✅ COPIED TO CLIPBOARD!";
                btn.style.background = "#059669";
                setTimeout(() => {{
                    btn.innerHTML = originalText;
                    btn.style.background = "";
                }}, 2000);
            }}
        }}

        function copyQuestion(qid, event) {{
            if (event) event.stopPropagation();
            if (EXPERIMENT_TEXTS[qid]) {{
                copyText(EXPERIMENT_TEXTS[qid], "✅ Copied " + qid.toUpperCase() + " Question & Solution!");
            }}
        }}

        function copyToClipboard(elementId, fname) {{
            const codeEl = document.getElementById(elementId);
            if (!codeEl) return;
            const text = codeEl.innerText;
            const name = fname ? fname : 'code';
            copyText(text, "✅ Copied " + name + " to clipboard!");
        }}

        function showToast(msg) {{
            const toast = document.getElementById('toast');
            toast.innerText = msg;
            toast.classList.add('show');
            setTimeout(() => {{
                toast.classList.remove('show');
            }}, 2400);
        }}

        function openRawModal() {{
            const modal = document.getElementById('raw-modal');
            const textarea = document.getElementById('raw-textarea');
            textarea.value = ALL_SOLUTIONS_TEXT;
            modal.classList.add('open');
            setTimeout(() => textarea.select(), 50);
        }}

        function closeRawModal() {{
            document.getElementById('raw-modal').classList.remove('open');
        }}

        function closeModalOnBackdrop(e) {{
            if (e.target.id === 'raw-modal') closeRawModal();
        }}

        function selectModalText() {{
            const textarea = document.getElementById('raw-textarea');
            textarea.focus();
            textarea.select();
            showToast("Text selected - press Ctrl+C to copy");
        }}

        function copyModalText() {{
            const textarea = document.getElementById('raw-textarea');
            copyText(textarea.value, "✅ All text copied from modal!");
        }}

        function filterQuestions() {{
            const query = document.getElementById('search-input').value.toLowerCase();
            const navItems = document.querySelectorAll('.nav-item');
            const cards = document.querySelectorAll('.question-card');

            navItems.forEach(item => {{
                const text = item.innerText.toLowerCase();
                item.style.display = text.includes(query) ? 'flex' : 'none';
            }});

            cards.forEach(card => {{
                const text = card.innerText.toLowerCase();
                card.style.display = text.includes(query) ? 'block' : 'none';
            }});
        }}

        function highlightNav(el) {{
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            el.classList.add('active');
        }}

        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') closeRawModal();
        }});
    </script>
</body>
</html>
'''
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(full_html)
    print("index.html generated successfully!")

def generate_quiz_html(all_text, question_texts):
    cards_html = ""
    for s in SECTIONS:
        fcontent_primary = read_file_content(s["files"][0]["name"])
        escaped_code = html.escape(fcontent_primary)
        ftype = s["files"][0]["type"]
        lang_class = "language-c" if ftype == "c" else "language-none"

        files_menu = ""
        for idx, f in enumerate(s["files"]):
            fcode = read_file_content(f["name"])
            files_menu += f'''
            <button class="file-chip" onclick="showQuizCode('{s["id"]}', {idx}, '{html.escape(f["name"])}')">
                {html.escape(f["title"])}
            </button>
            '''

        compile_row = ""
        if "compile" in s:
            compile_row = f'''
            <div class="q-compile">
                <code>{html.escape(s["compile"]).replace(chr(10), "<br>")}</code>
            </div>
            '''

        cards_html += f'''
        <div class="quiz-card" id="card_{s["id"]}" data-num="{s["num"]}" data-category="{s.get("category", "code")}">
            <div class="quiz-card-header">
                <div class="quiz-card-title-line">
                    <span class="quiz-num">Q{s["num"]}</span>
                    <h3 class="quiz-title">{html.escape(s["clean_title"])}</h3>
                    <span class="quiz-badge badge-{ftype}">{html.escape(s["badge"])}</span>
                </div>
                <div class="quiz-card-actions">
                    <button class="btn-action-primary" onclick="copyQuestion('{s["id"]}')">
                        📋 Copy Q + Solution
                    </button>
                    <button class="btn-action-code" onclick="copyQuizActiveCode('{s["id"]}')">
                        📋 Copy Code Only
                    </button>
                </div>
            </div>

            <div class="quiz-prompt">
                <strong>Problem:</strong> {html.escape(s["question"])}
            </div>

            <div class="quiz-summary">
                <strong>⚡ Key Concept:</strong> {html.escape(s["summary"])}
            </div>

            {compile_row}

            <div class="quiz-files-bar">
                {files_menu}
            </div>

            <div class="quiz-code-box">
                <div class="quiz-code-header">
                    <span id="{s["id"]}_active_fname" class="active-file-label">📄 {html.escape(s["files"][0]["name"])}</span>
                    <button class="copy-small" onclick="copyQuizActiveCode('{s["id"]}')">📋 Copy</button>
                </div>
                <pre class="quiz-code"><code id="{s["id"]}_code_view" class="{lang_class}">{escaped_code}</code></pre>
            </div>
        </div>
        '''

    all_solutions_json = json.dumps(all_text).replace("</script>", "<\\/script>")
    question_texts_json = json.dumps(question_texts).replace("</script>", "<\\/script>")

    quiz_files_data = {}
    for s in SECTIONS:
        quiz_files_data[s["id"]] = [
            {"name": f["name"], "title": f["title"], "code": read_file_content(f["name"])}
            for f in s["files"]
        ]
    quiz_files_json = json.dumps(quiz_files_data).replace("</script>", "<\\/script>")

    quiz_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>⚡ DCCN Lab Quiz Cheat Sheet & Instant Copy Portal</title>
    <meta name="description" content="Ultra-fast, distraction-free cheat sheet and 1-click copy portal for DCCN Lab Exam.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
    <style>
        :root {{
            --bg: #090d16;
            --card-bg: #111827;
            --border: #26334d;
            --text: #f1f5f9;
            --muted: #94a3b8;
            --accent: #38bdf8;
            --green: #10b981;
            --amber: #f59e0b;
            --code-bg: #060911;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            line-height: 1.5;
            padding: 16px;
        }}

        .quiz-container {{
            max-width: 1100px;
            margin: 0 auto;
        }}

        /* Header Sticky Bar */
        .quiz-top-bar {{
            position: sticky;
            top: 10px;
            z-index: 100;
            background: rgba(17, 24, 39, 0.95);
            border: 2px solid #0284c7;
            border-radius: 12px;
            padding: 14px 20px;
            backdrop-filter: blur(10px);
            margin-bottom: 20px;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6);
        }}

        .top-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 12px;
        }}

        .top-brand {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .pulse-light {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: var(--green);
            box-shadow: 0 0 10px var(--green);
        }}

        .brand-title {{
            font-size: 1.1rem;
            font-weight: 800;
            color: #ffffff;
        }}

        .brand-subtitle {{
            font-size: 0.78rem;
            color: var(--accent);
        }}

        .top-buttons {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}

        .btn-copy-all {{
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: #ffffff;
            border: 1px solid #34d399;
            padding: 9px 18px;
            border-radius: 8px;
            font-size: 0.92rem;
            font-weight: 800;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);
        }}

        .btn-copy-all:hover {{
            background: linear-gradient(135deg, #34d399 0%, #10b981 100%);
            transform: translateY(-1px);
        }}

        .btn-portal-link {{
            background: rgba(38, 51, 77, 0.7);
            color: #e2e8f0;
            border: 1px solid var(--border);
            padding: 8px 14px;
            border-radius: 6px;
            font-size: 0.82rem;
            font-weight: 600;
            text-decoration: none;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}

        .btn-portal-link:hover {{
            background: var(--accent);
            color: #090d16;
        }}

        .filter-row {{
            display: flex;
            gap: 10px;
            align-items: center;
            flex-wrap: wrap;
        }}

        .search-field {{
            flex: 1;
            min-width: 220px;
            padding: 8px 14px;
            background: var(--bg);
            border: 1px solid var(--border);
            border-radius: 6px;
            color: #ffffff;
            font-size: 0.85rem;
            outline: none;
        }}

        .search-field:focus {{
            border-color: var(--accent);
        }}

        .filter-tags {{
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }}

        .tag-btn {{
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid var(--border);
            color: var(--muted);
            padding: 5px 10px;
            border-radius: 6px;
            font-size: 0.78rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.15s;
        }}

        .tag-btn:hover, .tag-btn.active {{
            background: var(--accent);
            color: #090d16;
            border-color: var(--accent);
        }}

        /* Cards */
        .quiz-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 24px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        }}

        .quiz-card-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 12px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 12px;
        }}

        .quiz-card-title-line {{
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .quiz-num {{
            font-family: 'Fira Code', monospace;
            background: #0284c7;
            color: #ffffff;
            font-weight: 800;
            font-size: 0.85rem;
            padding: 3px 8px;
            border-radius: 6px;
        }}

        .quiz-title {{
            font-size: 1.15rem;
            font-weight: 700;
            color: #ffffff;
        }}

        .quiz-badge {{
            font-size: 0.72rem;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 9999px;
            text-transform: uppercase;
        }}

        .badge-c {{
            background: rgba(16, 185, 129, 0.15);
            color: var(--green);
            border: 1px solid rgba(16, 185, 129, 0.3);
        }}

        .badge-txt {{
            background: rgba(192, 132, 252, 0.15);
            color: #c084fc;
            border: 1px solid rgba(192, 132, 252, 0.3);
        }}

        .quiz-card-actions {{
            display: flex;
            gap: 8px;
        }}

        .btn-action-primary {{
            background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
            color: #ffffff;
            border: 1px solid #38bdf8;
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s;
        }}

        .btn-action-primary:hover {{
            background: var(--accent);
            color: #090d16;
        }}

        .btn-action-code {{
            background: rgba(16, 185, 129, 0.15);
            color: var(--green);
            border: 1px solid rgba(16, 185, 129, 0.3);
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s;
        }}

        .btn-action-code:hover {{
            background: var(--green);
            color: #090d16;
        }}

        .quiz-prompt {{
            background: rgba(15, 23, 42, 0.7);
            border-left: 3px solid var(--accent);
            padding: 10px 14px;
            border-radius: 4px;
            font-size: 0.88rem;
            color: #cbd5e1;
            margin-bottom: 10px;
        }}

        .quiz-summary {{
            background: rgba(245, 158, 11, 0.08);
            border-left: 3px solid var(--amber);
            padding: 8px 12px;
            border-radius: 4px;
            font-size: 0.85rem;
            color: #fde68a;
            margin-bottom: 10px;
        }}

        .q-compile {{
            background: #000000;
            border: 1px dashed var(--border);
            padding: 6px 12px;
            border-radius: 4px;
            font-family: 'Fira Code', monospace;
            font-size: 0.78rem;
            color: var(--green);
            margin-bottom: 12px;
        }}

        .quiz-files-bar {{
            display: flex;
            gap: 6px;
            margin-bottom: 10px;
            flex-wrap: wrap;
        }}

        .file-chip {{
            background: rgba(38, 51, 77, 0.6);
            border: 1px solid var(--border);
            color: #cbd5e1;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.76rem;
            font-family: 'Fira Code', monospace;
            cursor: pointer;
            transition: all 0.15s;
        }}

        .file-chip:hover {{
            background: var(--accent);
            color: #090d16;
        }}

        .quiz-code-box {{
            border: 1px solid var(--border);
            border-radius: 8px;
            overflow: hidden;
            background: var(--code-bg);
        }}

        .quiz-code-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #090e17;
            padding: 6px 12px;
            border-bottom: 1px solid var(--border);
            font-size: 0.78rem;
        }}

        .active-file-label {{
            color: var(--accent);
            font-family: 'Fira Code', monospace;
            font-weight: 600;
        }}

        .copy-small {{
            background: rgba(56, 189, 248, 0.15);
            color: var(--accent);
            border: 1px solid rgba(56, 189, 248, 0.3);
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.72rem;
            font-weight: 700;
            cursor: pointer;
        }}

        .copy-small:hover {{
            background: var(--accent);
            color: #090d16;
        }}

        .quiz-code {{
            background: var(--code-bg) !important;
            padding: 14px !important;
            margin: 0 !important;
            max-height: 400px;
            overflow-y: auto;
            font-family: 'Fira Code', monospace !important;
            font-size: 0.82rem !important;
        }}

        /* Toast */
        #quiz-toast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: #ffffff;
            padding: 12px 20px;
            border-radius: 8px;
            font-weight: 800;
            font-size: 0.88rem;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.25s ease;
            z-index: 9999;
        }}

        #quiz-toast.show {{
            transform: translateY(0);
            opacity: 1;
        }}
    </style>
</head>
<body>

    <div class="quiz-container">
        <!-- Sticky Header Bar -->
        <header class="quiz-top-bar">
            <div class="top-row">
                <div class="top-brand">
                    <span class="pulse-light"></span>
                    <div>
                        <div class="brand-title">DCCN LAB QUIZ QUICK PORTAL</div>
                        <div class="brand-subtitle">One-Click Copy & Solution Lookup Engine</div>
                    </div>
                </div>
                <div class="top-buttons">
                    <button class="btn-copy-all" id="btn-quiz-copy-all" onclick="copyAllSolutions()">
                        ⚡ ONE-CLICK COPY ALL (Q1–Q15)
                    </button>
                    <a href="all_solutions.txt" download class="btn-portal-link">
                        📥 all_solutions.txt
                    </a>
                    <a href="index.html" class="btn-portal-link">
                        📖 Full Manual
                    </a>
                </div>
            </div>

            <div class="filter-row">
                <input type="text" id="quiz-search" class="search-field" placeholder="🔍 Search question, topic (e.g. CRC, Dijkstra, Socket, Parity, IP)..." onkeyup="filterQuiz()">
                <div class="filter-tags">
                    <button class="tag-btn active" onclick="setCategory('all', this)">All (15)</button>
                    <button class="tag-btn" onclick="setCategory('code', this)">C Code (11)</button>
                    <button class="tag-btn" onclick="setCategory('theory', this)">Reports (4)</button>
                </div>
            </div>
        </header>

        <div id="quiz-cards-list">
            {cards_html}
        </div>
    </div>

    <div id="quiz-toast">Copied to clipboard!</div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-c.min.js"></script>
    <script>
        const ALL_SOLUTIONS_TEXT = {all_solutions_json};
        const EXPERIMENT_TEXTS = {question_texts_json};
        const QUIZ_FILES = {quiz_files_json};

        function showQuizToast(msg) {{
            const t = document.getElementById('quiz-toast');
            t.innerText = msg;
            t.classList.add('show');
            setTimeout(() => t.classList.remove('show'), 2200);
        }}

        function copyRawText(text, msg) {{
            if (navigator.clipboard && window.isSecureContext) {{
                navigator.clipboard.writeText(text).then(() => {{
                    showQuizToast(msg || "Copied to clipboard!");
                }}).catch(() => fallbackCopy(text, msg));
            }} else {{
                fallbackCopy(text, msg);
            }}
        }}

        function fallbackCopy(text, msg) {{
            const ta = document.createElement("textarea");
            ta.value = text;
            ta.style.position = "fixed";
            ta.style.left = "-9999px";
            ta.style.top = "0";
            document.body.appendChild(ta);
            ta.focus();
            ta.select();
            document.execCommand('copy');
            document.body.removeChild(ta);
            showQuizToast(msg || "Copied to clipboard!");
        }}

        function copyAllSolutions() {{
            copyRawText(ALL_SOLUTIONS_TEXT, "⚡ ALL 15 Experiments & Solutions Copied!");
            const btn = document.getElementById("btn-quiz-copy-all");
            if (btn) {{
                const orig = btn.innerHTML;
                btn.innerHTML = "✅ COPIED TO CLIPBOARD!";
                setTimeout(() => btn.innerHTML = orig, 2000);
            }}
        }}

        function copyQuestion(qid) {{
            if (EXPERIMENT_TEXTS[qid]) {{
                copyRawText(EXPERIMENT_TEXTS[qid], "📋 Copied Question & Solution for " + qid.toUpperCase() + "!");
            }}
        }}

        function copyQuizActiveCode(qid) {{
            const codeEl = document.getElementById(qid + "_code_view");
            if (codeEl) {{
                copyRawText(codeEl.innerText, "📋 Copied code for " + qid.toUpperCase() + "!");
            }}
        }}

        function showQuizCode(qid, fileIdx, fname) {{
            const files = QUIZ_FILES[qid];
            if (!files || !files[fileIdx]) return;
            const item = files[fileIdx];
            const codeEl = document.getElementById(qid + "_code_view");
            const labelEl = document.getElementById(qid + "_active_fname");
            if (codeEl) codeEl.innerText = item.code;
            if (labelEl) labelEl.innerText = "📄 " + item.name;
            if (window.Prism) Prism.highlightElement(codeEl);
            showQuizToast("Switched to " + item.name);
        }}

        let currentCategory = 'all';
        function setCategory(cat, el) {{
            currentCategory = cat;
            document.querySelectorAll('.tag-btn').forEach(b => b.classList.remove('active'));
            if (el) el.classList.add('active');
            filterQuiz();
        }}

        function filterQuiz() {{
            const query = document.getElementById('quiz-search').value.toLowerCase();
            const cards = document.querySelectorAll('.quiz-card');

            cards.forEach(card => {{
                const cat = card.getAttribute('data-category');
                const matchesCat = (currentCategory === 'all') || (cat === currentCategory);
                const text = card.innerText.toLowerCase();
                const matchesQuery = text.includes(query);
                card.style.display = (matchesCat && matchesQuery) ? 'block' : 'none';
            }});
        }}
    </script>
</body>
</html>
'''
    with open("quiz.html", "w", encoding="utf-8") as f:
        f.write(quiz_html)
    print("quiz.html generated successfully!")

def build_all():
    print("Building all solutions text...")
    all_text = build_all_solutions_plain_text()
    with open("all_solutions.txt", "w", encoding="utf-8") as f:
        f.write(all_text)
    print("all_solutions.txt generated successfully!")

    question_texts = {}
    for s in SECTIONS:
        question_texts[s["id"]] = build_question_plain_text(s)

    print("Generating index.html...")
    generate_index_html(all_text, question_texts)

    print("Generating quiz.html...")
    generate_quiz_html(all_text, question_texts)
    print("All builds completed successfully!")

if __name__ == "__main__":
    build_all()
