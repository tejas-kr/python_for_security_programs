import socket


class Scanner:
    """Port Scanner Class
    """
    open_ports: list
    def __init__(self, ip_add):
        """__init__

        Args:
            ip_add (str): Ip Address where to scan ports
        """
        self.ip_add = ip_add
        self.open_ports = []

    def scan_ports(self, lower_port, higher_port):
        """Scan Ports

        Args:
            lower_port (int): Lower port val
            higher_port (int): Upper port val
        """
        for port in range(lower_port, higher_port+1):
            if self.is_open(port):
                self.open_ports.append(port)
    
    def is_open(self, port):
        """is_open

        Args:
            port (int): Port val

        Returns:
            Boolean: Checks if port is open or not
        """
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        result = s.connect_ex((self.ip_add, port,))
        s.close()
        return result == 0
    
    def __repr__(self):
        """__repr__

        Returns:
            str: String for class
        """
        return f"Scanner: {self.ip_add}"
    

def main():
    """Main Function
    """
    ip_add = 'localhost'
    scan = Scanner(ip_add)
    scan.scan_ports(lower_port=0, higher_port=100)
    print(scan.open_ports)


if __name__ == "__main__":
    main()