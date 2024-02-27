import socket
import threading
import q3_data_processing

# Global variables
clients = []
lock = threading.Lock()

def handle_client(client_socket):
    while True:
        try:
            # Receive pickled message from client
            data = client_socket.recv(1024)
            if not data:
                break
            message = q3_data_processing.unpickle_message(data)

            # Broadcast message to all clients
            with lock:
                for c in clients:
                    c.send(q3_data_processing.pickle_message(message))
        except Exception as e:
            print(f"Error: {e}")
            break

    # If client disconnects, remove it from the clients list
    with lock:
        clients.remove(client_socket)
    client_socket.close()

def main():
    # Server setup
    host = '127.0.0.1'
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server started. Listening on port", port)

    # Accept client connections
    while True:
        client_socket, address = server_socket.accept()
        print("Connection from", address)

        # Add client socket to the list of clients
        with lock:
            clients.append(client_socket)

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
