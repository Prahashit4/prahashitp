height = int(input("enter the height of the triangle:"))
n=input("symbol:")
for i in range(height+1):
    for j in range(i):
        print(n,end="")
    print('')
    
