n= input("Enter the first string: ")
n2= input("Enter the second string: ")
n3= input("Enter the third string: ")
v=""
c=""
l=""
for i in range(len(n)):
    if(n[i]=='a'or n[i]=='e'or n[i]=='i'or n[i]=='o'or n[i]=='u'or n[i]=='A'or n[i]=='E'or n[i]=='I'or n[i]=='O'or n[i]=='U'):
        v=v+'$'
    else:
        v=v+n[i]
for i in range(len(n2)):
    if(n2[i]=='a'or n2[i]=='e'or n2[i]=='i'or n2[i]=='o'or n2[i]=='u'or n2[i]=='A'or n2[i]=='E'or n2[i]=='I'or n2[i]=='O'or n2[i]=='U'):
        c=c+n2[i]
    else:
        c=c+'*'
for i in range(len(n3)):
    if(n3[i].isupper()):
        l=l+n3[i].lower()
    else:
        l=l+n3[i]
print(v)
print(c)
print(l)