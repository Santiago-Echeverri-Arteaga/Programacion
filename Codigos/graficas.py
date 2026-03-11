import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def cm2inch(x): return x/2.54


fig = plt.figure(figsize=(cm2inch(8), cm2inch(15)))
fig.subplots_adjust(hspace=0)
gs = GridSpec(2, 2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0], projection='polar')
ax3 = fig.add_subplot(gs[0, 1], projection='3d')
plt.show()
