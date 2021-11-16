import argparse

def traiter_la_ligne_de_commande():
    '''traiter'''
    parser = argparse.ArgumentParser(add_help=True, description='Squadro')
    parser.add_argument('IDUL',nargs ='+', type = str, metavar='IDUL',
    help = 'IDUL du ou des joueur(s)')
    parser.add_argument('-p','--parties',metavar='',
    type = list,help = 'Lister les 20 dernières parties')
    return parser.parse_args()

def afficher_le_plateau_de_jeu(etat_de_jeu):
    '''affichage'''
    print('légende:')
    print('□',etat_de_jeu[0].get("nom"))
    print('■', etat_de_jeu[1].get("nom"))
    pion_jv = etat_de_jeu[1].get("pions")
    pion_jh = etat_de_jeu[0].get("pions")
    plateau = ['     . | . : | : : | : : | : . | .','       ','...    ']
    if pion_jv[0] == 0:
        plateau[1] += '█    .'
        plateau[2] += '●     '
    elif pion_jv[0] ==12:
        plateau[1] += '●    '
        plateau[2] += '█     '
    else:
        plateau[1] += '|    .'
        if pion_jv[0]==11:
            plateau[2] += '●     '
        else:
            plateau[2] += '|     '

    if pion_jv[1] == 0:
        plateau[1] += '█ .   '
        plateau[2] += '●     '
    elif pion_jv[1] ==12:
        plateau[1] += '●    '
        plateau[2] += '█     '
    else:
        plateau[1] += '| .   '
        if pion_jv[1]==11:
            plateau[2] += '●     '
        else:
            plateau[2] += '|     '
    if pion_jv[2] == 0:
        plateau[1] += '█    .'
        plateau[2] += '●     '
    elif pion_jv[2] ==12:
        plateau[1] += '●    '
        plateau[2] += '█     '
    else:
        plateau[1] += '|    .'
        if pion_jv[2]==11:
            plateau[2] += '●     '
        else:
            plateau[2] += '|     '
    if pion_jv[3] == 0 :
        plateau[1] += '█ .   '
        plateau[2] += '●     '
    elif pion_jv[3] ==12:
        plateau[1] += '●    '
        plateau[2] += '█     '
    else:
        plateau[1] += '| .   '
        if pion_jv[3]==11:
            plateau[2] += '●     '
        else:
            plateau[2] += '|     '
    if pion_jv[4] == 0:
        plateau[1] += '█'
        plateau[2] += '●    .'
    elif pion_jv[4] ==12 :
        plateau[1] += '●    '
        plateau[2] += '█    .'
    else :
        plateau[1] +='|'
        if pion_jv[4]==11:
            plateau[2] += '●     '
        else:
            plateau[2] += '|     '
    plateau.append('──')
    plateau.append('...   ')
    plateau.append('.      ')
    plateau.append('──')
    plateau.append('.     ')
    plateau.append('..     ')
    plateau.append('──')
    plateau.append('..    ')
    plateau.append('.      ')
    plateau.append('──')
    plateau.append('.     ')
    plateau.append('...    ')
    plateau.append('──')
    plateau.append('...   ')
    plateau.append('     . ')
    if pion_jh[0] == 0:
        plateau[3] +='□□ ○'
    elif pion_jh[0] == 12:
        plateau[3] += '○ □□'
    else:
        plateau[3] += '───'
    for i in range(5):
        if pion_jv[i] == 1:
            plateau[3] += '─█────'
            plateau[4] += ' ●    '
        elif pion_jv[i] == 11:
            plateau[3] += '─█───'
            plateau[4] += ' |    '
        elif pion_jh[0] == i + 1:
            plateau[3] = '─' + plateau[3]
            plateau[3] += '□□ ○──'
            plateau[4] += ' |    '
        elif pion_jh[0] == 11-i:
            plateau[3] = plateau[3][:-1]
            plateau[3] = '─' + plateau[3]
            plateau[3] += '○ □□───'
            plateau[4] += ' |    '
        else:
            plateau[3] += '─┼────'
            plateau[4] += ' |    '
        if pion_jv[i] == 10:
            plateau[5] += '●     '
        else:
            plateau[5] += '|     '
    if pion_jh[0] == 6:
        plateau[3] = '─' + plateau[3][:-3] + '○ □□──'
    else:
        plateau[3] += '───'
    if pion_jh[1] == 0:
        plateau[6] +='□□ ○'
    elif pion_jh[1] == 12:
        plateau[6] += '○ □□'
    else:
        plateau[6] += '───'
    for i in range(5):
        if pion_jv[i] == 2:
            plateau[6] += '─█────'
            plateau[7] += ' ●    '
        elif pion_jv[i] == 10:
            plateau[6] += '─█────'
            plateau[7] += ' |    '
        elif pion_jh[1] == i + 1:
            plateau[6] = '─' + plateau[6]
            plateau[6] += '□□ ○──'
            plateau[7] += ' |    '
        elif pion_jh[1] == 11-i:
            plateau[6] = plateau[6][:-1]
            plateau[6] = '─' + plateau[6]
            plateau[6] += '○ □□───'
            plateau[7] += ' |    '
        else:
            plateau[6] += '─┼────'
            plateau[7] += ' |    '
        if pion_jv[i] == 9:
            plateau[8] += '●     '
        else:
            plateau[8] += '|     '
    if pion_jh[1] == 6:
        plateau[6] = '─'+plateau[6][:-3] + '○ □□──'
    else:
        plateau[6] += '───'
    if pion_jh[2] == 0:
        plateau[9] +='□□ ○'
    elif pion_jh[2] == 12:
        plateau[9] += '○ □□'
    else:
        plateau[9] += '───'
    for i in range(5):
        if pion_jv[i] == 3:
            plateau[9] += '─█────'
            plateau[10] += ' ●    '
        elif pion_jv[i] == 9:
            plateau[9] += '─█────'
            plateau[10] += ' |    '
        elif pion_jh[2] == i + 1:
            plateau[9] = '─' + plateau[9]
            plateau[9] += '□□ ○──'
            plateau[10] += ' |    '
        elif pion_jh[2] == 11-i:
            plateau[9] = plateau[9][:-1]
            plateau[9] = '─' + plateau[9]
            plateau[9] += '○ □□───'
            plateau[10] += ' |    '
        else:
            plateau[9] += '─┼────'
            plateau[10] += ' |    '
        if pion_jv[i] == 8:
            plateau[11] += '●     '
        else:
            plateau[11] += '|     '
    if pion_jh[2] == 6:
        plateau[9] = '─'+plateau[9][:-3] + '○ □□──'
    else:
        plateau[9] += '───'
    if pion_jh[3] == 0:
        plateau[12] +='□□ ○'
    elif pion_jh[3] == 12:
        plateau[12] += '○ □□'
    else:
        plateau[12] += '───'
    for i in range(5):
        if pion_jv[i] == 4:
            plateau[12] += '─█────'
            plateau[13] += ' ●    '
        elif pion_jv[i] == 8:
            plateau[12] += '─█────'
            plateau[13] += ' |    '
        elif pion_jh[3] == i + 1:
            plateau[12] = '─' + plateau[12]
            plateau[12] += '□□ ○──'
            plateau[13] += ' |    '
        elif pion_jh[3] == 11-i:
            plateau[12] = plateau[12][:-1]
            plateau[12] = '─' + plateau[12]
            plateau[12] += '○ □□───'
            plateau[13] += ' |    '
        else:
            plateau[12] += '─┼────'
            plateau[13] += ' |    '
        if pion_jv[i] == 7:
            plateau[14] += '●     '
        else:
            plateau[14] += '|     '
    if pion_jh[3] == 6:
        plateau[12] = '─'+plateau[12][:-3] + '○ □□──'
    else:
        plateau[12] += '───'
    if pion_jh[4] == 0:
        plateau[15] +='□□ ○'
    elif pion_jh[4] == 12:
        plateau[15] += '○ □□'
    else:
        plateau[15] += '───'
    for i in range(5):
        if pion_jv[i] == 5:
            plateau[15] += '─█────'
            plateau[16] += ' ●    '
        elif pion_jv[i] == 7:
            plateau[15] += '─█────'
            plateau[16] += ' |    '
        elif pion_jh[4] == i + 1:
            plateau[15] = '─' + plateau[15]
            plateau[15] += '□□ ○──'
            if pion_jv[i] == 6 :   
                plateau[16] += ' ●    '
            else:
                plateau[16] += ' |    '
        elif pion_jh[4] == 11-i:
            plateau[15] = plateau[15][:-1]
            plateau[15] = '─' + plateau[15]
            plateau[15] += '○ □□───'
            if pion_jv[i] == 6 :
                plateau[16] += ' ●    '
            else:
                plateau[16] += ' |    '
        else:
            plateau[15] += '─┼────'
            if pion_jv[i] == 6 :   
                plateau[16] += ' ●    '
            else:
                plateau[16] += ' |    '
    if pion_jh[4] == 6:
        plateau[15] = plateau[15][:-3] + '○ □□──'
    else:
        plateau[15] += '───'
    if pion_jv[0] == 6:
        plateau[17] += '█ .   '
    else :
        plateau[17] += '| .   '
    for i in range(2):
        if pion_jv[i+1] == 6:
            plateau[17] += '█     '
        else:
            plateau[17] += '|     '
    if pion_jv[3] ==6:
        plateau[17] += '█   . '
    else:
        plateau[17] +='|  .  '
    if pion_jv[4] ==6:
        plateau[17] +='█ .   '
    else:
        plateau[17] +='| .   '

    plateau.append('     : | : . | . : | : . | . : | :')
    plateau[4] += '  .'
    plateau[5] = plateau[5][:-1]+ '...'
    plateau[7] = plateau[7][:-1]+ ' ...'
    plateau[8] += '..'
    plateau[10] += ' ..'
    plateau[11] = plateau[11][:-2]+ ' ...'
    plateau[13] = plateau[13][:-1]+ ' ...'
    plateau[14] += ' .'
    plateau[16] += '  .'
    return '\n'.join(plateau)

def formatter_les_parties(liste_parties):
    '''formatter'''
    representation =[]
    for e, dictio in enumerate(liste_parties):
        joueur = dictio.get("joueurs")
        if e == 0:
            representation.append(f'{1+e} : {dictio.get("date")}, {joueur[0]} vs {joueur[1]}\n')
        else:
            if e ==19:
                representation.append(f'{1+e}: {dictio.get("date")}, {joueur[0]} vs {joueur[1]}')
                representation[19] += f', gagnant: {dictio.get("gagnant")}'
            else:
                representation.append(f'{1+e}: {dictio.get("date")}, {joueur[0]} vs {joueur[1]}\n')
    return ''.join(representation)

