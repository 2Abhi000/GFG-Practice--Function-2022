#Python Functions (Sum of numbers) | Set 1
n=int(input("Testcases: "))
for i in range(n):
    t=list(map(int,input('Enter the value:').split()))
    print(sum(t))
