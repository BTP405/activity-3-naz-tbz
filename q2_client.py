import socket
import pickle
from q2_task import Task

def send_task(host, port, task):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        serialized_task = pickle.dumps(task)
        client_socket.send(serialized_task)
        print("Task sent to server.")
        client_socket.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    task = Task("print", ["Hello, world!"])
    send_task('127.0.0.1', 5555, task)
