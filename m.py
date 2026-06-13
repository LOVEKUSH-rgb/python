an_letters = "afdfdjADJKJFfkjjj"

word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

for c in word:
    if c in an_letters:
        print(f'Give me an {c}: {c}')
    else:
        print(f'Give me a {c}: {c}')
print("What's that spell?")
for i in range(times):
    print(f'{word} !!!')
