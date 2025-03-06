import random
import os
import sys

alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
simbols = '@#$%&-+_!.'

while True:

    password = ''

    password_size = input('Digite a quantidade de caracteres da senha desejada (min: 8, máx:22)')

    try:
         password_size = int(password_size)
    except ValueError:
        
        os.system('cls')
        print('Você digitou alguma letra ou símbolo, tente novamente.')
        continue

    if password_size < 8 or password_size > 22:
        
        os.system('cls')
        print('Você digitou um tamanho inválido. Por favor digite um número entre 8 e 22')
        continue

    password_set = set()

    password_uppers_quantity = random.randint(1, password_size-2)

    uppers_counter = 1

    while uppers_counter <= password_uppers_quantity:
     
     letter = random.choice(alphabet_upper)

     if letter in password_set:
         
         continue
     
     uppers_counter += 1

     password_set.add(letter)

    if len(password_set) == password_size-2:

        simbols_quantity = 1
        password_set.add(random.choice(simbols))
        password_lowers_quantity = 1
        password_set.add(random.choice(alphabet_lower))

        os.system('cls')

        for l in password_set:

            password += l
        
        print(f'A senha gerada é: {password}')

        outra_operacao = input('Digite [R] para repetir ou qualquer outra tecla pra sair.').lower()

        if outra_operacao == 'r':

            os.system('cls')
            continue
        else:
            break
    
    password_lowers_quantity = random.randint(1,password_size-len(password_set)-1)

    lowers_counter = 1

    while lowers_counter <= password_lowers_quantity:

        letter = random.choice(alphabet_lower)

        if letter in password_set:

            continue

        lowers_counter += 1

        password_set.add(letter)

    if len(password_set) == password_size - 1:

        simbols_quantity = 1

        password_set.add(random.choice(simbols))

        for l in password_set:

            password += l
        
        print(f'A senha gerada é: {password}')

        outra_operacao = input('Digite [R] para repetir ou qualquer outra tecla pra sair.').lower()

        if outra_operacao == 'r':

            os.system('cls')
            continue
        else:
            break

    simbols_quantity = password_size-len(password_set)

    simbols_counter = 1

    while simbols_counter <= simbols_quantity:
        simbol = random.choice(simbols)
        
        if simbol in password_set:

            continue

        simbols_counter += 1

        password_set.add(simbol)
    
    os.system('cls')

    for l in password_set:

        password += l
    
    print(f'A senha gerada foi: {password}')

    outra_operacao = input('Digite [R] para realizar outra operação ou qualquer outra tecla para sair.').lower()

    if outra_operacao == 'r':
        os.system('cls')
        continue

    break

print('Obrigado por usar nosso gerador de senhas!')
sys.exit()

