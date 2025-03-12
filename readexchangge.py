file1=open('sample.txt','r')
file2=open('new.txt','w')

print(file1.readlines())

for line in file1.readlines():
    if not(line.startswith("Pushpa")):
        print(line)
        file2.write(line)

file1.close()
file2.close()