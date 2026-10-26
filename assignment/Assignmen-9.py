#Write a program that opens a file and then reads the contents of the file. The
#program should then print out the contents of the file.
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()