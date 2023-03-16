
import keyboard
import funçoes
while True:
    a = input('Digite algo:')
    if a == 'parar':
        break
    elif 'abrir' in a:
        funçoes.abrir(a)
    elif 'pesquisar' in a:
        funçoes.pesquisar(a)
    else:
        print('Entrada inválida')