import os
import html

SECTIONS = [
    {
        "id": "q1",
        "num": "1",
        "title": "Lab Network Topology, Interfaces, Routers & IP Pools",
        "badge": "Theory",
        "unit": "Unit 1: Network Topology & Commands",
        "concept": "Extended Star Topology, Switch CAM tables, Router default gateways, and RFC 1918 Private IP pools (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16).",
        "question": "1. To familiarize with the Lab Network Topology, Locating different interfaces, routers and switches. Studying different pools of IP addresses.",
        "files": [
            {"name": "Q1_Lab_Network_Topology.txt", "type": "txt", "title": "Network Topology & IP Pools Report"}
        ]
    },
    {
        "id": "q2",
        "num": "2",
        "title": "Networking Commands (PING, TRACEROUTE), Telnet & Delay",
        "badge": "Theory",
        "unit": "Unit 1: Network Topology & Commands",
        "concept": "PING (ICMP Type 8 Echo Request / Type 0 Reply), TRACEROUTE (TTL expiry, ICMP Type 11), Telnet (Port 23 cleartext) vs SSH (Port 22 encrypted), and 4 nodal delays (Processing, Queuing, Transmission, Propagation).",
        "question": "2. To learn and observe the usage of different networking commands e.g. PING, TRACEROUTE. Learning remote login using telnet session. Measuring typical average delays between different locations of the network.",
        "files": [
            {"name": "Q2_Networking_Commands_and_Delays.txt", "type": "txt", "title": "Networking Commands & Delay Analysis"}
        ]
    },
    {
        "id": "q3",
        "num": "3",
        "title": "Ping Tool Statistics & Round-Trip Times",
        "badge": "Measurements",
        "unit": "Unit 1: Network Topology & Commands",
        "concept": "Measured round trip time (RTT) and packet loss for google.com (Avg RTT ~38ms), facebook.com (Avg RTT ~58ms), and bitmesra.ac.in (Avg RTT ~150ms).",
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
        "title": "Trace Route Path Analysis",
        "badge": "Measurements",
        "unit": "Unit 1: Network Topology & Commands",
        "concept": "Hop-by-hop router discovery and latency progression across local gateway and transit AS carriers to Google (7 hops), Facebook (9 hops), and BIT Mesra (10 hops).",
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
        "title": "IPv4 Class Determination",
        "badge": "C Code",
        "unit": "Unit 2: IP Addressing & Conversion",
        "concept": "Class A: 0-127 (mask 255.0.0.0), Class B: 128-191 (mask 255.255.0.0), Class C: 192-223 (mask 255.255.255.0), Class D: 224-239 (Multicast), Class E: 240-255 (Experimental).",
        "compile": "gcc Q5_IP_Class_Determination.c -o Q5",
        "question": "5. Write a C/C++ program to determine if the IP address is in Class A, B, C, D, or E.",
        "files": [
            {"name": "Q5_IP_Class_Determination.c", "type": "c", "title": "IPv4 Class Identifier"}
        ]
    },
    {
        "id": "q6",
        "num": "6",
        "title": "Dotted Decimal to 32-bit Address Translation",
        "badge": "C Code",
        "unit": "Unit 2: IP Addressing & Conversion",
        "concept": "Combines 4 octets via bitwise shift: (A<<24) | (B<<16) | (C<<8) | D into 32-bit binary, decimal, and hex representation.",
        "compile": "gcc Q6_Dotted_Decimal_To_32Bit.c -o Q6",
        "question": "6. Write a C/C++ program to translate dotted decimal IP address into 32 bit address.",
        "files": [
            {"name": "Q6_Dotted_Decimal_To_32Bit.c", "type": "c", "title": "Dotted Decimal to 32-Bit Binary & Hex"}
        ]
    },
    {
        "id": "q7",
        "num": "7",
        "title": "Bit Stuffing and De-stuffing",
        "badge": "C Code",
        "unit": "Unit 3: Data Link Layer Framing",
        "concept": "HDLC bit framing: Stuffs '0' after five consecutive 1s to prevent false flag pattern (01111110 / 0x7E). Receiver discards the 0 after five 1s.",
        "compile": "gcc Q7_Bit_Stuffing_Destuffing.c -o Q7",
        "question": "7. Write a C/C++ program to perform bit stuffing and de-stuffing.",
        "files": [
            {"name": "Q7_Bit_Stuffing_Destuffing.c", "type": "c", "title": "HDLC Bit Stuffing & Framing"}
        ]
    },
    {
        "id": "q8",
        "num": "8",
        "title": "Character Stuffing and De-stuffing",
        "badge": "C Code",
        "unit": "Unit 3: Data Link Layer Framing",
        "concept": "Byte-oriented framing with DLE STX (start) and DLE ETX (end). Stuffs extra DLE when DLE appears in data payload.",
        "compile": "gcc Q8_Character_Stuffing_Destuffing.c -o Q8",
        "question": "8. Write a C/C++ program to perform character stuffing and de-stuffing.",
        "files": [
            {"name": "Q8_Character_Stuffing_Destuffing.c", "type": "c", "title": "Byte Stuffing (DLE STX / DLE ETX)"}
        ]
    },
    {
        "id": "q9",
        "num": "9",
        "title": "Error Detection Methods",
        "badge": "C Code",
        "unit": "Unit 4: Error Detection & Correction",
        "concept": "1) Single Parity (Even/Odd), 2) 2D Matrix Parity (LRC & VRC - locates 1-bit error), 3) CRC (Modulo-2 XOR polynomial division), 4) Internet Checksum RFC 1071 (16-bit 1's complement sum).",
        "compile": "gcc Q9_1_Single_Parity.c -o Q9_1 && gcc Q9_2_Two_Dimension_Parity.c -o Q9_2 && gcc Q9_3_CRC.c -o Q9_3 && gcc Q9_4_Internet_Checksum.c -o Q9_4",
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
        "title": "Error Correction using Hamming Code",
        "badge": "C Code",
        "unit": "Unit 4: Error Detection & Correction",
        "concept": "Hamming (7, 4) Code: 4 data bits + 3 parity bits at power-of-2 positions. Syndrome S = s3 s2 s1 points to the exact corrupted bit index (1-7) to flip and correct.",
        "compile": "gcc Q10_Hamming_Code.c -o Q10",
        "question": "10. Write a C/C++ program to perform error correction using Hamming code method.",
        "files": [
            {"name": "Q10_Hamming_Code.c", "type": "c", "title": "Hamming (7, 4) Code Encoding & Correction"}
        ]
    },
    {
        "id": "q11",
        "num": "11",
        "title": "Socket Programming & Client-Server Model",
        "badge": "C Code",
        "unit": "Unit 5: Socket Programming & HTTP",
        "concept": "TCP Socket Lifecycle: Server: socket() -> bind() -> listen() -> accept() -> recv()/send(). Client: socket() -> connect() -> send()/recv().",
        "compile": "gcc Q11_1_Socket_Server.c -o server && gcc Q11_2_Socket_Client.c -o client (Windows: add -lws2_32)",
        "question": "11. Study and implement model for Socket Programming and Client - Server model.",
        "files": [
            {"name": "Q11_Socket_Programming_Model.txt", "type": "txt", "title": "Socket Programming Lifecycle & Theory"},
            {"name": "Q11_1_Socket_Server.c", "type": "c", "title": "11.1 TCP Socket Server"},
            {"name": "Q11_2_Socket_Client.c", "type": "c", "title": "11.2 TCP Socket Client"}
        ]
    },
    {
        "id": "q12",
        "num": "12",
        "title": "HTTP Sockets: Web Page Upload & Download",
        "badge": "C Code",
        "unit": "Unit 5: Socket Programming & HTTP",
        "concept": "HTTP over raw TCP port 80: 1) GET request download to local HTML file, 2) POST request data upload with Content-Length header.",
        "compile": "gcc Q12_1_HTTP_Download.c -o Q12_1 && gcc Q12_2_HTTP_Upload.c -o Q12_2 (Windows: add -lws2_32)",
        "question": "12. Create a socket for HTTP for web page upload and download.",
        "files": [
            {"name": "Q12_1_HTTP_Download.c", "type": "c", "title": "12.1 HTTP GET Web Page Downloader"},
            {"name": "Q12_2_HTTP_Upload.c", "type": "c", "title": "12.2 HTTP POST Web Page Uploader"}
        ]
    },
    {
        "id": "q13",
        "num": "13",
        "title": "Simulation of PING & TRACEROUTE Commands",
        "badge": "C Code",
        "unit": "Unit 6: Protocol Simulations",
        "concept": "Simulates ICMP echo requests, latency variations, packet loss, min/avg/max RTT, and hop-by-hop TTL increments.",
        "compile": "gcc Q13_1_Ping_Simulation.c -o Q13_1 && gcc Q13_2_Traceroute_Simulation.c -o Q13_2",
        "question": "13. Write a code simulating PING and TRACEROUTE commands.",
        "files": [
            {"name": "Q13_1_Ping_Simulation.c", "type": "c", "title": "13.1 PING Command Simulator"},
            {"name": "Q13_2_Traceroute_Simulation.c", "type": "c", "title": "13.2 TRACEROUTE Command Simulator"}
        ]
    },
    {
        "id": "q14",
        "num": "14",
        "title": "DHCP Server Simulation (DORA)",
        "badge": "C Code",
        "unit": "Unit 6: Protocol Simulations",
        "concept": "Complete DHCP 4-way handshake: Discover (broadcast), Offer (IP allocation), Request (client selection), Acknowledgment (lease assignment).",
        "compile": "gcc Q14_DHCP_Server_Simulation.c -o Q14",
        "question": "14. Write a code simulating DHCP server.",
        "files": [
            {"name": "Q14_DHCP_Server_Simulation.c", "type": "c", "title": "DHCP Server Simulation (DORA)"}
        ]
    },
    {
        "id": "q15",
        "num": "15",
        "title": "Routing Table Implementation",
        "badge": "C Code",
        "unit": "Unit 7: Routing Algorithms",
        "concept": "1) Dijkstra Link-State Shortest Path Tree (OSPF) with next-hop mapping, 2) Distance Vector Bellman-Ford (RIP) iterative neighbor table convergence.",
        "compile": "gcc Q15_1_Dijkstra_Routing.c -o Q15_1 && gcc Q15_2_Distance_Vector_Routing.c -o Q15_2",
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

def generate_index_html():
    current_unit = ""
    sidebar_items_html = ""
    sections_html = ""
    ribbon_chips_html = ""

    for s in SECTIONS:
        ribbon_chips_html += f'''
        <div class="ribbon-chip" title="Click icon to copy, title to jump">
            <a href="#{s["id"]}" class="chip-link">Q{s["num"]}</a>
            <button class="chip-copy-btn" onclick="copyQuestion('{s["id"]}', event)" title="1-Click Copy Q{s["num"]} + Code">📋</button>
        </div>'''

        if s["unit"] != current_unit:
            current_unit = s["unit"]
            sidebar_items_html += f'<div class="unit-header">{html.escape(current_unit)}</div>\n'
        
        sidebar_items_html += f'''
        <a href="#{s["id"]}" class="nav-item" onclick="highlightNav(this)">
            <span class="nav-tag">Q{s["num"]}</span>
            <span class="nav-title">{html.escape(s["title"])}</span>
        </a>'''

        files_tabs_html = ""
        files_content_html = ""

        for idx, f in enumerate(s["files"]):
            fname = f["name"]
            ftitle = f["title"]
            ftype = f["type"]
            fcontent = read_file_content(fname)
            escaped_code = html.escape(fcontent)
            is_active = "active" if idx == 0 else ""
            content_id = f"{s['id']}_content_{idx}"
            lang_class = "language-c" if ftype == "c" else "language-none"

            files_tabs_html += f'''
            <button class="tab-btn {is_active}" onclick="switchTab('{s["id"]}', {idx})">
                {html.escape(ftitle)}
            </button>'''

            files_content_html += f'''
            <div id="{content_id}" class="tab-content {is_active}">
                <div class="code-header">
                    <span class="file-name">📄 <a href="{fname}" target="_blank">{html.escape(fname)}</a></span>
                    <div class="code-actions">
                        <button class="copy-btn" onclick="copyCodeOnly('{content_id}_code', '{html.escape(fname)}')">📋 Copy Code Only</button>
                        <a href="{fname}" download class="download-btn">⬇ Download</a>
                    </div>
                </div>
                <pre class="code-block"><code id="{content_id}_code" class="{lang_class}">{escaped_code}</code></pre>
            </div>'''

        escaped_q = html.escape(s["question"]).replace("\n", "<br>")
        compile_html = ""
        if "compile" in s:
            compile_html = f'''
            <div class="compile-box">
                <span class="compile-label">🛠️ GCC:</span>
                <code class="compile-text">{html.escape(s["compile"])}</code>
            </div>'''

        concept_html = ""
        if "concept" in s:
            concept_html = f'''
            <div class="concept-box">
                <strong>💡 Key Concept:</strong>
                <span class="concept-text">{html.escape(s["concept"])}</span>
            </div>'''

        sections_html += f'''
        <section id="{s["id"]}" class="question-card">
            <div class="card-header">
                <div class="card-title-group">
                    <span class="badge badge-{s["files"][0]["type"]}">{html.escape(s["badge"])}</span>
                    <h2 class="card-title">Q{s["num"]}: {html.escape(s["title"])}</h2>
                </div>
                <div class="card-header-actions">
                    <button class="btn-copy-card" onclick="copyQuestion('{s["id"]}')" title="Copy Question & Solution">
                        📋 Copy Question & Solution
                    </button>
                    <a href="#{s["id"]}" class="anchor-link" title="Direct link">🔗</a>
                </div>
            </div>

            <div class="problem-box">
                <strong>Problem Statement:</strong>
                <p class="problem-text">{escaped_q}</p>
            </div>

            {concept_html}
            {compile_html}

            <div class="tabs-container">
                <div class="tab-buttons-bar">
                    {files_tabs_html}
                </div>
                {files_content_html}
            </div>
        </section>'''

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IT302 DCCN Lab Solutions | 1-Click Copy All for Quiz</title>
    <meta name="description" content="One-click copy all DCCN lab experiments and complete C solutions for IT302 quiz.">
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
            --accent-green: #10b981;
            --accent-purple: #c084fc;
            --accent-amber: #fbbf24;
            --code-bg: #070d18;
            --sidebar-width: 310px;
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

        /* Sidebar */
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
            padding: 16px 20px;
            border-bottom: 1px solid var(--border-color);
            background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
        }}

        .sidebar-title {{
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--accent-blue);
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
            padding: 10px;
            background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
            color: #ffffff;
            border: 1px solid #38bdf8;
            border-radius: 8px;
            font-size: 0.85rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .btn-sidebar-copy:hover {{
            background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%);
        }}

        .search-box {{
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
        }}

        .search-input {{
            width: 100%;
            padding: 8px 12px;
            background-color: var(--bg-color);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            color: var(--text-primary);
            font-size: 0.85rem;
            outline: none;
        }}

        .search-input:focus {{
            border-color: var(--accent-blue);
        }}

        .nav-list {{
            flex: 1;
            padding: 8px 0 24px;
        }}

        .unit-header {{
            padding: 12px 16px 4px;
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
            padding: 7px 16px;
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 0.82rem;
            transition: all 0.15s;
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
        }}

        .nav-title {{
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        /* Main Content */
        #main {{
            margin-left: var(--sidebar-width);
            flex: 1;
            padding: 20px 36px 60px;
            max-width: 1250px;
        }}

        /* Sticky Mega Bar */
        .quiz-mega-banner {{
            position: sticky;
            top: 14px;
            z-index: 90;
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border: 2px solid #0284c7;
            border-radius: 12px;
            padding: 14px 18px;
            margin-bottom: 24px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(10px);
        }}

        .quiz-banner-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 10px;
        }}

        .quiz-banner-info {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .pulse-dot {{
            width: 10px;
            height: 10px;
            background-color: var(--accent-green);
            border-radius: 50%;
            box-shadow: 0 0 10px var(--accent-green);
        }}

        .quiz-banner-heading {{
            font-size: 1.05rem;
            font-weight: 800;
            color: #ffffff;
        }}

        .quiz-banner-sub {{
            font-size: 0.78rem;
            color: var(--accent-cyan);
        }}

        .btn-mega-copy {{
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: #ffffff;
            border: 1px solid #34d399;
            padding: 10px 22px;
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
        }}

        .chip-link {{
            color: #cbd5e1;
            text-decoration: none;
            padding: 3px 8px;
            font-weight: 600;
            font-family: 'Fira Code', monospace;
        }}

        .chip-link:hover {{
            color: var(--accent-blue);
        }}

        .chip-copy-btn {{
            background: rgba(56, 189, 248, 0.15);
            border: none;
            border-left: 1px solid var(--border-color);
            color: var(--accent-blue);
            padding: 3px 6px;
            cursor: pointer;
            font-size: 0.75rem;
        }}

        .chip-copy-btn:hover {{
            background: var(--accent-blue);
            color: #0f172a;
        }}

        /* Hero */
        .hero-banner {{
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px 28px;
            margin-bottom: 28px;
        }}

        .hero-title {{
            font-size: 1.65rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 6px;
        }}

        .hero-desc {{
            color: var(--text-secondary);
            font-size: 0.92rem;
            max-width: 850px;
            margin-bottom: 16px;
        }}

        .hero-buttons {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            text-decoration: none;
            cursor: pointer;
            border: 1px solid transparent;
            transition: all 0.15s;
        }}

        .btn-primary {{
            background-color: var(--accent-blue);
            color: #0f172a;
        }}

        .btn-primary:hover {{
            background-color: #7dd3fc;
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
            padding: 22px;
            margin-bottom: 28px;
            scroll-margin-top: 110px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 14px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 12px;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .card-title-group {{
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .card-title {{
            font-size: 1.2rem;
            font-weight: 700;
            color: #ffffff;
        }}

        .card-header-actions {{
            display: flex;
            align-items: center;
            gap: 8px;
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
            transition: all 0.15s;
        }}

        .btn-copy-card:hover {{
            background: var(--accent-blue);
            color: #0f172a;
        }}

        .anchor-link {{
            color: var(--text-secondary);
            text-decoration: none;
            opacity: 0.6;
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
        }}

        .badge-c {{
            background: rgba(16, 185, 129, 0.15);
            color: var(--accent-green);
            border: 1px solid rgba(16, 185, 129, 0.3);
        }}

        .badge-txt {{
            background: rgba(192, 132, 252, 0.15);
            color: var(--accent-purple);
            border: 1px solid rgba(192, 132, 252, 0.3);
        }}

        .problem-box {{
            background-color: rgba(15, 23, 42, 0.6);
            border-left: 4px solid var(--accent-blue);
            padding: 10px 14px;
            border-radius: 4px;
            margin-bottom: 12px;
            font-size: 0.9rem;
            color: #cbd5e1;
        }}

        .problem-box strong {{
            color: var(--accent-blue);
            font-size: 0.8rem;
            text-transform: uppercase;
            display: block;
            margin-bottom: 2px;
        }}

        .concept-box {{
            background-color: rgba(251, 191, 36, 0.08);
            border-left: 4px solid var(--accent-amber);
            padding: 8px 12px;
            border-radius: 4px;
            margin-bottom: 12px;
            font-size: 0.85rem;
            color: #fde68a;
        }}

        .concept-box strong {{
            color: var(--accent-amber);
            font-size: 0.78rem;
            display: block;
            margin-bottom: 2px;
        }}

        .compile-box {{
            display: flex;
            align-items: center;
            gap: 8px;
            background: rgba(0, 0, 0, 0.35);
            border: 1px dashed var(--border-color);
            padding: 5px 10px;
            border-radius: 6px;
            margin-bottom: 14px;
            font-size: 0.78rem;
            color: #94a3b8;
            font-family: 'Fira Code', monospace;
        }}

        .compile-label {{
            color: var(--accent-green);
            font-weight: 700;
        }}

        /* Tabs */
        .tabs-container {{
            margin-top: 12px;
        }}

        .tab-buttons-bar {{
            display: flex;
            gap: 6px;
            overflow-x: auto;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 10px;
        }}

        .tab-btn {{
            background: transparent;
            border: none;
            color: var(--text-secondary);
            padding: 7px 12px;
            font-size: 0.82rem;
            font-weight: 500;
            cursor: pointer;
            border-radius: 6px 6px 0 0;
            border-bottom: 2px solid transparent;
            transition: all 0.15s;
            white-space: nowrap;
        }}

        .tab-btn:hover {{
            color: var(--text-primary);
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
            padding: 7px 12px;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            border: 1px solid var(--border-color);
            border-bottom: none;
            font-size: 0.78rem;
        }}

        .file-name a {{
            color: var(--accent-blue);
            text-decoration: none;
            font-family: 'Fira Code', monospace;
        }}

        .code-actions {{
            display: flex;
            gap: 6px;
        }}

        .copy-btn, .download-btn {{
            background-color: var(--surface-hover);
            color: var(--text-primary);
            border: 1px solid var(--border-color);
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.74rem;
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
            padding: 14px !important;
            margin: 0 !important;
            max-height: 440px;
            overflow-y: auto;
            font-family: 'Fira Code', monospace !important;
            font-size: 0.82rem !important;
        }}

        /* Toast */
        #toast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: #ffffff;
            padding: 10px 18px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 0.88rem;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.25s ease;
            z-index: 999;
        }}

        #toast.show {{
            transform: translateY(0);
            opacity: 1;
        }}

        @media (max-width: 900px) {{
            #sidebar {{ display: none; }}
            #main {{ margin-left: 0; padding: 14px; }}
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
            <input type="text" id="search-input" class="search-input" placeholder="Search questions..." onkeyup="filterQuestions()">
        </div>
        <div class="nav-list" id="nav-list">
            {sidebar_items_html}
        </div>
    </nav>

    <!-- Main Content -->
    <main id="main">

        <!-- Sticky Quiz Mega Bar -->
        <div class="quiz-mega-banner">
            <div class="quiz-banner-top">
                <div class="quiz-banner-info">
                    <span class="pulse-dot"></span>
                    <div>
                        <div class="quiz-banner-heading">DCCN LAB QUIZ 1-CLICK COPY PORTAL</div>
                        <div class="quiz-banner-sub">15 Experiments • Complete C Codes • Quick Copies Ready</div>
                    </div>
                </div>
                <button class="btn-mega-copy" id="btn-copy-all-top" onclick="copyAllSolutions()">
                    ⚡ ONE-CLICK COPY ALL (Q1–Q15)
                </button>
            </div>

            <div class="quick-ribbon-bar">
                <span class="ribbon-label">Quick Copy:</span>
                {ribbon_chips_html}
            </div>
        </div>

        <header class="hero-banner">
            <h1 class="hero-title">IT302 — Data Communication & Computer Networks</h1>
            <p class="hero-desc">
                Complete C source code implementations, empirical network statistics, and study reports for all 15 experiments.
                Click the 1-click copy button above to copy all experiments with solutions into your clipboard at once.
            </p>
            <div class="hero-buttons">
                <button class="btn btn-primary" onclick="copyAllSolutions()">
                    ⚡ Copy All Experiments & Solutions
                </button>
                <a href="IT302 DCCNLAB ASSIGNMENT.pdf" target="_blank" class="btn btn-secondary">
                    📄 Original Assignment PDF
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

    <div id="toast">✅ Copied to clipboard!</div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-c.min.js"></script>
    <script>
        function switchTab(sectionId, tabIndex) {{
            const card = document.getElementById(sectionId);
            card.querySelectorAll('.tab-btn').forEach((b, i) => b.classList.toggle('active', i === tabIndex));
            card.querySelectorAll('.tab-content').forEach((c, i) => c.classList.toggle('active', i === tabIndex));
        }}

        function copyToClipboard(text, msg) {{
            if (navigator.clipboard && window.isSecureContext) {{
                navigator.clipboard.writeText(text).then(() => showToast(msg)).catch(() => fallbackCopy(text, msg));
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
            showToast(msg);
        }}

        function copyAllSolutions() {{
            let output = "================================================================================\\n";
            output += "IT302 - DCCN LAB ASSIGNMENT: ALL EXPERIMENTS & SOLUTIONS (Q1 TO Q15)\\n";
            output += "================================================================================\\n\\n";

            document.querySelectorAll('.question-card').forEach(card => {{
                const title = card.querySelector('.card-title')?.innerText || '';
                const problem = card.querySelector('.problem-text')?.innerText || '';
                const concept = card.querySelector('.concept-text')?.innerText || '';
                const compile = card.querySelector('.compile-text')?.innerText || '';

                output += "================================================================================\\n";
                output += title + "\\n";
                output += "================================================================================\\n";
                output += "Problem Statement:\\n" + problem + "\\n\\n";
                if (concept) output += "Key Concept:\\n" + concept + "\\n\\n";
                if (compile) output += "Compilation:\\n" + compile + "\\n\\n";

                card.querySelectorAll('.tab-content').forEach(tc => {{
                    const fname = tc.querySelector('.file-name a')?.innerText || '';
                    const code = tc.querySelector('code')?.innerText || '';
                    output += "--------------------------------------------------------------------------------\\n";
                    output += "--- File: " + fname + " ---\\n";
                    output += "--------------------------------------------------------------------------------\\n";
                    output += code + "\\n\\n";
                }});
                output += "\\n";
            }});

            copyToClipboard(output, "⚡ ALL 15 EXPERIMENTS & SOLUTIONS COPIED!");
            const btn = document.getElementById("btn-copy-all-top");
            if (btn) {{
                const orig = btn.innerHTML;
                btn.innerHTML = "✅ COPIED TO CLIPBOARD!";
                setTimeout(() => btn.innerHTML = orig, 2000);
            }}
        }}

        function copyQuestion(sectionId, event) {{
            if (event) event.stopPropagation();
            const card = document.getElementById(sectionId);
            if (!card) return;
            const title = card.querySelector('.card-title')?.innerText || '';
            const problem = card.querySelector('.problem-text')?.innerText || '';
            const concept = card.querySelector('.concept-text')?.innerText || '';
            const compile = card.querySelector('.compile-text')?.innerText || '';

            let output = "================================================================================\\n";
            output += title + "\\n";
            output += "================================================================================\\n";
            output += "Problem Statement:\\n" + problem + "\\n\\n";
            if (concept) output += "Key Concept:\\n" + concept + "\\n\\n";
            if (compile) output += "Compilation:\\n" + compile + "\\n\\n";

            card.querySelectorAll('.tab-content').forEach(tc => {{
                const fname = tc.querySelector('.file-name a')?.innerText || '';
                const code = tc.querySelector('code')?.innerText || '';
                output += "--------------------------------------------------------------------------------\\n";
                output += "--- File: " + fname + " ---\\n";
                output += "--------------------------------------------------------------------------------\\n";
                output += code + "\\n\\n";
            }});

            copyToClipboard(output, "📋 " + title + " Copied!");
        }}

        function copyCodeOnly(elementId, fname) {{
            const codeEl = document.getElementById(elementId);
            if (!codeEl) return;
            copyToClipboard(codeEl.innerText, "📋 Copied " + fname + " code!");
        }}

        function showToast(msg) {{
            const toast = document.getElementById('toast');
            toast.innerText = msg;
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2200);
        }}

        function filterQuestions() {{
            const query = document.getElementById('search-input').value.toLowerCase();
            document.querySelectorAll('.nav-item').forEach(item => {{
                item.style.display = item.innerText.toLowerCase().includes(query) ? 'flex' : 'none';
            }});
            document.querySelectorAll('.question-card').forEach(card => {{
                card.style.display = card.innerText.toLowerCase().includes(query) ? 'block' : 'none';
            }});
        }}

        function highlightNav(el) {{
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            el.classList.add('active');
        }}
    </script>
</body>
</html>'''

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("index.html generated successfully!")

if __name__ == "__main__":
    generate_index_html()
