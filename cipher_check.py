import ssl
import socket
import sys

# Check if the target host is provided as a command-line argument
if len(sys.argv) < 2:
    print('Please provide the target host as a command-line argument.')
    sys.exit(1)

# Extract the target host from the command line
host = sys.argv[1]
port = 443

# Create a socket and wrap it with an SSL context
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_context = ssl.create_default_context()

# Set up the SSL context to only allow TLSv1.2 protocol
ssl_context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
ssl_sock = ssl_context.wrap_socket(sock, server_hostname=host)

try:
    # Connect to the remote host
    ssl_sock.connect((host, port))

    # Get the cipher information
    cipher = ssl_sock.cipher()
    print('Cipher: {}'.format(cipher[0]))

    # Print all available ciphers
    print('Available Ciphers:')
    for cipher in ssl_sock.get_ciphers():
        print(cipher['name'])

finally:
    # Close the connection
    ssl_sock.close()
