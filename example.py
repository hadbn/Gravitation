import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from numpy import random
fig, ax = plt.subplots()

G=1
dt=0.01
n=10

ax.axis('equal')
ax.set(xlim=[-100, 100], ylim=[-100,100])



pos=np.random.randint(-5,6,(n,2))
masses=np.random.randint(1,5,n)
vitesse = np.zeros((n,2))
# position=np.concatenate(pos,vitesses)

def get_new_position(pos,vitesse):
    Pos1 = pos[:,np.newaxis,:]
    Pos2 = pos[np.newaxis,:,:]
    Diff= Pos1-Pos2
    Dist=np.square(Diff)
    Dist=np.sum(Dist, axis=2)
    Dist=np.sqrt(Dist)
    Dist[Dist == 0] = np.inf
    F=masses[np.newaxis,:,np.newaxis]*Diff
    F=F/(Dist[:,:,np.newaxis]**3)
    F=np.nan_to_num(F)
    A=-G*np.sum(F,axis=1)

    pos=pos+dt*vitesse
    vitesse=vitesse+dt*A
    return (pos,vitesse)

scat = ax.scatter(pos[:,0], pos[:,1])


def animate(t):
    # une variable globale est une variable utilisée dans une fonction mais dont la modification de la valeur a une portée globale (donc extérieure à la fonction)

    global pos
    global vitesse
    pos,vitesse = get_new_position(pos,vitesse)

    print("pos =", pos)
    print("nombre de particules =", len(pos))

    # update the scatter plot:
    # le np.stack sert ici à mettre les positions dans la bonne shape
    data = np.stack(pos).T
    scat.set_offsets(data)
    return scat

ani = animation.FuncAnimation(fig=fig, func=animate, interval=100,cache_frame_data=False)
plt.show()


