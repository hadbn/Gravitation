import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()


ax.axis('equal')
#ax.set(xlim=[-1, 1000], ylim=[-1,1000])


positions = [[0, 1000], [0,0]]

def get_new_position(position):
    Xs = positions[0]
    Ys = positions[1]
    return [[Xs[0]+1, Xs[1]-1], [Ys[0]+1, Ys[1]+1]]

scat = ax.scatter(positions[0], positions[1])


def animate(t):
    # une variable globale est une variable utilisée dans une fonction mais dont la modification de la valeur a une portée globale (donc extérieure à la fonction)

    global positions
    positions = get_new_position(positions)

    # update the scatter plot:
    # le np.stack sert ici à mettre les positions dans la bonne shape
    data = np.stack(positions).T
    scat.set_offsets(data)
    return scat

ani = animation.FuncAnimation(fig=fig, func=animate, interval=100)
plt.show()