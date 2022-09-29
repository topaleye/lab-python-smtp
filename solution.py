from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google Mail server) if you want to verify the script beyond GradeScope
    #mailserver = (mailserver, 25)
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.connect((mailserver,port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    # print(recv) #You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #     print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #     print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFromCommand = "MAIL FROM: <to652@nyu.edu>\r\n"
    clientSocket.send(mailFromCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #     print('250 FROM reply not received from server.')
    # else:
    #     print('MAIL FROM received.')

    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    mailTOcommand = "RCPT TO: <to652@nyu.edu>\r\n"
    clientSocket.send(mailTOcommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #     print('250 reply not received from server.')
    # else:
    #     print('MAIL RCPT TO FROM received.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    mailDATACommand = b"DATA\r\n"
    clientSocket.send(mailDATACommand)
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #     print('250 DATA reply not received from server.')
    # else:
    #     print('MAIL DATA received.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(("To: to652@nyu.edu").encode())
    clientSocket.send(("From: to652@nyu.edu").encode())
    clientSocket.send(("Subject: Hello World").encode())
    clientSocket.send((msg).encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())

    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    mailQUITCommand = "QUIT\r\n"
    clientSocket.send(mailQUITCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #     print('250 QUIT reply not received from server.')
    # Fill in end
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')