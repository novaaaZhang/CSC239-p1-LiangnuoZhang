# CSC239-p1-LiangnuoZhang

## Overview of Application
The code mainly simulates an ATM. It has three functions: get balance, add money, and subtract money. A client can connect to a server to perform basic banking operations. The server maintains an account balance, and the client can send commands to the server to interact with this balance.

## Client->Server Message Format

## Server->Client Message Format

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
Connection from ('127.0.0.1', 57641)  

## Acknowledgments
idea inspired by Allison in office hour.

## Client and Server Command Line Traces

