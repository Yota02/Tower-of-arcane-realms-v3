import pygame

class DialogBox:

    def __init__(self):
        self.box = pygame.image.load("data_gama/dialog/dialog_box.png")
        info = pygame.display.Info()
        self.box = pygame.transform.scale(self.box, (int(info.current_w * 0.7), int(info.current_h * 0.2)))
        self.text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque dictum arcu eget ex pulvinar"
        self.font = pygame.font.Font("data_gama/dialog/dogica.ttf", 24)
        self.line_spacing = 10  # Espace entre les lignes
        self.text_lines = self.wrap_text(self.text, self.font, box_width=self.box.get_width() - 20)
        self.max_chars_per_frame = 1  # Nombre de caractères à afficher par frame
        self.current_chars = 0  # Nombre de caractères déjà affichés

    def wrap_text(self, text, font, box_width):
        lines = []
        line = ""
        for word in text.split():
            test_line = line + word + " "
            if font.size(test_line)[0] > box_width:
                lines.append(line)
                line = word + " "
            else:
                line = test_line
        lines.append(line)
        return lines

    def render(self, screen):
        screen_width, screen_height = screen.get_size()
        box_width, box_height = self.box.get_size()
        x = (screen_width - box_width) // 2
        y = screen_height - box_height
        screen.blit(self.box, (x, y))
        text_height = len(self.text_lines) * (self.font.get_height() + self.line_spacing)  # Calcul de la hauteur totale du texte
        text_y = y + box_height // 2 - text_height // 2
        for i, line in enumerate(self.text_lines):
        # Calcul du nombre de caractères à afficher pour cette ligne
            chars_to_render = min(self.current_chars, len(line))
        # Rendu du texte partiellement affiché pour cette ligne
            text_surface = self.font.render(line[:chars_to_render], False, (0,0,0))
            text_rect = text_surface.get_rect()
            text_rect.centerx = x + box_width // 2
            text_rect.y = text_y + i * (self.font.get_height() + self.line_spacing)  # Ajout de l'espace entre les lignes
            screen.blit(text_surface, text_rect)
    # Mise à jour du nombre de caractères à afficher
        self.current_chars += self.max_chars_per_frame
    # Si on a affiché tout le texte, on réinitialise les variables pour afficher à nouveau le texte complet
        if self.current_chars > len(self.text):
            self.current_chars = 0
            pygame.time.wait(1000)  # Attente d'une seconde avant de réafficher le texte complet

