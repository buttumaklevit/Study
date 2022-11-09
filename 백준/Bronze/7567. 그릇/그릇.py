Bo = input()
check = Bo[0] ; height = 0
for B in Bo:
    if height == 0 and B:
        height += 10
    elif check == B:
        height += 5
    elif check != B:
        height += 10
        check = B
print(height)