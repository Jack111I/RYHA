import socket

def run():
    # Scans the internal network for open ports
    active_ips = []
    for i in range(1, 255):
        ip = f"192.168.1.{i}"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.01)
        if s.connect_ex((ip, 445)) == 0: active_ips.append(ip)
        s.close()
    return active_ips