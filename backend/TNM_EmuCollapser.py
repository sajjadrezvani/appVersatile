import os , time 
print("Hi! welcome to TNM emulator collapser by Sajjad Rezvani.K ... \n   watting...   \n   ....\n   .....\n\n")
deskname=os.getlogin()
txt_name= input('Enter your txt file name on Desktop:    ')
#filename1='D:\\emulator.txt'
filename1='C:\\Users\\'+deskname+'\\Desktop\\'+txt_name
file1= open(filename1,'r')
result=file1.read()
file1.close()
result=result+"\n"
#filename2='D:\\SR_result.txt'
filename2='C:\\Users\\'+deskname+'\\Desktop\\SR_result.txt'
file2 = open(filename2,'w')



while len(result)!=0:
    file1= open(filename1,'r')
    line=file1.readline()
    file2.write(line)
    file1.close()

    if line!="0x7f,0x22,0x31}\n" :
    
        nextEnter=result.find("\n",0)
        while result.find(line)==0:
            result=result[nextEnter+1::]  
            if len(result)==0:
                break

        start= 0

        while(result.find(line,start)!=-1 and result[result.find(line,start)-1]=="\n"):
            lastChr=result.find(line,start)-1
            if result[lastChr]=="\n":
                nextEnter=result.find("\n",lastChr+1)
                result=result[0:lastChr+1:]+result[nextEnter+1::]
            start=0


#   result=result.replace(line,'')
    elif line=="0x7f,0x22,0x31}\n" :
        while result.find(line)==0:
            result=result[16::]  

    file1=open(filename1,'w')
    file1.write(result)
    file1.close()

file2.close()
os.remove(filename1)
print("\ngood luck! enjoy of it... ")
time.sleep(5)

