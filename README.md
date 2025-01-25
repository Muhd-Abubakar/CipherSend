# Secure File Transfer Using TLS Protocol

This project implements a secure file transfer mechanism using the Transport Layer Security (TLS) protocol. The system enables secure communication between a client and a server, ensuring confidentiality, integrity, and authentication of the data being transferred.

---

## **Features**
- **End-to-End Encryption**: Secure file transfer using TLS.
- **Data Integrity Verification**: Ensures the transferred file is not tampered with.
- **Modular Design**: Easy to adapt for different environments.
- **Support for Multiple File Types**: Transfer various file formats securely.

---

## **Project Structure**
SecureFileTransfer/
├── client.py          # Client-side implementation
├── server.py          # Server-side implementation
├── README.md          # Project documentation
├── requirements.txt   # Python dependencies (if any)
└── .gitignore         # Excludes sensitive files

---

## **How to Set Up**

### **1. Requirements**
- Python 3.8 or higher
- Libraries: `socket`, `ssl`

Cloning the Repo
```bash
git clone https://github.com/Muhd-Abubakar/CipherSend.git
```
2. **Generating Certificates**
To create the server.key and server.crt files required for TLS, follow these steps:

Generate a Private Key:

```bash

openssl genrsa -out server.key 2048
```
This creates a 2048-bit RSA private key.

Generate a Certificate Signing Request (CSR):

```bash

openssl req -new -key server.key -out server.csr
```
During this step, you will be prompted to enter information like country, state, and organization.

Generate a Self-Signed Certificate:

```bash
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```
This will create a certificate (server.crt) valid for 1 year.

Place the server.key and server.crt in the appropriate directory as configured in the code.

3. **Running the Project**
Start the Server
Run the server to listen for client requests:

```bash
python server.py
```
Start the Client
Run the client to connect and transfer files:

```bash
python client.py
```
