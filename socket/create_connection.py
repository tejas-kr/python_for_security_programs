import socket


def main():
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    host = 'localhost'
    port = 8080
    s.connect((host, port,))
    print("Connected")

    s.close()

if __name__ == "__main__":
    main()
