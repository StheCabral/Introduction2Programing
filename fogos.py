name = input()
decibeis = int(input())
decibeis_caruaru = int(input())
decibeis_campina = int(input())

if (decibeis <= decibeis_caruaru and decibeis <= decibeis_campina):
    print(f"Boa Felipe, o {name} será um sucesso em Campina Grande e Caruaru!")
elif (decibeis <= decibeis_caruaru and decibeis > decibeis_campina):
     print(f"Infelizmente em Campina Grande não vai rolar, mas em Caruaru o {name} vai ser extouro!")
elif (decibeis > decibeis_caruaru and decibeis <= decibeis_campina):
    print(f"Infelizmente em Caruaru não vai rolar, mas em Campina Grande o {name} vai ser extouro!")
else: 
    print(f"Poxa Felipe, não vai ser dessa vez que {name} fará um sucesso pelas festas juninas do Brasil")
