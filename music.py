artists = input().split(" - ")
possible_grades = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
dean_grades = []
sam_grades = []
for artist in artists:
    songs = input().split(" - ")
    for song in songs:
        while ("Sam" in comment or "Dean" in comment): #rodar até receber outra música
            enter = input()
            if (":" in enter):
                comment = enter.split(": ")
                if ("Sam" in comment):
                    sam_grades.append(comment)
                elif ("Dean" in comment):
                    dean_grades.append(comment)
            else:
                songs = enter.split(" - ")
# ao inves de criar arrays de comentários, guardar o ultimo valoe de sam, o ultimo valor de dean e depois analisar
e depois guardar os seguintes ultimos
