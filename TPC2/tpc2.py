print("Para terminar faça Ctrl + D")
print("Insira o texto: ")

count = True
num = ""
sum = 0

line = ""
while True:
    try:
        line += input().lower()
    except EOFError:
        break

max = len(line)

for i in range(0, max):
    if line[i].isdigit() and count:
        num += line[i]
    elif count:
        if num != "":
            sum += int(num) 
        else: 
            sum += 0
        num = ""
    if line[i] == '=':
        print(sum)
    elif line.find("on", i) == i:
        count = True
    elif line.find("off", i) == i:
        count = False