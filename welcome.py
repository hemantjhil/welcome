# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
s=".|."
s1="-"
s2="WELCOME"
k=(int)((m-1)/2)
for i in range((int)((n-1)/2)):
    for j in range(k-((3*i)+1)):
        print(s1,end='')
    for j in range(2*i+1):
        print(s,end='')
    for j in range(k-((3*i)+1)):
        print(s1,end='')
    print(" ")
for i in range((int)((m/2-3))):
    print(s1,end='')
print("WELCOME",end='')
for i in range((int)((m/2-3))):
    print(s1,end='')
print(" ")
for i in range((int)((n-1)/2)):
    for j in range(3*(i+1)):
        print(s1,end='')
    for j in range(n-(2*(i+1))):
        print(s,end='')
    for j in range(3*(i+1)):
        print(s1,end='')
    print(" ")
