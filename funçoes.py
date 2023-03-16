import os
import yaml

def pesquisar(a):
    if 'pesquisar no youtube' in a:
        conteudo = a[20:]
        os.startfile('https://www.youtube.com/results?search_query='+conteudo)
    elif 'pesquisar' in a:
        a = a[9:]
        os.startfile('https://duckduckgo.com/?q='+a)
def abrir(a):
    data = yaml.safe_load(open('path.yml','r',encoding='utf-8').read())
    for Aplicativo in data['Aplicativos']:
        b = Aplicativo['Nome']
        c = Aplicativo['Caminho']
        if b in a:
            os.startfile(c)