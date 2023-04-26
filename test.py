import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sélection de caractéristique")

# Liste des caractéristiques
caractéristiques = ["Force", "Agilité", "Endurance", "Intelligence"]

# Création des surfaces d'affichage pour chaque caractéristique
font = pygame.font.SysFont(None, 30)
surface_list = []
for i, caractéristique in enumerate(caractéristiques):
    surface = font.render(caractéristique, True, (255, 255, 255))
    x = 50
    y = 50 + i*50
    surface_rect = surface.get_rect(topleft=(x, y))
    surface_list.append((surface, surface_rect))

# Boucle principale du jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérification de quelle caractéristique est sélectionnée
            for surface, surface_rect in surface_list:
                if surface_rect.collidepoint(pygame.mouse.get_pos()):
                    # Marquage de la caractéristique sélectionnée
                    surface.fill((255, 0, 0))
    
    # Affichage des surfaces d'affichage à l'écran
    for surface, surface_rect in surface_list:
        screen.blit(surface, surface_rect)
    
    pygame.display.flip()

pygame.quit()
