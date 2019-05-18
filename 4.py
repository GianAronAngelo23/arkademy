n=int(input("Masukkan Angka Ganjil:"))

for i in range(0,n):
    for j in range(0,n):
        if(i==j or j==n-1-i):
            print("x",end=" ")
        else:
            print("=",end=" ")
    print()