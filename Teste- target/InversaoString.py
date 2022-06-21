'5- Inversão string: '

str = input("Digite uma palavra ou frase: ").lower()

print(f'String original: {str}')
print(f'String invertida: ', end='')

for i in range(len(str)-1, -1, -1):
    print(str[i], end='')
