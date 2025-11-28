SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

"""Wrote this code using the algorithm in a book called BigBookSmallPythonProjects."""
print('\nOriginally written by AL Sweigart.')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B is encrypted into D, and so on.')
print()

while True:
    print('Do you want to (e)ncrypt ot (d)ecrypt?')
    response = input("> ").lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')
    
while True:
    maxKey = len(SYMBOLS) - 1
    print(f'Please enter the key (0 to {maxKey}) to use.')
    response = input('> ')
    if not response.isdecimal():
        continue
    
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break
    
print(f'Enter the message to {mode}. ')
message = input("> ")

message = message.upper()

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
            
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
            
        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol
        
print(translated)