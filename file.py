import os

f = open('try.txt', 'w')

f.write("We are here for the School meeting")
f.close()

# #open and read the file after the appending:
f = open("try.txt", "r")
print(f.read())