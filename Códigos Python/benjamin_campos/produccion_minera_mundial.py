import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation
from matplotlib.colors import Normalize

data = pd.read_csv('Produccion_mundial_cobre.csv', sep=';', decimal='.')
data = data[data.iloc[:, 0] != 'TOTAL']

for col in data.columns[1:]:
    try:
        data[col] = pd.to_numeric(data[col], errors='coerce')
    except:
        pass

paises = data.iloc[:, 0].tolist()
años = [int(col) for col in data.columns[1:] if col.isdigit()]

fig, ax = plt.subplots(figsize=(15, 10))

norm = Normalize(vmin=0, vmax=len(paises))
colors = cm.viridis(norm(np.arange(len(paises))))  

def update(frame):
    ax.clear()
    año = años[frame]
    
    año_data = data.iloc[:, [0, frame + 1]].copy()
    año_data.columns = ['País', 'Producción']
    año_data = año_data.sort_values('Producción', ascending=False).reset_index(drop=True)
    
    top_producers = año_data[año_data['Producción'] > 50].copy()
    
    x_pos = np.arange(len(top_producers))
    tamaño_burbujas = top_producers['Producción'] * 2
    
    for i, (_, row) in enumerate(top_producers.iterrows()):
        país = row['País']
        producción = row['Producción']
        idx = paises.index(país) if país in paises else 0
        
        ax.scatter(i, producción, s=tamaño_burbujas[i], color=colors[idx], alpha=0.7, edgecolors='black')

        ax.text(producción + 50, i, f"{país}: {producción:.1f} kt", va='center')
    
    ax.set_ylim(0, top_producers['Producción'].max() * 1.3)
    ax.set_xlim(-1, len(top_producers))
    ax.set_xticks(x_pos)
    ax.set_xticklabels(top_producers['País'], rotation=45, ha='right')
    ax.set_ylabel('Producción de Cobre (kt)', fontsize=14)
    ax.set_title(f'Producción Mundial de Cobre - {año}', fontsize=18)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    return ax

ani = FuncAnimation(fig, update, frames=len(años), interval=1000, blit=False)
ani.save('produccion_mundial_cobre.gif', writer='pillow', fps=1, dpi=100)
plt.tight_layout()
plt.show()