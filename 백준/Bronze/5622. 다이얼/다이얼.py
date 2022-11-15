str_list = ["","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz","0"]

S = input().lower()
time = 0
for s in S:
    for i in range(len(str_list)):
        if s in str_list[i]:
            # print(i+1)
            time+=(i+1)

print(time)