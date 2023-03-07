import re
import json

def parser(file):
    dic = []
    exp = re.compile(r"(?P<Dir>\d+)::(?P<Ano>\d{4})-(?P<Mes>\d{2})-(?P<Dia>\d{2})::(?P<Nome>[a-zA-Z ]+)::(?P<Pai>[a-zA-Z ]+)::(?P<Mae>[a-zA-Z ]+)::(?P<Obs>(\s*.*\s*)*)::")
    f = open(file, 'r')
    for line in f:
        match = exp.finditer(line)
        for m in match:
            if match:
                dic = dic + [m.groupdict()]
    return dic

def freq_ano(dic):
    dicanos = {}

    for d in dic:
        if d['Ano'] in dicanos:
            dicanos[d['Ano']] += 1
        else:
            dicanos[d['Ano']] = 1

    dicanos_ordenado = sorted(dicanos.items(), key = lambda x: x[1], reverse=True)
    print(dicanos_ordenado)
    
    return dicanos 

def nomes_apelidos(dic,seculo):
    nomes = {}
    apelidos = {}
    
    regex_nome = re.compile(r'^\w+')
    regex_apelido = re.compile(r'\w+$')
    
    
    for d in dic:

        nome = regex_nome.search(d['Nome']).group()
        apelido = regex_apelido.search(d['Nome']).group()

        if int(d['Ano']) // 100 + 1 == seculo:
            if nome not in nomes:
                nomes[nome] = 1
            nomes[nome] += 1
            if apelido not in apelidos:
                apelidos[apelido] = 1
            apelidos[apelido] += 1

    nomes_ordenados = sorted(nomes.items(), key=lambda x: x[1], reverse=True)[:5]
    apelidos_ordenados = sorted(apelidos.items(), key=lambda x: x[1], reverse=True)[:5]
    print(nomes_ordenados)
    print(apelidos_ordenados)


def freq_relações(dic):
    relações = dict()
    exp = re.compile(r"[a-zA-Z ]*,([a-zA-Z\s]*)\.[ ]*Proc\.\d+\.")

    for d in dic:
        matches = exp.finditer(d['Obs'])
        for match in matches:
            if match.group(1) not in relações:
                relações[match.group(1)] = 0
            relações[match.group(1)] += 1

    #relações_ord = sorted(relações.items(), key = lambda x: x[1], reverse=True)
    #print(relações_ord)
    print(relações)
    return relações

def convert_json(dic, path):
    file = open(path, "w")
    json.dump(dic[:20], file, indent=4)
    

def main():

    #eliminar linhas repetidas
    with open('processos.txt', 'r') as f:
        linhas = f.readlines()

    linhas_unicas = set(linhas)

    with open('processos.txt', 'w') as f:
        for linha in linhas_unicas:
            f.write(linha)

    #parse do ficheiro processos.txt
    dic = parser("processos.txt")

    print("Opções disponíveis:")
    print("1- Frequência de processos por ano")
    print("2- Frequência de nomes próprios e apelidos")
    print("3- Frequência dos vários tipos de relação")
    print("4- Converter os 20 primeiros registos num novo ficheiro em formato Json")

    num = int(input("Escolha uma opção: "))

    if num==1:
        dic_anos = freq_ano(dic)
    elif num==2:
        for i in range(17, 21):
            print("Século:", i)
            nomes_apelidos(dic,i)
    elif num==3:
        dic_relações = freq_relações(dic)
    elif num==4:
        convert_json(dic, "processos.json")
    else:
        print("Não é uma opção válida") 


if __name__ == "__main__":
    main()