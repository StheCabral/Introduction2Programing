song_name = input()
song_genre = input()

if (song_genre == "Xote" or song_genre == "Forró"):
    print(f"\'{song_name}\' foi adicionada com sucesso na playlist \'Dandrilha\'.")
else:
      print(f"Ocorreu um erro ao adicionar \'{song_name}\' na playlist.")

