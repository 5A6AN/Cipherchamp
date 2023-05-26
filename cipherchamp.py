import ssl
import socket

# Prompt user for remote host
remote_host = input("Enter the remote host: ")

# Create a socket and establish a secure connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.create_default_context()

try:
    # Connect to the remote host using SSL/TLS
    with context.wrap_socket(sock, server_hostname=remote_host) as s:
        # Get the list of available ciphers
        ciphers = s.cipher()
        print("Available ciphers:")
        for cipher in ciphers:
            print(cipher)
except socket.gaierror as e:
    print(f"Error: {e}")
except ssl.SSLError as e:
    print(f"SSL Error: {e}")
finally:
    # Close the socket
    sock.close()
