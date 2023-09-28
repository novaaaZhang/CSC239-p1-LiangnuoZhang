import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
server_address = (host, 31415)
server_socket.bind(server_address)
server_socket.listen(1)

print("ATM Server is ready to accept connections...")
balance = 0.0

while True:
    client_socket, client_address = server_socket.accept()

    try:
        print(f"Connection from {client_address}")

        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            # set initial
            if data.startswith("set_balance "):
                try:
                    initial_balance = float(data.split(" ")[1])
                    balance = initial_balance
                except ValueError:
                    client_socket.send("Invalid initial balance.".encode())

            # get current balance
            elif data == "get_balance":
                client_socket.send(f"ATM Balance: ${balance}".encode())

            # add money
            elif data.startswith("add "):
                try:
                    amount_to_add = float(data.split(" ")[1])
                    balance += amount_to_add  
                    client_socket.send("Money added successfully.".encode())
                except ValueError:
                    client_socket.send("Invalid amount.".encode())

            # subtract money
            elif data.startswith("subtract "):
                try:
                    amount_to_subtract = float(data.split(" ")[1])
                    balance -= amount_to_subtract
                    client_socket.send("Money subtracted successfully.".encode())
                except ValueError:
                    client_socket.send("Invalid amount.".encode())

            # exit program
            elif data == "exit":
                print(f"Connection from {client_address} closed.")
                break  

            else:
                client_socket.send("Invalid request".encode())

    except ConnectionError as e:
        print(f"Connection Error: {e}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()

