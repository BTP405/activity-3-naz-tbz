import socket
import threading
import q3_data_processing

def receive_messages(client_socket):
    while True:
        try:
            # Receive pickled message from server
            data = client_socket.recv(1024)
            if not data:
                break
            message = q3_data_processing.unpickle_message(data)
            
            print(message)
        except Exception as e:
            print(f"Error: {e}")
            break

def send_message(client_socket):
    while True:
        message = input()
        client_socket.send(q3_data_processing.pickle_message(message))

def main():
    # Client setup
    host = '127.0.0.1'
    port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Start a thread to send messages to the server
    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    send_thread.start()

    # Join threads
    receive_thread.join()
    send_thread.join()

    client_socket.close()

if __name__ == "__main__":
    main()
