set = [] #[[aluno + sintomas], [aluno + sintomas], [aluno + sintomas]]
report = []
danger = 0
names_in_danger = []
symptons = ["dor de cabeca", "insonia", "pesadelos", "suor frio", "visoes"]
max = False
while ("descobrir" not in report):
    report = input().split(", ")
    if ("descobrir" not in report):
        set.append(report)

for student in set: #percorrendo array report com todos os alunos
    total_symptons = len(student) #quantidade de sintomas daquele aluno
    for sympton in range (1, total_symptons): #percorrendo os sintomas do aluno
        if ((student[sympton]) in symptons): #verificando seo estudante tem algum dos sintomas
            danger += 1
    print(danger)
    if (danger == 5):
        names_in_danger.append(student[0])
        if ((student[0] == "Max")):
            max = True
            set.remove(student)
#############formatando saída
total_in_danger = len(names_in_danger)
formatted_names = names_in_danger
formatted_names.remove(formatted_names[0])
formatted_names.remove(formatted_names[-1])
names = " ,".join(formatted_names)
##############output
print(len(names_in_danger))
if (max):
    print("Oh não, Max está em perigo! Let's run up that hill com a Kate Bush e ajudar nossa amiga.")
    if (total_in_danger >= 1):
        print(f"Além dela, tem mais {total_in_danger} pessoa(s) na mira do Vecna!")
else:
    print(f"Tem {total_in_danger} pessoa(s) na mira do Vecna!")
    
if (total_in_danger == 0):
    print("Não conseguimos encontrar ninguém com esses sintomas, o próximo ataque do Vecna será imprevisível.")
elif (total_in_danger > 1):
    print(f"Precisamos avisar {names_in_danger[0]}, {names} e {names_in_danger[-1]} para prepararem suas músicas favoritas.")
elif (total_in_danger == 1):
    print(f"Precisamos avisar {set[0][0]} para preparar sua música favorita.")
