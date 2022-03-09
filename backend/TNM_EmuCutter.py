import os , time 
print("Hi! welcome to TNM emulator cutter by Sajjad Rezvani.K ... \n   watting...   \n   ....\n   .....\n\n")
deskname=os.getlogin()
txt_name= input('Enter your txt file name on Desktop:    ')

#filename1='D:\\emulator.txt'
filename1='C:\\Users\\'+deskname+'\\Desktop\\'+txt_name
file1= open(filename1,'r')
oneLine=file1.readline()

filename2='C:\\Users\\'+deskname+'\\Desktop\\SR_result.txt'
file2 = open(filename2,'w')

while oneLine:
    index = oneLine.find('}')
    if index==-1 : 
        index= len(oneLine)-2
        print(index)
    oneLine= oneLine[:index+1]
    file2.write(oneLine+'\n')
    oneLine=file1.readline()

file1.close()
file2.close()
os.remove(filename1)
print("\ngood luck! enjoy of it... ")
time.sleep(10)
