from collections import defaultdict
import math


def lerficheiro(ficheiro):
    dados = []
    with open(ficheiro) as f:
        for line in f:
            line = line.strip()
            dados.append(line.split(','))
    dados.pop(0)
    return dados

def distribuicaosexos(dados):
    return {'Feminino': sum(1 for entrada in dados if entrada[5] == '1' and entrada[1] == 'F'),
            'Masculino': sum(1 for entrada in dados if entrada[5] == '1' and entrada[1] == 'M'),
            'FemininoS': sum(1 for entrada in dados if entrada[5] == '0' and entrada[1] == 'F'),
            'MasculinoS': sum(1 for entrada in dados if entrada[5] == '0' and entrada[1] == 'M')}


def distribuicaoescaloesetarios(dados):
    aux = defaultdict(int)
    for entrada in dados:
        if entrada[5] == '1':
            num = math.floor(int(entrada[0]) / 5) + 1
            aux[num] += 1
    return dict(aux)

def distribuicaocolesterol(dados):
    aux = {}
    for entrada in dados:
        if entrada[5] == '1':
            nivel = math.floor(int(entrada[3])/10) + 1
            aux.setdefault(nivel, 0)
            aux[nivel] += 1
    return aux

def printDistSexo(dados):
    print("\nQuantidade de casos por sexo")
    print( " ___________ ___________________________ _____________________________ ")
    print( "|   Sexo    | Número de pessoas doentes | Número de pessoas saudáveis |")
    print( "|-----------|---------------------------|-----------------------------|")
    print(f"| Masculino |             {dados['Masculino']}           |             {dados['MasculinoS']}             |")
    print( "|-----------|---------------------------|-----------------------------|")
    print(f"| Feminino  |             {dados['Feminino']}            |             {dados['FemininoS']}             |")
    print( "|___________|___________________________|_____________________________|")

def printDistIdade(dados):
    print("\nQuantidade de casos por faixa etária")
    print( " ______________ _________________ ")
    print( "| Faixa etária | Número de casos |")
    print( "|--------------|-----------------|")

    grupos = list(dados.keys())
    grupos.sort()

    for num in grupos:
        if len(str(dados[num]))==1:
            print(f"|   [{(num-1)*5}-{num*5-1}]    |       {dados[num]}         |")
            print( "|--------------|-----------------|")
        if len(str(dados[num]))==2:
            print(f"|   [{(num-1)*5}-{num*5-1}]    |       {dados[num]}        |")
            print( "|--------------|-----------------|")
        if len(str(dados[num]))==3:
            print(f"|   [{(num-1)*5}-{num*5-1}]    |       {dados[num]}       |")
            print( "|--------------|-----------------|")
        
        

def printDistColesterol(dados):
    print("\nQuantidade de casos por nível de colesterol")
    print( " _____________________ _________________ ")
    print( "| Nível de Colesterol | Número de casos |")
    print( "|---------------------|-----------------|")

    grupos = list(dados.keys())
    grupos.sort()

    for num in grupos:
        if len(str((num-1)*10))==1:
            print(f"|      [{(num-1)*10}-{num*10-1}]          |        {dados[num]}      |")
            print( "|---------------------|-----------------|")
        elif len(str((num-1)*10))==2:
            print(f"|      [{(num-1)*10}-{num*10-1}]        |        {dados[num]}      |")
            print( "|---------------------|-----------------|")
        elif len(str(dados[num]))==1:
            print(f"|      [{(num-1)*10}-{num*10-1}]      |        {dados[num]}        |")
            print( "|---------------------|-----------------|")
        elif len(str(dados[num]))==2:
            print(f"|      [{(num-1)*10}-{num*10-1}]      |        {dados[num]}       |")
            print( "|---------------------|-----------------|")
        elif len(str(dados[num]))==3:
            print(f"|   [{(num-1)*10}-{num*10-1}]      |        {dados[num]}      |")
            print( "|---------------------|-----------------|")


dados= lerficheiro('myheart.csv')

print("Opções de distribuição")
print("1- Distribuição da doença por sexo")
print("2- Distribuição da doença por faixa etária")
print("3- Distribuição da doença por níveis de colesterol")

num = int(input("Escolha uma opção: "))

if num==1:
    dic = distribuicaosexos(dados)
    printDistSexo(dic)
elif num==2:
    dic = distribuicaoescaloesetarios(dados)
    printDistIdade(dic)
else: 
    dic = distribuicaocolesterol(dados)
    printDistColesterol(dic)

