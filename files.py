file1 = open("myfile.txt","w")
print("output of read function is ")
data = file1.read()
print(data)
print()

file2= open("Blank.txt","w")
str1 = 'python'
file2.write(str1)
print()


file3 = open("Hw.txt", "r+")
print(file3.readline(11))
print()            
