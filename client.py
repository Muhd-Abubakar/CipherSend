import socket
import ssl

# Client settings
HOST = 'localhost'
PORT = 65432
FILE_TO_SEND = 'file_to_send.txt'

# Wrap the socket with SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(cafile="server.crt")

# Create a secure connection
with socket.create_connection((HOST, PORT)) as client_socket:
    with context.wrap_socket(client_socket, server_hostname=HOST) as tls_socket:
        print("Connected to the server. Sending file...")
        
        # Send file data
        with open(FILE_TO_SEND, "rb") as f:
            while (chunk := f.read(1024)):
                tls_socket.sendall(chunk)
        print("File sent successfully!")
