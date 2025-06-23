import scapy.all as scapy
from logger import process_packet

def sniffing():
    try:
        scapy.sniff(count=20, prn=process_packet, iface="Ethernet")
    except KeyboardInterrupt:
        print("Sniffing stopped by user.")   
    except Exception as e:
        print(f"Error: {e}")
    