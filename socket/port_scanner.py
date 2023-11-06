import socket


class Scanner:
    """Port Scanner Class
    """
    open_ports: list
    def __init__(self, ip_add):
        self.ip_add = ip_add
        self.open_ports = []

    def scan_ports(self, lower_port, higher_port):
        for port in range(lower_port, higher_port+1):
            if self.is_open(port):
                self.open_ports.append(port)
    
    def is_open(self, port):
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        result = s.connect_ex((self.ip_add, port,))
        s.close()
        return result == 0
    
    def __repr__(self):
        return f"Scanner: {self.ip}"
    

def main():
    ip_add = 'localhost'
    scan = Scanner(ip_add)
    scan.scan_ports(lower_port=0, higher_port=100)
    print(scan.open_ports)


if __name__ == "__main__":
    main()