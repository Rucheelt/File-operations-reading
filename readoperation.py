file=open('sample.txt','r')
print(file.read())
file.close()

file=open('sample.txt','r')#reading in parts , by specifying characters
print(file.read(500))
file.close()

file=open('sample.text','a')
file.write("So this was the story of pushpa described in brief")
file.close()