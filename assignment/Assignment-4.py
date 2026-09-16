# Imagine you have a secret message hidden in a regular sentence. This program is
# like a decoder ring! It will ask you for the secret message (substring) and the coded message (string). Build
# a program which will tell you if the secret message can be found hidden inside the coded message or not.

secret_message = input("Enter a string: ")
coded_message = input("enter a coded message: ")

if coded_message in secret_message:
    print("Found")
else:
    print("Not Found")