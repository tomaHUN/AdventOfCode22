

def olvass():
    #file olvas
    myInput =[]
    try:
        myFile  = open('in.txt','rt')
        line = myFile.readline()
        while line != '':
            #listához adom és leszedem az újsor jeleket mert nem dolgoná fel
            myInput.append(line.rstrip('\n'))
            #print(line, end='')
            line = myFile.readline()
            
        myFile.close()
    except FileNotFoundError:  
        print("File not found")  
    return myInput