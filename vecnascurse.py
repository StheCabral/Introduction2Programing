set = [] #[[aluno + sintomas], [aluno + sintomas], [aluno + sintomas]]
report = []
names_in_danger = []
max = False
symptons = ["dor de cabeca", "insonia", "pesadelos", "suor frio", "visoes"]
while ("descobrir" not in report):
    report = input().split(", ")
    if ("descobrir" not in report):
        set.append(report)
for student in set: #  percorrendo array report com todos os alunos
    danger = 0
    total_symptons = len(student) #  quantidade de sintomas daquele aluno
    for sympton in range (1, total_symptons): #  percorrendo os sintomas do aluno
        if ((student[sympton]) in symptons): #  verificando seo estudante tem algum dos sintomas
            danger += 1
    if (danger == 5): #  Se ele tem todos os sintomas ele está em perigo
        names_in_danger.append(student[0])
total_in_danger = len(names_in_danger)

##############   output
if ("Max" in names_in_danger):
    max = True
    names_in_danger.remove("Max")
    total_in_danger = len(names_in_danger)
    print("Oh não, Max está em perigo! Let's run up that hill com a Kate Bush e ajudar nossa amiga.")
    if (total_in_danger >= 1):
        print(f"Além dela, tem mais {total_in_danger} pessoa(s) na mira do Vecna!")
    if (total_in_danger == 0):
        total_in_danger = -1
elif (total_in_danger >= 1):
    print(f"Tem {total_in_danger} pessoa(s) na mira do Vecna!")  


if (total_in_danger > 1):
    formatted_names = names_in_danger
    last_name = formatted_names.pop(-1)
    names = ", ".join(formatted_names)
    print(f"Precisamos avisar {names} e {last_name} para prepararem suas músicas favoritas.")
elif (total_in_danger == 1):
    print(f"Precisamos avisar {names_in_danger[0]} para preparar sua música favorita.")
elif (total_in_danger == 0):
    print("Não conseguimos encontrar ninguém com esses sintomas, o próximo ataque do Vecna será imprevisível.")
