from logger import view
from sniffer import sniffing

def main():
    print("\n")
    print("*===== Packet Sniffer Logger =====*\n")
    print("- Foundational tool to help detect suspicious traffic patterns.\n")
    print("- Sniff packets and save packet data in structured JSON\n")

    print("1. Packet Sniff (20 packets)")
    print("2. View logged packets")
    print("3. Quit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        sniffing()
        main()
    elif choice == "2":
        view()
        main()
    elif choice == "3":
        print("Goodbye!\n")
        exit()
    else:
        print("Invalid choice. Try again.\n")
        main()


if __name__ == "__main__":
        main()