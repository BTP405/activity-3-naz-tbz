import socket
import q1_data_processing

def send_file(server_address, file_path):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server_address)
        
        # Pickle the file and send it to the server
        q1_data_processing.pickle_data(file_path, 'pickled_file.pickle')
        with open('pickled_file.pickle', 'rb') as f:
            pickled_data = f.read()
        
        client_socket.sendall(pickled_data)
        
        print("File sent successfully.")
    
    except (socket.error, ConnectionError) as e:
        print("Socket or connection error:", e)
    
    except Exception as e:
        print("Error sending file:", e)    
    
    finally:
        client_socket.close()

if __name__ == "__main__":
    server_address = ('localhost', 12345)  # Server address
    file_path = 'file_to_send.txt'  # Path of the file to be sent
    send_file(server_address, file_path)
