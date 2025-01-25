import socket
import ssl

# Server settings
HOST = 'localhost'
PORT = 65432

# Wrap the socket with SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

# Create and bind the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}")
    
    # Wrap the socket with TLS
    with context.wrap_socket(server_socket, server_side=True) as tls_socket:
        while True:
            print("Waiting for a connection...")
            conn, addr = tls_socket.accept()
            print(f"Connection established with {addr}")
            
            # Receive file data
            with conn:
                with open("received_file.txt", "wb") as f:
                    print("Receiving file...")
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                    print("File received successfully!")
