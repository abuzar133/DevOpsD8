#open file in read mode
#open return a file object,which has a read method for reading the content of the file
file = open("examaple.txt", 'r')
content = file.read()
print(content)
file.close()

#with statement opens the file , does the operation and closes the file automatically
with open("examaple.txt",'r') as file:
    content= file.read() #stores the content as a string
    print(content)
    print(type(content))

with open("examaple.txt", 'r')as file:
    for line in file: #reads the line by line
        print(line.strip())

with open("examaple.txt",'r') as file :
    lines = file.readlines() #stores the content as a list of strings
    print(lines)
    print(type(lines))


print("***************************************Exception handling***************************")

try:
    with open("examaple.txt", 'r') as file:
        lines = file.readlines()  # stores the content as a list of strings
        print(lines)
        print(type(lines))
except filenotfound as e :
    print("file not found")
except Exception as e:
    print("some error occured")

#write mode
with open("test.txt",'w')as file:
    file.write("this is a test file")

#write mode will overwrite the content of the file
with open("test.txt",'r')as infile,open("test.txt",'w')as outfile:
    for line in infile:
        outfile.write(line)

#this is append mode which will append the comtent of the file
with open("test.txt",'a')as file:
    file.write("\nThis is a test file")
