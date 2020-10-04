from socket import *
import ssl
import base64

def smtp_client(port=1065, mailserver='127.0.0.1'):
    msg = b"\r\n I love computer networking!."
    endmsg = b"\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = "smtp.gmail.com"
    serverPort = 465

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((mailserver, serverPort))
    clientSocketSSL = ssl.wrap_socket(clientSocket)
    # Fill in end
    recv = clientSocketSSL.recv(1024).decode()
    #print(recv)
    #if recv[:3] != "220":
        #print("220 reply not received from server.")


    #print("helo")
    # Send HELO command and print server response.
    heloCommand = b"HELO Kathy\r\n"
    clientSocketSSL.send(heloCommand)
    recv1 = clientSocketSSL.recv(1024).decode()
    #print(recv1)
    #if recv[:3] != "250":
        #print("250 reply not received from server.")

  
    username = "kathyy.chingg@gmail.com"
    password = "XXXXXXXX"
    base64Authcredentials = ("\x00"+username+"\x00"+password).encode()
    base64Authcredentials = base64.b64encode(base64Authcredentials)
    authMessage = "AUTH PLAIN ".encode()+base64Authcredentials+'\r\n'.encode()
    clientSocketSSL.send(authMessage)
    recv2 = clientSocketSSL.recv(1024).decode()
    #print(recv2)
    #if recv2[:3] != "250":
        #print("250 reply not received from server.")



    #print('rev2')
    #print("MAIL")
    # Send MAIL FROM command and print server response.
    mailFrom = b"MAIL FROM:<kathyy.chingg@gmail.com>\r\n"
    clientSocketSSL.send(mailFrom)
    recv3 = clientSocketSSL.recv(1024).decode()
    #print (recv3)
    #if recv3[:3] != "250":
        #print("250 reply not received from server.")


    #print("RCPT")
    # Send RCPT TO command and print server response.
    rcptTo = b"RCPT TO:<kc3191@nyu.edu>\r\n"
    clientSocketSSL.send(rcptTo)
    recv4 = clientSocketSSL.recv(1024).decode()
    #print("After RCPT TO command: "+recv3)
    #if recv4[:3] != "250":
        #print ("250 reply not received from server.")

    #print("DATA")
    # Send DATA command and print server response.
    data = b"DATA\r\n"
    clientSocketSSL.send(data)
    recv5 = clientSocketSSL.recv(1024).decode()
    #print("After DATA command: "+recv5)
    #if recv5[:3] != "250":
        #print ("250 reply not received from server.")

    # Send message data.
    clientSocketSSL.send(msg)

    # Message ends with a single period.
    clientSocketSSL.send(endmsg)

    # Send QUIT command and get server response.
    #print('reached the end')
    quit = b"QUIT\r\n"
    clientSocketSSL.send(quit)
    recv6 = clientSocketSSL.recv(1024).decode()
    #print(recv6)
    #if recv6[:3] != "250":
        #print ("250 reply not received from server.")
    #print('end')
    clientSocketSSL.close()
    #print('closed')


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
