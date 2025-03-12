file=open('sample.txt','r')
print(file.readline(10))
file.close()

file=open('sample.txt','r')
print(file.readline(5))
print(file.readline(15))
print(file.readline(25))
file.close()

file=open('sample.txt','r')
for line in file:
    print(line)
file.close()