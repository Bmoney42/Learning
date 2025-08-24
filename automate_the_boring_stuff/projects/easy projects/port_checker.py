port = 69

common_ports = {
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3389: "RDP"
}

while True:
    raw_port = input("port: ")
    if raw_port.isdigit():
        port = int(raw_port)
        if 1 <= port <= 65535:
            print("Valid!")
            if port in common_ports:
                service = common_ports[port]
                print("common_port:", service)
            else:
                print("not a common port")
        else:
            print("out of range, try again")
    else:
        print("not a number, try again")
