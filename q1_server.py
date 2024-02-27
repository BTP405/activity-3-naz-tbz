import socket
import os

def receive_file(client_socket, save_directory):
    try:
        # Receive pickled file object
        pickled_file = client_socket.recv(4096)
        if not pickled_file:
            print("No data received from client.")
            return
        
        # Save the received pickled file directly
        save_path = os.path.join(save_directory, 'received_file.pickle')
        with open(save_path, 'wb') as f:
            f.write(pickled_file)
        print("File saved to:", save_path)
    
    except Exception as e:
        print("Error receiving file:", e)


def run_server(save_directory):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    
    try:
        server_socket.bind(server_address)
        server_socket.listen(1)
        print("Server is listening for incoming connections...")
        
        while True:
            client_socket, client_address = server_socket.accept()
            print("Connected to:", client_address)
            
            receive_file(client_socket, save_directory)
            
            client_socket.close()
    
    except Exception as e:
        print("Server error:", e)
    
    finally:
        server_socket.close()

if __name__ == "__main__":
    save_directory = 'received_files'  # Specify the directory where received files will be saved
    run_server(save_directory)
