import socket
import pickle
from multiprocessing import Process

# Worker function
def process_task(task):
    try:
        # Execute the task
        result = task.execute()
        return result
    except Exception as e:
        print(f"Error processing task: {e}")
        return None

# Worker process function
def handle_client(client_socket):
    try:
        # Receive serialized task from client
        data = client_socket.recv(1024)
        task = pickle.loads(data)
        print("Task received from client.")

        # Process the task
        result = process_task(task)

        # Send the result back to client
        serialized_result = pickle.dumps(result)
        client_socket.send(serialized_result)
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

# Server setup
def main():
    host = '127.0.0.1'
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server started. Listening on port", port)

    # Accept client connections and handle each client in a separate process
    while True:
        client_socket, address = server_socket.accept()
        print("Connection from", address)

        client_process = Process(target=handle_client, args=(client_socket,))
        client_process.start()

if __name__ == "__main__":
    main()
