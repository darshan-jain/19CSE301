import socket
import pandas as pd
df  = pd.read_csv('/Users/darshan/PycharmProjects/socket/stationary.csv')
a = df.to_string(index=False)
s= socket.socket()
print("Socket Created")
s.bind(('127.0.0.1',5001))
s.listen(3)
print("Waiting for Connections")
while True:
    c,addr = s.accept()
    print("Connected with ", addr)
    c.send(bytes(a,'utf8'))

