s = 'abca'
seen = ' '
count = 0
for char in s: 
    if char not in seen:
        seen = seen+char
        count+=1
print(count)
print(seen)
print(len(seen))