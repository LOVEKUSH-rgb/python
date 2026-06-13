s = "demo loops - fruit loops"
for index in range(len(s)):
    if s[index] == 'i' and s[index] == 'u':
        print("there is an i or u")


for char in s:
    if char== 'i' or char == 'u':
        print("there is an i or u")



for d in s:
    if d in 'iu':
        print("there is an i or u") 