"""main.py"""
import squadro
import api
argument = squadro.traiter_la_ligne_de_commande()
partie_jeu = api.créer_une_partie(argument.IDUL)
partie_en_cours = api.récupérer_une_partie(partie_jeu[0])
while True:
    print(squadro.afficher_le_plateau_de_jeu(partie_en_cours[2]))
    print('donner le numéro du pion ',partie_en_cours[1])
    pion = input()
    partie_en_cours = api.jouer_un_coup(partie_en_cours[0], partie_en_cours[1], pion)
    partie_en_cours = api.récupérer_une_partie(partie_en_cours[0])
