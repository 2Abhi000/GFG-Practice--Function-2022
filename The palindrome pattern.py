#The Palindrome Pattern
row=int(input("Row: "))
col=int(input("Col: "))
a=[[int(input("Value: ")) for i in range(row)] for i in range(col)]
def palin(mat):
    d={}
    ar=[]
    for i in range(len(mat)):
        re=list(reversed(mat[i]))
        if re==mat[i]:
            d[i]=('R',re)
    
    for i in range(len(mat)):
        k=[]
        for j in range(len(mat)):
            k.append(mat[j][i])
        ar.append(k)
    for i in range(len(ar)):
        rev=list(reversed(ar[i]))
        if rev==ar[i]:
            d[i]=('C',rev)
    
    for i in d:
        if 'R' in d[i]:
            print(i,d[i][0])
            break
        elif 'C' in d[i]:
            print(i,d[i][0])
            break
ans=palin(a)
