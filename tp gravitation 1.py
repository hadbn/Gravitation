#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()

##initialisation
N=3
G=1.0
P_ini=np.array([[0,-1],[2,0],[2,-2]])
V_ini=np.array([[0,0],[0.1,0.1],[0,-0.1]])
M=np.array([1,2,3])
dt=0.05
P_tp=V_ini*dt+P_ini
P_tav=P_ini


def evol_position(P_tav,P_tp,M,dt,N):
    """
    renvoie l'évolution de P la matrice des positions à l'intant présent
    P_Tav: matrice coordonées passées
    P_tp : matrice coordonées futures
    M: matrice des masses
    dt : pas de temps
    N : nombre de corps
    """
    MG=M[np.newaxis,:,np.newaxis] 
    
    Diff=P_tp[np.newaxis,:,:]-P_tp[:,np.newaxis,:] #matrice des différences des coordonnées

    Dis=np.sqrt(Diff[:,:,0]**2+Diff[:,:,1]**2)
    Dis=Dis[:,:,np.newaxis] #matrices des distances au présent des corps entre eux

    P_futur=G*dt**2*np.sum(np.nan_to_num(Diff*MG/(Dis**3)), axis=1)+2*P_tp-P_tav #coordonnées futures des corps
    return P_tp,P_futur


def get_new_position(P_tp,P_tav):
    (P_tp,P_tav)=evol_position(P_tp,P_tav,M,dt,N)
    return P_tp, P_tav


scat = ax.scatter(P_tp[:,0], P_tp[:,1]) #j'ai repris l'exemple c'est à dire les Xs à gauche et les Ys à droite


def animate(t):
    # une variable globale est une variable utilisée dans une fonction mais dont la modification de la valeur a une portée globale (donc extérieure à la fonction)

    global P_tp
    global P_tav
    P_tp, P_tav = get_new_position(P_tp,P_tav)

    # update the scatter plot:
    # le np.stack sert ici à mettre les positions dans la bonne shape
    data = np.stack(P_tp)
    scat.set_offsets(data)
    return scat

ani = animation.FuncAnimation(fig=fig, func=animate, interval=100)
plt.show()

"""
Lors du lancement on remarque que pour des trop grand pas de temps, il y a divergence parfois du schéma .
Cela doit probablement être deu au fait que les schémas Explicite sont généralement plus instable que des méthodes implicites
Les schémas implicites eux, sont plus lourdes en mémoires et en complexitéde par le fait qu'il faut résoudre une équation à chaque pas de temps
Enfin, on remarque qu'il y a divergence des planètes lorsqu'elle se rapproche, cela est du au fait que l'on divise par la distance entre celles-ci qui se rapproche ainsi de 0. 
Un modèle évitant cela serait de donner une valeur minimale au distance (cela parait incohérent mais s'affranchirai de la problématique précédente)
"""