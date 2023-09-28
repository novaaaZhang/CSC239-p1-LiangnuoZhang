import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
server_address = (host, 31415) 
client_socket.connect(server_address)

try:
    # getthe initial ATM balance
    initial_balance = float(input("Enter the initial ATM balance: $"))
    
    # Send the initial balance to the server as an initial deposit
    client_socket.send(f"set_balance {initial_balance}".encode())
    
    while True:
        command = input("Enter a command (add [amount], subtract [amount], get_balance, or exit): ")

        if command == "exit":
            break

        client_socket.send(command.encode())

        response = client_socket.recv(1024).decode()
        print(response)


finally:
    client_socket.close()

