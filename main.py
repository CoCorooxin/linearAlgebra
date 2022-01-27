""""
TD
Algebre lineaire
le vecteur
la combinaison et la concatenation
"""
import numpy as np

a = np.array([1,2,3,4])

b = np.array([-1,3,4,6])

z = np.concatenate([a,b])

x_a = np.array([1,0,0,0,0])
x_e = np.array([0,1,0,0,0])
x_i = np.array([0,0,1,0,0])
x_u = np.array([0,0,0,1,0])
x_o = np.array([0,0,0,0,1])
voyelle = np.eye(5)

""""ou 
np.eye()
pour creer un array diagonale de 2D
"""
oui_com = x_o+ x_u+ x_i
#print(oui_com)   [0 0 1 1 1]
oui = np.concatenate([x_o,x_u,x_i])
#print(oui)    [0 0 0 0 1 0 0 0 1 0 0 0 1 0 0]

"""la difference le premier est la combinaison linéaire des trois vecteurs, le résultat reste la même taille 
mais concatenation crée un vecteur qui a une taille plus grande"""
text = open("text.txt", "r")
x = "la souris mange le fromage et le trouve bon"
l_w = x.split()
def text_dict(text):
    set_word = set(text)
    word_list = list(set_word)
    word_idx = {tokens : idx for (idx, tokens) in enumerate(word_list)}
    return word_idx

dicto = text_dict(l_w)

print(text_dict(l_w))
def text_vect(dicto, l_w):
    t = np.zeros(len(l_w))
    x = np.eye(len(l_w))
    for tok in l_w:
        idx = dicto[tok]
        t = t+x[idx]
    return t

print(text_vect(dicto,l_w))








