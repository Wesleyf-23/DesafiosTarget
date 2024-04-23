n = int(input("Digite o termo de fibonacci:"))

termo2=1
termo3=1
termo =0

if (n==1) or (n==2):
    print("1")
else:

    for cont in range(2,n):

        termo = termo2 + termo3
        termo3 = termo2
        termo2 = termo
        cont += 1

print(f"{termo}")