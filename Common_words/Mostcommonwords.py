#read from file, create a dic and find the 10 most common word, and count them

fname = input("Enter file name: ")
try:
    fh=open(fname,'r')
except:
    print('Wrong file name. Insert a valid file name:')
    quit()

#type this if i want to open a file without the input option
#fh=open('words.txt','r')

dic=dict()
for line in fh:
    line=line.rstrip()
    words=line.split()
    for word in words:
        dic[word]=dic.get(word,0)+1
#print(dic)

lst=list()
for k,v in dic.items():
    newtup=(v,k)
    lst.append(newtup)
#print("flipped", lst)

lst=sorted(lst, reverse=True)
#print("sorted", lst[:10])

for v,k in lst[:10]:
    print(k,v)
