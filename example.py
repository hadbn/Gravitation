
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


#Conditions initiales :
N= 10
G=1
dt=1
masse =np.random.uniform(1,5,N)
pos = np.random.uniform(0,10, (N, 2))
vit = np.zeros((N,2))

fig, ax = plt.subplots()

def distance(pos):
    diff = pos[np.newaxis, :, :] - pos[:, np.newaxis, :]
    norme = np.sqrt(np.sum(diff**2, axis=2))
    np.fill_diagonal(norme, np.inf)
    return diff, norme

def calcul_acceleration(pos,masse):
    diff, norme = distance(pos)
    m = masse[np.newaxis, :, np.newaxis]
    a=G*np.sum((m*diff)/(norme[:, :, np.newaxis])**3, axis=1)
    return a


#ax.axis('equal')
ax.set(xlim=[-10, 10], ylim=[-10,10])


def get_new_position(pos, masse):
    global vit
    At=calcul_acceleration(pos,masse)
    vit=vit + At*dt
    pos= pos + vit*dt
    return pos

scat = ax.scatter(pos[:,0], pos[:,1])


def animate(t):
    # une variable globale est une variable utilisée dans une fonction mais dont la modification de la valeur a une portée globale (donc extérieure à la fonction)

    global positions
    positions = get_new_position(pos,masse)

    # update the scatter plot:
    # le np.stack sert ici à mettre les positions dans la bonne shape
    data = np.stack(positions).T
    scat.set_offsets(data)
    return scat

ani = animation.FuncAnimation(
    fig=fig,
    func=animate,
    interval=100,
    cache_frame_data=False,
)
plt.show()
