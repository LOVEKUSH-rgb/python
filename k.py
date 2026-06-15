secret = 5
for i in range(1,11):
    if i == secret:
        print("found")
        break
else:
    print('not found')



found = False
secret = 67
for i in range(1,11):
    if i == secret:
        print('found')
        found = True
if not found:
    print('not found')