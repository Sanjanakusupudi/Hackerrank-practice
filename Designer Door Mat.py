n,m = map(int, input().split(" "))

strg = ".|."

i=0
for i in range(n):
    if (i<(n-1)/2):
        print(str((strg)*(2*i+1)).center(m,"-"))
    elif(i==(n-1)/2):
        print("WELCOME".center(m,"-"))
    else:
        print(str((strg)*((n-i)*2-1)).center(m,"-"))
