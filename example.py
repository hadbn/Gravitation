import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from copy import deepcopy
import numpy.random as rd
fig, ax = plt.subplots()

ax.axis('equal')
#ax.set(xlim=[-1, 1000], ylim=[-1,1000])

n = 10
G = 1
dt = 0.1

positions = rd.randint(0,100,(2,n))
vitesses = rd.randint(0,10,(2,n))
masses = rd.randint(1,6,(1,n))



def get_new_position(masses,positions,vitesses,dt):
    X = positions[0]
    Y = positions[1]
    Vx = vitesses[0]
    Vy = vitesses[1]
    
    newX = X + Vx*dt
    newY = Y + Vy*dt
    new_positions = np.array([newX,newY])

    tab_masses = (masses*np.ones((n,n))) * (np.transpose(masses)*np.ones((n,n))) # en position i,j : mi*mj

    positions = np.transpose(positions)

    if np.shape(positions) != (n,2) :
        positions = positions[:,:,0] # de manière incompréhensible, parfois la shape de positions est changée

    colonnes = positions*(np.ones((n,n))[:,:,np.newaxis]) # en position i,j : [xi,yi]
    lignes = np.moveaxis(colonnes,0,1) # en position i,j : [xj,yj]
    distances = lignes - colonnes
    directions = deepcopy(distances) # servira plus tard
    distances = distances**2
    distances = np.sum(distances,axis=2) # en position i,j : distance corps i - corps j au carré
    directions = directions/((np.sqrt(distances))[:,:,np.newaxis]) # en position i,j : vecteur unitaire j vers i
    distances[distances == 0] = np.inf
    Normes_Forces = G*tab_masses/distances # en position i,j normes de la force i sur j
    Forces = Normes_Forces[:,:,np.newaxis]*directions # en position i,j : vecteur force i sur j
    Forces = np.sum(Forces,axis=1) # en position j : force sur j
    Acc = Forces/np.transpose(masses)
    Ax = Acc[:,0]
    Ay = Acc[:,1]



    Vx = Vx + Ax*dt
    Vy = Vy + Ay*dt
    new_vitesses = [Vx,Vy]

    return new_positions,new_vitesses

scat = ax.scatter(positions[0], positions[1],s=masses*10)


def animate(t):
    # une variable globale est une variable utilisée dans une fonction mais dont la modification de la valeur a une portée globale (donc extérieure à la fonction)

    global positions
    positions = get_new_position(masses,positions,vitesses,dt)

    # update the scatter plot:
    # le np.stack sert ici à mettre les positions dans la bonne shape
    data = np.stack(positions).T
    scat.set_offsets(data)
    return scat

ani = animation.FuncAnimation(fig=fig, func=animate, interval=100)
plt.show()
