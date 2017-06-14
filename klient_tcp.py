#!/usr/bin/env python
import socket
import base64

def base64_to_text(text):
    try:
        return str(base64.b64decode(text))
    except:
        return str(base64.b64decode(text).decode('utf-8'))


def text_to_base64(text):
    print 'otrzymalem tekst do zakodowania:' + text
    try:
        return str(base64.b64encode(bytes(text)))
    except:
        return str(base64.b64encode(text.encode()))

def sendAndGetAnswer(msg):
    sock.sendall(msg + '')
    answer = sock.recv(1024)
    return answer

def getMsgCode(answer):
    return answer.split()[0]

def sendRecvPrint(sock, tag, text):
    sock.sendall(tag + " " +text+'\r\n')
    reply = sock.recv(2048)
    print('### poczatek wiadomosci ###')
    print(reply)
    print('### koniec wiadomosci ###')

globvar = 0

def randomTag():
    global globvar
    globvar += 1
    return "T" + str(globvar)





#HOST = socket.gethostbyname('interia.pl')
HOST = '212.182.24.27'
PORT = 143
server_address = (HOST, PORT)

# TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(server_address)

try:
    # TCP
    #sock.send("TEXT")


    # TCP
    answer = sock.recv(1024)
    print('answer: '+ answer)
    sendRecvPrint(sock,randomTag(),"LOGIN pasinf2017@infumcs.edu P4SInf2017")

    # sendRecvPrint(sock, randomTag(), "CREATE kkkk20176 ")
    sendRecvPrint(sock, randomTag(), "DELETE kkkk20176")
    # sendRecvPrint(sock,randomTag(),"SELECT Inbox")
    # sendRecvPrint(sock,randomTag(),"FETCH 5 BODY[text]")
    # sendRecvPrint(sock,randomTag(),"CLOSE")
    # sendRecvPrint(sock,randomTag(),"LOGOUT")



    print "###########koniec##########"

except socket.error, e:
    print e

sock.close()

