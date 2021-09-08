import socket
import io
import pandas as pd

#idea - pass dataframe as a string from the server and convert it back to dataframe in the client code.

c = socket.socket()
host = '127.0.0.1'
port = 5001

c.connect((host, port))
data_string = c.recv(1024).decode()

data = io.StringIO(data_string)
df = pd.read_csv(data, sep=" ",skipinitialspace = True)
df.reset_index(drop=True)

print("DataFrame:")
print(df)


print(df.dtypes)
print(df.columns)
print("Data Received from the server.Enter Function Code: ")

def view(df):
    df['Totalcost']= df['Quantity']*df['cost']
    print("DataFrame:")
    print(df)

def inser(df):
    dat = input()
    producid = input()
    quan = int(input())
    cos = int(input())
    totalcos = quan*cos
    new_row = {'Date':dat, 'productid':producid, 'Quantity':quan, 'cost':cos}
    #append row to the dataframe
    df = df.append(new_row, ignore_index=True)
    #df.loc[len(df.index)] = [dat,producid, quan,cos,totalcos]
    df['Totalcost']= df['Quantity']*df['cost']
    print(df)

def mod(df):
    df['Totalcost']= df['Quantity']*df['cost']
    print(df)

def upda(df):
    df['Totalcost']= df['Quantity']*df['cost']
    df['Category'] = ['A' if (x>=1 and x<=1000)  else 'B' for x in df['Totalcost']]
    print(df)

def ext(df):
    df['Totalcost']= df['Quantity']*df['cost']
    print("Enter Product ID to get details:")
    ind = int(input())
    print("Product Details: ")
    print(df.loc[df['productid']==ind])
    print("Enter Date  to get details:")
    ind = input()
    print("Product Details: ")
    print(df.loc[df['Date']==ind])



cp = input()
if(cp=='V'):
    view(df)
elif(cp=='M'):
    mod(df)
elif(cp=='I'):
    inser(df)
elif(cp=='U'):
    upda(df)
elif(cp=='F'):
    ext(df)


c.close()
