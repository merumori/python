print('Enter the file hendlig number ')
#print('1.create the file')
print('1.write the file')
print('2.read the file')
print('3.append the file')
print('4.exite the file')
num=int(input("enter the number"))
if(num==1):
	f=open("mori.txt","w")
	f.write("hello student....")
	f.close()
elif(num==2):
	f=open("mori.txt","r")
	file=f.read()
	print(file)
	f.close()
elif(num==3):
	f=open("mori.txt","a")
	f.write("mca student....")
	f.close()
elif(num==4):
	print("exite the file")
else:
	print("invelid number")

#Open the file in a Binary mode
f1=open('Python Syllabus_Pg1.png','rb')
f2=open('syllabus.png','wb')
#Read bytes from f1 and write it to f2
bytes=f1.read()
f2.write(bytes)
#Close the files
f1.close()
f2.close()



