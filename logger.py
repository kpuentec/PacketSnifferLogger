from datetime import datetime
import json
from scapy.layers.inet import IP, TCP, UDP
from config import FILE_PATH

def process_packet(packet):
    log = {"timestamp": datetime.now().isoformat()}
    if IP in packet:  
        log.update({
            "src": packet[IP].src,
            "dst": packet[IP].dst,
            "proto": packet.proto,
        })

        if TCP in packet:
            log["flags"] = str(packet[TCP].flags)
        elif UDP in packet:
            log["flags"] = "UDP"

    elif packet.haslayer("ARP"):
        log["proto"] = "ARP"
        log["src"] = packet.psrc
        log["dst"] = packet.pdst

    else:
        return

    try:
        with open(FILE_PATH, 'r') as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.append(log)

    with open(FILE_PATH, 'w') as f:
        json.dump(logs, f, indent=4)

    print(f"Logged packet: {log['src']} -> {log['dst']} ({log.get('flags')})")

    

def view():
    with open(FILE_PATH, 'r') as f:
        logs = json.load(f)
    for log in logs:
        print(log)