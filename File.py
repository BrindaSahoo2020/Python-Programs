#File Handling in Python

#Sample Output
#['Programming is fun,\n', 'if you wanna make your work fun:\n', '    use Python!']

file1= '''Programming is fun,
if you wanna make your work fun:
    use Python!'''
f = open("file1.txt","w")
f.write(file1)
f.close()

fi = open("file1.txt","r")
while True:
	line = fi.readlines()
	if len(line) == 0:
		break
	print(line)
fi.close()

#NOTE
'''file1.txt will be created with below text:
Programming is fun,
if you wanna make your work fun:
    use Python!
'''