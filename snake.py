import pygame
import time

# Initialisation de Pygame
pygame.init()

# Définition de la taille de l'écran
largeur = 800
hauteur = 600
ecran = pygame.display.set_mode((largeur, hauteur))

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Taille d'une unité du serpent
taille_unite = 20

# Vitesse de déplacement
vitesse = 20

# Direction initiale du serpent
direction = 'gauche'

# Position initiale du serpent
tete_x = largeur // 2
tete_y = hauteur // 2

# Liste des segments du serpent
segments = [(tete_x, tete_y)]

# Longueur du serpent
longueur_serpent = 5

# Boucle principale
quitter = False
while not quitter:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            quitter = True

    # Détection des touches
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and direction != "droite":
        direction = "gauche"
    elif touches[pygame.K_RIGHT] and direction != "gauche":
        direction = "droite"
    elif touches[pygame.K_UP] and direction != "bas":
        direction = "haut"
    elif touches[pygame.K_DOWN] and direction != "haut":
        direction = "bas"

    # Mise à jour de la position de la tête du serpent en fonction de la direction
    if direction == "gauche":
        tete_x -= vitesse
    elif direction == "droite":
        tete_x += vitesse
    elif direction == "haut":
        tete_y -= vitesse
    elif direction == "bas":
        tete_y += vitesse

    # Ajout de la nouvelle position de la tête à la liste des segments
    segments.append((tete_x, tete_y))

    # Limiter la longueur du serpent
    if len(segments) > longueur_serpent:
        segments = segments[1:]

    # Effacer l'écran
    ecran.fill(BLANC)

    # Dessiner les segments du serpent
    for segment in segments:
        pygame.draw.rect(ecran, NOIR, (segment[0], segment[1], taille_unite, taille_unite))

    # Mettre à jour l'écran
    pygame.display.flip()

    # Pause pour contrôler la vitesse du serpent
    time.sleep(0.1)

# Quitter Pygame
pygame.quit()
