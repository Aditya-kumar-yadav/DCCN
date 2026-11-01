import os
import html

SECTIONS = [
    {
        "id": "q1",
        "tag": "Q1: Lab Network Topology, Interfaces, Routers & IP Pools",
        "badge": "Theory / Study",
        "unit": "Unit 1: Network Topology & Commands",
        "question": "1. To familiarize with the Lab Network Topology, Locating different interfaces, routers and switches. Studying different pools of IP addresses.",
        "files": [
            {"name": "Q1_Lab_Network_Topology.txt", "type": "txt", "title": "Network Topology & IP Pools Report"}
        ]
    },
    {
        "id": "q2",
        "tag": "Q2: Networking Commands (PING, TRACEROUTE), Telnet & Delay",
        "badge": "Theory / Experimental",
        "unit": "Unit 1: Network Topology & Commands",
        "question": "2. To learn and observe the usage of different networking commands e.g. PING, TRACEROUTE. Learning remote login using telnet session. Measuring typical average delays between different locations of the network.",
        "files": [
            {"name": "Q2_Networking_Commands_and_Delays.txt", "type": "txt", "title": "Networking Commands & Delay Analysis"}
        ]
    },
    {
        "id": "q3",
        "tag": "Q3: Ping Tool Statistics & Round-Trip Times",
        "badge": "Measurements",
        "unit": "Unit 1: Network Topology & Commands",
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
        "tag": "Q4: Trace Route Path Analysis",
        "badge": "Measurements",
        "unit": "Unit 1: Network Topology & Commands",
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
        "tag": "Q5: IPv4 Class Determination",
        "badge": "C Code",
        "unit": "Unit 2: IP Addressing & Conversion",
        "question": "5. Write a C/C++ program to determine if the IP address is in Class A, B, C, D, or E.",
        "files": [
            {"name": "Q5_IP_Class_Determination.c", "type": "c", "title": "IPv4 Class Identifier"}
        ]
    },
    {
        "id": "q6",
        "tag": "Q6: Dotted Decimal to 32-bit Address Translation",
        "badge": "C Code",
        "unit": "Unit 2: IP Addressing & Conversion",
        "question": "6. Write a C/C++ program to translate dotted decimal IP address into 32 bit address.",
        "files": [
            {"name": "Q6_Dotted_Decimal_To_32Bit.c", "type": "c", "title": "Dotted Decimal to 32-Bit Binary & Hex"}
        ]
    },
    {
        "id": "q7",
        "tag": "Q7: Bit Stuffing and De-stuffing",
        "badge": "C Code",
        "unit": "Unit 3: Data Link Layer Framing",
        "question": "7. Write a C/C++ program to perform bit stuffing and de-stuffing.",
        "files": [
            {"name": "Q7_Bit_Stuffing_Destuffing.c", "type": "c", "title": "HDLC Bit Stuffing & Framing"}
        ]
    },
    {
        "id": "q8",
        "tag": "Q8: Character Stuffing and De-stuffing",
        "badge": "C Code",
        "unit": "Unit 3: Data Link Layer Framing",
        "question": "8. Write a C/C++ program to perform character stuffing and de-stuffing.",
        "files": [
            {"name": "Q8_Character_Stuffing_Destuffing.c", "type": "c", "title": "Byte Stuffing (DLE STX / DLE ETX)"}
        ]
    },
    {
        "id": "q9",
        "tag": "Q9: Error Detection Methods",
        "badge": "C Code (4 Methods)",
        "unit": "Unit 4: Error Detection & Correction",
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
        "tag": "Q10: Error Correction using Hamming Code",
        "badge": "C Code",
        "unit": "Unit 4: Error Detection & Correction",
        "question": "10. Write a C/C++ program to perform error correction using Hamming code method.",
        "files": [
            {"name": "Q10_Hamming_Code.c", "type": "c", "title": "Hamming (7, 4) Code Encoding & Correction"}
        ]
    },
    {
        "id": "q11",
        "tag": "Q11: Socket Programming & Client-Server Model",
        "badge": "Study & C Code",
        "unit": "Unit 5: Socket Programming & HTTP",
        "question": "11. Study and implement model for Socket Programming and Client - Server model.",
        "files": [
            {"name": "Q11_Socket_Programming_Model.txt", "type": "txt", "title": "Socket Programming Lifecycle & Theory"},
            {"name": "Q11_1_Socket_Server.c", "type": "c", "title": "11.1 TCP Socket Server (Cross-platform)"},
            {"name": "Q11_2_Socket_Client.c", "type": "c", "title": "11.2 TCP Socket Client (Cross-platform)"}
        ]
    },
    {
        "id": "q12",
        "tag": "Q12: HTTP Sockets: Web Page Upload & Download",
        "badge": "C Code (2 Parts)",
        "unit": "Unit 5: Socket Programming & HTTP",
        "question": "12. Create a socket for HTTP for web page upload and download.",
        "files": [
            {"name": "Q12_1_HTTP_Download.c", "type": "c", "title": "12.1 HTTP GET Web Page Downloader"},
            {"name": "Q12_2_HTTP_Upload.c", "type": "c", "title": "12.2 HTTP POST Web Page / Data Uploader"}
        ]
    },
    {
        "id": "q13",
        "tag": "Q13: Simulation of PING & TRACEROUTE Commands",
        "badge": "C Code (2 Parts)",
        "unit": "Unit 6: Protocol Simulations",
        "question": "13. Write a code simulating PING and TRACEROUTE commands.",
        "files": [
            {"name": "Q13_1_Ping_Simulation.c", "type": "c", "title": "13.1 PING Command Simulator"},
            {"name": "Q13_2_Traceroute_Simulation.c", "type": "c", "title": "13.2 TRACEROUTE Command Simulator"}
        ]
    },
    {
        "id": "q14",
        "tag": "Q14: DHCP Server Simulation (DORA)",
        "badge": "C Code",
        "unit": "Unit 6: Protocol Simulations",
        "question": "14. Write a code simulating DHCP server.",
        "files": [
            {"name": "Q14_DHCP_Server_Simulation.c", "type": "c", "title": "DHCP Server Simulation (Discover, Offer, Request, Ack)"}
        ]
    },
    {
        "id": "q15",
        "tag": "Q15: Routing Table Implementation",
        "badge": "C Code (2 Algorithms)",
        "unit": "Unit 7: Routing Algorithms",
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

def generate_html():
    current_unit = ""
    sidebar_items_html = ""
    sections_html = ""

    for s in SECTIONS:
        if s["unit"] != current_unit:
            current_unit = s["unit"]
            sidebar_items_html += f'<div class="unit-header">{html.escape(current_unit)}</div>\n'
        
        sidebar_items_html += f'''
        <a href="#{s["id"]}" class="nav-item" onclick="highlightNav(this)">
            <span class="nav-tag">{s["id"].upper()}</span>
            <span class="nav-title">{html.escape(s["tag"])}</span>
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
                        <button class="copy-btn" onclick="copyToClipboard('{content_id}_code')">📋 Copy</button>
                        <a href="{fname}" download class="download-btn">⬇ Download</a>
                    </div>
                </div>
                <pre class="code-block"><code id="{content_id}_code" class="{lang_class}">{escaped_code}</code></pre>
            </div>
            '''

        escaped_q = html.escape(s["question"]).replace("\n", "<br>")

        sections_html += f'''
        <section id="{s["id"]}" class="question-card">
            <div class="card-header">
                <div class="card-title-group">
                    <span class="badge badge-{s["files"][0]["type"]}">{html.escape(s["badge"])}</span>
                    <h2 class="card-title">{html.escape(s["tag"])}</h2>
                </div>
                <a href="#{s["id"]}" class="anchor-link" title="Direct link">🔗</a>
            </div>
            
            <div class="problem-box">
                <strong>Problem Statement:</strong>
                <p>{escaped_q}</p>
            </div>

            <div class="tabs-container">
                <div class="tab-buttons-bar">
                    {files_tabs_html}
                </div>
                {files_content_html}
            </div>
        </section>
        '''

    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IT302 - DCCN Lab Assignment Solutions & Source Code</title>
    <meta name="description" content="Complete C programs and empirical reports for IT302 Data Communication and Computer Networks Lab Assignment.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
    <style>
        :root {{
            --bg-color: #0f172a;
            --surface-color: #1e293b;
            --surface-hover: #334155;
            --border-color: #334155;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent-blue: #38bdf8;
            --accent-green: #4ade80;
            --accent-purple: #c084fc;
            --accent-amber: #fbbf24;
            --code-bg: #090d16;
            --sidebar-width: 320px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
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
            padding: 20px;
            border-bottom: 1px solid var(--border-color);
            background: linear-gradient(180deg, rgba(30,41,59,1) 0%, rgba(15,23,42,0.8) 100%);
        }}

        .sidebar-title {{
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--accent-blue);
            margin-bottom: 4px;
        }}

        .sidebar-subtitle {{
            font-size: 0.8rem;
            color: var(--text-secondary);
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
            padding: 10px 0;
        }}

        .unit-header {{
            padding: 12px 16px 6px;
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
            font-weight: 600;
            font-size: 0.75rem;
            color: var(--accent-blue);
            background: rgba(56, 189, 248, 0.1);
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
            padding: 36px 48px;
            max-width: 1200px;
        }}

        .hero-banner {{
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 32px;
            margin-bottom: 36px;
            position: relative;
            overflow: hidden;
        }}

        .hero-banner::before {{
            content: '';
            position: absolute;
            top: -50px;
            right: -50px;
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(56,189,248,0.15) 0%, transparent 70%);
            border-radius: 50%;
        }}

        .hero-title {{
            font-size: 1.85rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 10px;
        }}

        .hero-desc {{
            color: var(--text-secondary);
            font-size: 1rem;
            max-width: 800px;
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
            padding: 9px 16px;
            border-radius: 6px;
            font-size: 0.88rem;
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
            background-color: var(--surface-color);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 36px;
            scroll-margin-top: 24px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }}

        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 16px;
            border-bottom: 1px solid rgba(255,255,255,0.06);
            padding-bottom: 14px;
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
            margin-bottom: 18px;
            font-size: 0.92rem;
            color: #cbd5e1;
        }}

        .problem-box strong {{
            color: var(--accent-blue);
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            display: block;
            margin-bottom: 4px;
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
            background-color: rgba(255,255,255,0.03);
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
            background-color: #0b0f19;
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
            transition: background 0.15s;
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

        /* Toast feedback */
        #toast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background-color: var(--accent-green);
            color: #052e16;
            padding: 10px 18px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.85rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.3s ease;
            z-index: 999;
        }}

        #toast.show {{
            transform: translateY(0);
            opacity: 1;
        }}

        /* Responsive */
        @media (max-width: 900px) {{
            #sidebar {{
                display: none;
            }}
            #main {{
                margin-left: 0;
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>

    <!-- Left Sidebar -->
    <nav id="sidebar">
        <div class="sidebar-header">
            <div class="sidebar-title">IT302 DCCN LAB</div>
            <div class="sidebar-subtitle">Assignments & Source Codes</div>
        </div>
        <div class="search-box">
            <input type="text" id="search-input" class="search-input" placeholder="Search questions..." onkeyup="filterQuestions()">
        </div>
        <div class="nav-list" id="nav-list">
            {sidebar_items_html}
        </div>
    </nav>

    <!-- Main Content Area -->
    <main id="main">
        <header class="hero-banner">
            <h1 class="hero-title">IT302 — Data Communication & Computer Networks</h1>
            <p class="hero-desc">
                Interactive laboratory portal containing complete C source code implementations, 
                measured network statistics (PING, Traceroute), and study reports.
            </p>
            <div class="hero-buttons">
                <a href="https://github.com/Aryan9891/DCCN-Lab-repo" target="_blank" class="btn btn-primary">
                    ⭐ View on GitHub
                </a>
                <a href="IT302 DCCNLAB ASSIGNMENT.pdf" target="_blank" class="btn btn-secondary">
                    📄 Original Assignment PDF
                </a>
                <a href="README.md" target="_blank" class="btn btn-secondary">
                    📋 README & Guide
                </a>
            </div>
        </header>

        <div id="questions-container">
            {sections_html}
        </div>
    </main>

    <div id="toast">Copied to clipboard!</div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-c.min.js"></script>
    <script>
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

        function copyToClipboard(elementId) {{
            const codeEl = document.getElementById(elementId);
            if (!codeEl) return;
            const text = codeEl.innerText;
            navigator.clipboard.writeText(text).then(() => {{
                showToast("Code copied to clipboard!");
            }}).catch(() => {{
                showToast("Failed to copy!");
            }});
        }}

        function showToast(msg) {{
            const toast = document.getElementById('toast');
            toast.innerText = msg;
            toast.classList.add('show');
            setTimeout(() => {{
                toast.classList.remove('show');
            }}, 2000);
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
    </script>
</body>
</html>
'''
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(full_html)
    print("index.html generated successfully!")

if __name__ == "__main__":
    generate_html()
