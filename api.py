"""api.py"""
import httpx
URL = 'https://pax.ulaval.ca/squadro/api2/'
"""Fonction liste partie"""
def liste_parties(liste_idul):
    rep = httpx.get(URL+'parties', params={'iduls':liste_idul})
    if rep.status_code == 200:
       rep = rep.json()
       return rep.get("parties")
    if rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])
"""fonction recup"""
def récupérer_une_partie(id_partie):
    liste = [id_partie,]
    rep = httpx.get(URL+'partie', params={'id':liste})
    if rep.status_code == 200:
        tup = (rep.json()['id'], rep.json()['prochain_joueur'], rep.json()['état'])
        return tup
    if rep.status_code ==406:
        raise RuntimeError(rep.json()['message'])
"""cree"""
def créer_une_partie(liste_iduls):
    rep = httpx.post(URL+'partie', json={'iduls': liste_iduls})
    if rep.status_code == 200:
        rep = rep.json() 
        tup = (rep.get('id'), rep.get('prochain_joueur'), rep.get('état'))
        return tup
    if rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])
"""jou"""
def jouer_un_coup(id_partie, idul, pion):
    rep = httpx.put(URL+'jouer', json= {'id':id_partie, 'idul':idul, 'pion':pion})
    if rep.status_code == 200:
        rep = rep.json()
        if rep['gagnant'] is not None:
           raise StopIteration(rep['gagnant'])
        else:
             tup = (rep['id'], rep['prochain_joueur'], rep['état'])
             return tup
    if rep.status_code == 406:
        raise RuntimeError(rep.json()['message'])
