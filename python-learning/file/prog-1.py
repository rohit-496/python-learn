'''
a = " a very long string with emails"

emails = []
'''
# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()
'''
f = open("file.txt")
lines = f.readlines()
print(lines)
f.close()
'''
# f = open("file.txt")
# line1 = f.readline()
# print(line1)
# line1 = f.readline()
# print(line1)
# f.close


with open("file/file.txt") as  f :
    f.readline()
    #you dont have to close the file explicitly using with statement
