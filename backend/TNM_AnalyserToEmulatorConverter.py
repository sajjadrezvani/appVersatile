import pandas as pd
import time,os

deskName = os.getlogin()
print("\nHello!   Welcome to TNM_AnalyserToEmulator_converter by SRK\n")
print("Warning: I use two column \"ID\" and \"Data\" to fill emulator, so you should have thease specific name for exel column :/ \n")

fileNameExel = input('Enter your exel file name located on your desktop:    ')
fileAddExel = 'C:\\Users\\' + deskName + '\\Desktop\\' + fileNameExel
fileNameSheet = input('Enter your exel sheet name:   ')

mypanda = pd.read_excel(fileAddExel , sheet_name=fileNameSheet ,engine='openpyxl')
print(mypanda.head(),'\n')

print(' Waiting...\n        ....\n        .....\n')

fileNameTxt = 'C:\\Users\\' + deskName + '\\Desktop\\output' + fileNameExel[:-5] + '.txt' 
txtFile = open(fileNameTxt, 'w')
txtFile .write('1\n14\n')

colID ='ID' 
colData ='Data'
txtFile.write( str(mypanda.loc[1,colID]) +'\n')
txtFile.write( str(mypanda.loc[2,colID]) +'\n')
txtFile.write('1\n1\n2000\n10\n7\n0\n0\n0\n')

for i in range(mypanda.shape[0]):
    cell = str(mypanda.loc[i,colData])
    cell = '0X' + cell[:-1]
    output = cell.replace(' ',',0X')
    txtFile.write( output + '}\n')

print(mypanda.info(),'\n')
print(mypanda.describe(),'\n\n')

print('Have a nice day! See you soon :)) ')

while(1):
    1