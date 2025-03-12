file1=open('sample.txt','r')
file2=open('new.txt','w')

count=file1.readlines()
type(count)
for i in range(1,len(count)+1):
    if(i%2==0):
        file2.write(count[i-1])
    else:
        pass


file2.close()

file2=open('new.txt','r')
count1=file2.read()
print(count1)
file1.close()
file2.close()
