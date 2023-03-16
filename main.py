
import keyboard
import funçoes
import searchapp
print('§§§§§LAB a3§§§§§')
while True:
    a = input('Digite algo:')
    if 'sair' in a:
        break
    elif 'adicionar' in a:
        searchapp.adicionar()
    else:
        funçoes.abrir(a)
        funçoes.pesquisar(a)
