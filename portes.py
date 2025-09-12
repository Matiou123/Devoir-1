import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D

# --- Fonctions auxiliaires ---
def vecteur_unitaire(angle_deg):
    angle_rad = np.radians(angle_deg)
    return np.cos(angle_rad), np.sin(angle_rad)
def porteX(angle_deg):
    angle_rad = np.radians(angle_deg)
    ket0 = np.sin(angle_rad)
    ket1 = np.cos(angle_rad)
    return (ket0,ket1)
def porteZ(angle_deg):
    angle_rad = np.radians(angle_deg)
    ket0 = np.cos(angle_rad)
    ket1 = -np.sin(angle_rad)
    return (ket0,ket1)
def porteH(angle_deg):
    angle_rad = np.radians(angle_deg)
    ket0 = (np.cos(angle_rad) + np.sin(angle_rad))/np.sqrt(2)
    ket1 = (np.cos(angle_rad) - np.sin(angle_rad))/np.sqrt(2)
    return (ket0,ket1)
def porteR(angle_deg):
    angle_deg += 45
    angle_rad = np.radians(angle_deg)
    return (np.cos(angle_rad), np.sin(angle_rad))
def porteF(angle_deg, angle_porte):
    angle_rad = np.radians(angle_deg - angle_porte)
    return (np.cos(angle_rad), np.sin(angle_rad))
""" def porteC(angle_deg):
    angle_rad = np.radians(angle_deg)
    proba_1 = np.random(np.sin(angle_deg))
    if proba_1 >= np.sin(angle_deg):
        return 0
    else: return  """
def porteWmoins(angle_deg):
    angle_rad = np.radians(2*angle_deg)
    sin = np.sin(angle_rad)
    ket0 = sin
    if (angle_deg % 360) > 180:
        ket1 = -np.sqrt(1 - sin**2)
    else:
        ket1 = np.sqrt(1 - sin**2)
    return ket0, ket1

def porteWplus(angle_deg):
    angle_rad = np.radians(2*angle_deg)
    cos = np.cos(angle_rad)
    ket0 = cos
    if (angle_deg % 360) > 180:
        ket1 = -np.sqrt(1 - cos**2)
    else:
        ket1 = np.sqrt(1 - cos**2)
    return ket0, ket1

def probaEnBaseQuantique(probabilité):
    if probabilité == 1:
        return 0,1
    if probabilité == 0:
        return 1,0
    angle_rad = np.atan(np.sqrt(probabilité/(1-probabilité)))
    ket0 = np.cos(angle_rad)
    ket1 = np.sin(angle_rad)
    return ket0, ket1

def plot_porte_animée(Porte,angle_deg):
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
    vecteur2ket1 = ax.quiver(0, 0, 0, 1, angles='xy', scale_units='xy', scale=1, color='orange')  
    vecteur2Ket0 = ax.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1, color='green')
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
        x1, y1 = Porte(angle_deg)

        # Mise à jour des vecteurs
        vecteur1.set_UVC(x, y)
        vecteur2.set_UVC(x1, y1)

        ax.set_title(f"Porte W+ avec angle {angle_deg}°")
        return vecteur1, vecteur2

    # --- Animation ---
    ani = FuncAnimation(fig, update, frames=range(0, 361), interval=20, blit=True, repeat=True)
    ani.save("PorteWplus.gif", writer="pillow", fps=30)
    plt.show()


def plot_porte(Porte, angle_deg):
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
    vecteur2ket1 = ax.quiver(0, 0, 0, 10, angles='xy', scale_units='xy', scale=10, color='orange')  
    vecteur2Ket0 = ax.quiver(0, 0, 10, 0, angles='xy', scale_units='xy', scale=10, color='green')


    # --- Légende ---
    # Création de "handles" factices pour la légende
    legend_elements = [
        Line2D([0], [0], color='red', lw=2, label='Vecteur unité'),
        Line2D([0], [0], color='magenta', lw=2, label='Vecteur W'),
    ]
    ax.legend(handles=legend_elements, loc="upper right")

    
    x, y = vecteur_unitaire(angle_deg)
    x1, y1 = Porte(angle_deg)

    # Mise à jour des vecteurs
    vecteur1.set_UVC(x, y)
    vecteur2.set_UVC(x1, y1)

    ax.set_title(f"Porte W avec angle {angle_deg}°")

    plt.show()

""" ket0 , ket1 = probaEnBaseQuantique(0.999)
print(ket0**2,ket1**2) """

def plot_proba_to_vecteur():
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

    vecteur1 = ax.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1, color='magenta')
    vecteur2ket1 = ax.quiver(0, 0, 0, 1, angles='xy', scale_units='xy', scale=1, color='orange')  
    vecteur2Ket0 = ax.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1, color='green')
    # --- Légende ---
    # Création de "handles" factices pour la légende
    legend_elements = [
        Line2D([0], [0], color='magenta', lw=2, label='Vecteur probabilité')
    ]
    ax.legend(handles=legend_elements, loc="upper right")

    # --- Fonction de mise à jour ---
    def update(proba):
        
        x1, y1 = probaEnBaseQuantique(proba)

        # Mise à jour des vecteurs
        vecteur1.set_UVC(x1, y1)

        ax.set_title(f"Vecteur probabilité avec p = {proba:.2f}")
        return [vecteur1]

    # --- Animation ---
    frames = np.arange(0, 1.01, 1e-2)  # p varie de 0 à 1 avec pas de 0.001
    ani = FuncAnimation(fig, update, frames=frames, interval=20, blit=True, repeat=True)
    ani.save("Proba_to_vecteur.gif", writer="pillow", fps=30)
    plt.show()
    
plot_proba_to_vecteur()
