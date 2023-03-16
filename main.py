
import keyboard
import funçoes
print('§§§§§LAB a1§§§§§')
while True:
    a = input('Digite algo:')
    if 'sair' in a:
        break
    funçoes.abrir(a)
    funçoes.pesquisar(a)