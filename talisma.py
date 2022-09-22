amuletos = {
    "Carneiro" : {"skill": "Adormecer", "requirement": "Imortalidade", "previous" : "Cao"}, 

    "Cao": {"skill": "Imortalidade", "requirement": "Forca descomunal", "previous" : "Touro"},

    "Cobra": {"skill": "Invisibilidade", "requirement": "Equilibrio espiritual", "previous" : "Tigre"},

    "Coelho" : {"skill": "Alta velocidade", "requirement": "Metamorfose animal", "previous" : "Macaco"},

    "Tigre" : {"skill": "Equilibrio espiritual", "requirement": "Adormecer", "previous" : "Carneiro"}, 

    "Dragao" : {"skill": "Fogo", "requirement": "Cura", "previous" : "Cavalo"},

    "Cavalo": {"skill": "Cura", "requirement": "Levitacao", "previous" : "Galo"}, 

    "Macaco": {"skill": "Metamorfose animal", "requirement": "Raio laser", "previous" : "Porco"},

    "Galo": {"skill": "Levitacao", "requirement": "Animar objetos", "previous" : "Rato"}, 

    "Porco": {"skill": "Raio laser", "requirement": "Fogo", "previous" : "Dragao"},

    "Rato": {"skill": "Animar objetos", "requirement": "Alta velocidade", "previous" : "Coelho"}, 

    "Touro": {"skill": "Forca descomunal", "requirement": "Invisibilidade", "previous" : "Cobra"}
    }
total_jackie_stones = int(input())
skills = []

for i in range (total_jackie_stones):
    stone = input()
    skills.append(amuletos[stone]["skill"])

enemys = int(input())
enemys_defeated = 0
for i in range (enemys):
    stone_persued = input()

    if (amuletos[stone_persued]["requirement"] in skills):
        skills.append(amuletos[stone_persued]["skill"])
        print(f"Boa! O talisma do {stone_persued} vai ser nosso!")
        enemys_defeated += 1
    else:
        requirement = (amuletos[stone_persued]["previous"])
        print(f"Nao vai dar, melhor ir atras do talisma do {requirement} antes.")
if (enemys_defeated == enemys):
    print("Esse plano funciona, vamos agora!")
else:
    print("Que mau dia!! Melhor pensarmos num plano de fuga.")