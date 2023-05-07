import socket
import os

def create_response(filename):
    try:
        with open(filename, 'rb') as file:
            content = file.read()
            response_header = 'HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length:{}\n\n'.format(len(content))
            response = response_header.encode() + content
    except FileNotFoundError:
        response = b'HTTP/1.1 404 Not Found\n\n404 Not Found'
    return response

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(1)
    print('Server is listening on port 8000')
    while True:
        client_socket, client_address = server_socket.accept()
        print('Client connected from:', client_address)
        request = client_socket.recv(1024).decode()
        filename = request.split()[1][1:]
        if not filename:
            filename = 'index.html'
        response = create_response(filename)
        client_socket.sendall(response)
        client_socket.close()

start_server()
