# f = open("demo.txt","r")
# # data = f.read()
# # print(data)
# # print(type(data))

# # line1 = f.readline()
# # print(line1)

# # line2 = f.readline()
# # print(line2)
# f.close()

# f = open("demo.txt","a")
# f.write("I want to play guitar")
# f.close()

# f =open("demo.txt","r")
# print(f.read())
# f.close()

# f= open("sample.txt","r+")
# f.write("Hey there newbie!! \n Wanna play some ML,,,,,")
# f.seek(0)##moves cursor to the beginning.
# print(f.read())
# f.close()

# f= open("sample.txt","r+")
# f.write("Hey there newbie!! \n Wanna play some ML,,,,,")
# f.close()
# f =open("sample.txt", "r")
# print(f.read())
# # f.close()

# import os
# os.remove("sample.txt")  #deletes the file

# f = open("practice.txt", "r+")
# f.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like Programming in Java")
# f.seek(0)
# print(f.read())
# f.close()

# #replaces the Java word with the python..
# f = open("practice.txt","r")
# data = f.read()
# new_data = data.replace("Java","Python")
# print(new_data)

# ##finds the word learning in the text file
# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")
    
#find the word and finds the first line it occurs.

def check_for_line():
    word="learning"
    line = 1
    data =True
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line)
            line+=1
check_for_line()