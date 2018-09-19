
import socket
import _thread                     

# create the socket and listen
s = socket.socket()          
port = 12345     
s.bind(('', port)) 
s.listen(5)  
  
def on_new_client(clientsocket,addr):
    while True:
        # msg = clientsocket.recv(1024) 
        #do some checks and if msg == someWeirdSignal: break:
        print(addr, ' >> ayy')
        msg = ('SERVER >> '.encode('utf-8')) 
        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        clientsocket.send(msg) 

    clientsocket.close()

# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   _thread.start_new_thread(on_new_client(c, addr))
   
c.close() 