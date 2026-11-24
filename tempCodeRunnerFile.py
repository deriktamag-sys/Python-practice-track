
f= open("sample.txt","r+")
f.write("Hey there newbie!! \n Wanna play some ML,,,,,")
f.close()
f =open("sample.txt", "r")
print(f.read())
f.close()