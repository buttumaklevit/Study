A = input().lower()
cro_list = ["dz=","c=","c-","d-","lj","nj","s=","z="]

for cro in cro_list:
    if cro in A:
        A=A.replace(cro, "*")
print(len(A))