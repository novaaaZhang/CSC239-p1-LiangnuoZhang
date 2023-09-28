# CSC239-p1-LiangnuoZhang

## Overview of Application
The code mainly simulates an ATM. It has three functions: get balance, add money, and subtract money. A client can connect to a server to perform basic banking operations. The server maintains an account balance, and the client can send commands to the server to interact with this balance.

## Client->Server Message Format
Set Initial Balance: set_balance [amount]  
Add Money: add [amount]  
Subtract Money: subtract [amount]  
Get Balance: get_balance  
Exit: exit  

## Server->Client Message Format
Success Response: [Operation] successfully.  
Error Response：Invalid amount.  
Current Balance Response: ATM Balance: $[balance]  
Invalid Request Response: Invalid request


## Example Output
- Client:
Enter the initial ATM balance: $200  
Enter a command (add [amount], subtract [amount], get_balance, or exit): add 20  
Money added successfully.  
Enter a command (add [amount], subtract [amount], get_balance, or exit): subtract 30  
Money subtracted successfully.  
Enter a command (add [amount], subtract [amount], get_balance, or exit): get_balance  
ATM Balance: $190.0  
Enter a command (add [amount], subtract [amount], get_balance, or exit): exit  

- Server:
ATM Server is ready to accept connections...  
Connection from ('127.0.0.1', 12345)
Connection from ('127.0.0.1', 31542)
Connection from ('127.0.0.1', 51324)
Connection from ('127.0.0.1', 42413)

## Acknowledgments
idea inspired by Allison in office hour.

## Client and Server Command Line Traces (for the example output)
- Client:
% python3 atm_client.py  
client starting - connecting to math server at IP 127.0.0.1 and port 31415  
sets the initial ATM balance to $200 using the "set_balance" command and receives a success message.  
adds $20 to the balance using the "add" command and receives a success message.  
subtracts $30 from the balance using the "subtract" command and receives a success message.  
requests the current balance again and receives the updated balance, which is now $190.  
exits the session using the "exit" command.  

- Server:
% python3 atm_server.py  
server starting - listening for connections at IP 127.0.0.1 and port 31415  
connected established with ('127.0.0.1', 57641)  
The server receives and processes various client requests:  
Set initial balance  
Get balance  
Adding money  
Subtracting money  
Exiting the session  
The server closes the connection when a client exits the session.  


