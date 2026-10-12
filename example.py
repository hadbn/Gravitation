import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
fig, ax = plt.subplots()
G=1
N = 3
dt = 0.01 # le pas de temps pour Euler
def distance (X,Y):
    a,b = X
    c,d = Y
    return np.sqrt ( (a-c)**2 + (b-d)**2 )

ax.axis('equal')
ax.set(xlim=[-6, 6], ylim=[-6,6])


positions = np.random.randint(-5,6,2*N).reshape(N,2)
masses= np.random.randint(0,5,N)
"""vecteurs = np.zeros((N,N,2))
for i in range (N):
    for j in range (N):
        if i!=j : 
            Pi = positions [i]
            Pj =positions [j]
            vecteurs[i][j] = (Pj - Pi)/distance(Pi,Pj)""" #essai avec boucle for des vecteurs pointant de i -> j

#calcul des accelerations initiales 
vecteurs = positions[:,np.newaxis,:] - positions[np.newaxis,:,:] # matrice de taille (N,N,2) de coordonnées (xi-xj,yi-yj)
distances = np.sqrt((vecteurs*vecteurs).sum(axis=2)) # matrice de même taille de coord = aux distances entre les points Pi et Pj
distances[np.eye(N, dtype=bool)] = np.inf #on mets des infini sur la diagonale pour obtenir 0 qd on divise par la distance (on a cherché sur Internet)
acc1 = vecteurs/(distances[:,:,np.newaxis]**2) # tableau des (Xi-Xj)/ (distance au carré entre i et j) (sans le facteur masse)
mass = masses.reshape(3,1) # pour braodcast lors du produit des masses avec acc1
mass_carré = mass*np.ones((N,N)) # matrice carrée 
mass_carré[np.eye(N, dtype=bool)] = 0 # même matrice carrée mais avec des 0 sur la diagonale
acc_avec_mass= acc1*(mass_carré[:,:,np.newaxis]) #broadcasting 
accelerations = acc_avec_mass.sum(axis=1) # tableau des accélérations 

#on suppose des vitesses initiales nulles 
vitesses = np.zeros(2*N).reshape(N,2)


def get_new_position(position):
    # on est à t_i et on va à t_i+1
    global vitesses
    global positions
    global accelerations
    vitesses = vitesses + accelerations*dt # on a les vitesses de chaque point à t_i+1
    positions = positions + vitesses*dt  # implémentation d'Euler

    #accelerations à t_i+1 (même procédure que le tableau accélérations à l'état inital mais avec des tableaux positions et vitesses ≠)
    vecteurs = positions[:,np.newaxis,:] - positions[np.newaxis,:,:]
    distances = np.sqrt((vecteurs*vecteurs).sum(axis=2)) 
    distances[np.eye(N, dtype=bool)] = np.inf #on mets des infini sur la diagonale pour obtenir 0 qd on divise par la distance
    acc1 = vecteurs/(distances[:,:,np.newaxis]**2) # tableau des (Xi-Xj)/distance au carré entre i et j (sans le facteur masse)
    acc_avec_mass= acc1*(mass_carré[:,:,np.newaxis]) #broadcasting 
    accelerations = acc_avec_mass.sum(axis=1) # tableau des accélérations       
    return positions


scat = ax.scatter(positions[:,0], positions[:,1]) # ts les x et y de chaque point

def animate(t):
    # une variable globale est une variable utilisée dans une fonction mais dont la modification de la valeur a une portée globale (donc extérieure à la fonction)

    global positions
    positions = get_new_position(positions)

    # update the scatter plot:
    # le np.stack sert ici à mettre les positions dans la bonne shape
    data = np.stack(positions).T #on fait la transposée
    scat.set_offsets(data)
    return scat

ani = animation.FuncAnimation(fig=fig, func=animate, interval=5000)
plt.show()
