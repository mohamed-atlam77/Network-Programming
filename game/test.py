# [1] send button
msg = Entry(Frame3)
msg.pack(side="left",expand=1,fill="both")
def sendButton():
     global username 
     message = msg.get()
     finMessage =username + "-> " + message
     sock.send(message.encode())
     chat.insert(END,finMessage)
     chat.insert(END,"\n")
     msg.delete(0, END)
send = Button(Frame3,text="send",bg="Aqua", fg="Black",width=2,height=1,font=('courier','12'),command=sendButton )#connect)
send.pack(side="left",expand=1,fill="x")

# ########################################################################
# [2] send function
def send(message):
     while True:
        s.send(message.encode('utf-8'))
##########################################################################
# [3] send function
def send():
    while True:
        s.send(input('sender :').encode(utf-8))
##########################################################################
# [4] recive function
def recive():
    while True:
        data = s.recv(1024)
        print(data.decode('utf-8'))
##########################################################################
# [5]define connect method
server = Entry(Frame1)
server.insert(0,'127.0.0.1')
portt = Entry(Frame1)
portt.insert(0,'12221')
def connect():                                   
    global username
    host = server.get()
    temp = portt.get()
    username = user.get()
    port = int(temp)
    sock.connect((host, port))
    # start_new_thread(recievingMSG, (sock,))
    start_new_thread(recievingMSG,(sock,))
connect = Button(Frame1,text="Connect",command=connect )#connect)
connect.grid(row=3,column=1)
# ##########################################################################
# [6] recive thread
import _thread
def recive(s):
    while True:
        data = s.recv(1024)
        print(data.decode('utf-8'))
start_new_thread(recive,(s,))
# ###########################################################################
# [7] recive MSG
chat = Text(Frame2)
chat.pack(side="left")
def recievingMSG(sock):
    while True:
        recievedMsg = sock.recv(1024).decode()
        finrecievedMsg = recievedMsg + "\n"
        chat.insert(END,finrecievedMsg)
# ###########################################################################
# [8] send thread
import _thread
def send(s):
    while True:
        s.send(input('sender :').encode(utf-8))
start_new_thread(send,(sock,))
#############################################################################
# [9] create socket
client_socket=socket(AF_INET,SOCK_STREAM)


# 10
# Function to handle clients'connections
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8')) 
            aliases.remove(alias)
            break