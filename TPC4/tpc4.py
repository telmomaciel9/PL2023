import json
import re


def read(file):
    list = []

    regex =  re.compile(r"(?P<Numero>[^,]+),(?P<Nome>[^,]+),(?P<Curso>[^,]+),?(?P<Notas>[^{,]+)?(?P<Intervalo>\{\d(?:,\d)?\})?(?:::)?(?P<FAgregacao>[^,]+)?")

    with open(file,'r') as file:
        cabeçalho = (regex.match(file.readline()[:-1]).groupdict())

        lines = file.readlines()

        for line in lines:
            subdic = {}
            arguments = line.split(',')

            subdic['Numero'] = arguments[0]
            subdic['Nome'] = arguments[1]
            subdic['Curso'] = arguments[2]

            if(cabeçalho['Notas']):
                if(cabeçalho['Intervalo']):
                    regex_delimiters = re.compile(r"{(?P<Inicio>\d),?(?P<Fim>\d)?}")
                    num = (regex_delimiters.match(cabeçalho['Intervalo']).groupdict())
                    if(num['Fim']):
                        notas = []
                        for x in arguments[3:3+int(num['Fim'])]:
                            if(x.isdigit()):
                                notas.append(int(x))
                    else:
                        notas = []
                        for x in arguments[3:3+int(num['Inicio'])]:
                            if(x.isdigit()):
                                notas.append(int(x))
                    if(cabeçalho['FAgregacao']):
                        function = cabeçalho['FAgregacao']
                        if(function == "sum"):
                            soma = sum(notas)
                            subdic['Notas'] = soma
                        if(function == "media"):
                            media = sum(notas)/len(notas)
                            subdic['Notas'] = media
                        if(function == "min"):
                            minimo = min(notas)
                            subdic['Notas'] = minimo
                        if(function == "max"):
                            maximo = max(notas)
                            subdic['Notas'] = maximo
                    else:
                        subdic['Notas'] = notas
                else:
                    subdic['Notas'] = arguments[3]
            list.append(subdic)
    return list

def create_json(dic, path):
    file = open(path, "w")
    json.dump(dic, file, indent=4, ensure_ascii=False)

def main():
    print("Ficheiros disponíveis para converter:")
    print("1- alunos.csv")
    print("2- alunos2.csv")
    print("3- alunos3.csv")
    print("4- alunos4.csv")
    print("5- alunos5.csv")
    
    option = input("Digite o ficheiro que pretende converter:")
    if option == '1':
        lista = read("alunos.csv")
        create_json(lista,"alunos.json")
    elif option == '2':
        lista = read("alunos2.csv")
        create_json(lista,"alunos2.json")
    elif option == '3':
        lista = read("alunos3.csv")
        create_json(lista,"alunos3.json")
    elif option == '4':
        lista = read("alunos4.csv")
        create_json(lista,"alunos4.json")
    elif option == '5':
        lista = read("alunos5.csv")
        create_json(lista,"alunos5.json")
    else:
        print("Opção inválida.")
        main()

if __name__ == '__main__':
    main()