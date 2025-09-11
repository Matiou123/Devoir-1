import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D

# --- Fonctions auxiliaires ---
def vecteur_unitaire(angle_deg):
    angle_rad = np.radians(angle_deg)
    return np.cos(angle_rad), np.sin(angle_rad)

def porteW(angle_deg):
    angle_rad = np.radians(2*angle_deg)
    cos = np.cos(angle_rad)
    x = cos
    if (angle_deg % 360) > 180:
        y = -np.sqrt(1 - cos**2)
    else:
        y = np.sqrt(1 - cos**2)
    return x, y

# --- Préparation du graphe ---
fig, ax = plt.subplots()

# Cercle unité
theta = np.linspace(0, 2*np.pi, 500)
ax.plot(np.cos(theta), np.sin(theta), 'b')

# Axes
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)

# Limites
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)

# Deux vecteurs initialisés
vecteur1 = ax.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1, color='red')
vecteur2 = ax.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1, color='magenta')

# --- Légende ---
# Création de "handles" factices pour la légende
legend_elements = [
    Line2D([0], [0], color='red', lw=2, label='Vecteur unité'),
    Line2D([0], [0], color='magenta', lw=2, label='Vecteur porteW')
]
ax.legend(handles=legend_elements, loc="upper right")

# --- Fonction de mise à jour ---
def update(angle_deg):
    x, y = vecteur_unitaire(angle_deg)
    x1, y1 = porteW(angle_deg)

    # Mise à jour des vecteurs
    vecteur1.set_UVC(x, y)
    vecteur2.set_UVC(x1, y1)

    ax.set_title(f"Cercle trigonométrique avec angle {angle_deg}°")
    return vecteur1, vecteur2

# --- Animation ---
ani = FuncAnimation(fig, update, frames=range(0, 361), interval=15, blit=True, repeat=True)
ani.save("cercle_trigo.gif", writer="pillow", fps=30)
plt.show()
