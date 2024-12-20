from SRC.Database import helper

def createtable():
    num = helper.inputdata()
    for n in range(1,11):
        print(f"{num} * {n} = {num*n}")