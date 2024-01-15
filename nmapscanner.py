#!/usr/bin/python3
import sys
import socket
from threading import Thread

host = socket.gethostbyname(sys.argv[1])
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

if len(sys.argv) != 4:
    print("enter proper command")
    print("--" * 40)
    print("nmapscanner -h")
    print("--" * 40)

    sys.exit()

print(f"[+] scanning target {sys.argv[1]} -> ip = {host}")

print(f"port_name           port_open           ")
port_name = {21: "ftp", 22: "ssh", 80: "http", 443: "https", 888: "tcp/udp"}


def connection(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((host, port))
    if not conn:
        print(f"{port_name[port]}                   {port}")
    else:
        pass

    s.close()


for i in range(start_port, end_port + 1):
    th = Thread(target=connection, args=(i,))
    th.start()
