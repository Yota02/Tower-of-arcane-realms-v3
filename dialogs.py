import pygame

class DialogBox:

    def __init__(self):
        self.box = pygame.image.load("data_gama/dialog/dialog_box.png")
        info = pygame.display.Info()
        self.box = pygame.transform.scale(self.box, (int(info.current_w * 0.7), int(info.current_h * 0.2)))
        self.texts = ["Lorem ipsum dolor sit amet", "consectetur adipiscing elit. Quisque dictum arcu eget ex pulvinar"]
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font("data_gama/dialog/dogica.ttf", 24)
        self.line_spacing = 10  # Espace entre les lignes
        self.max_chars_per_frame = 1  # Nombre de caractères à afficher par frame
        self.current_chars = 0  # Nombre de caractères déjà affichés
        self.reading = True
        self.text_lines = []

    def wrap_text(self, text, font, box_width):
        """Wrap text to fit inside a given width when rendered using a given font."""
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
        if self.reading:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.next_text()
                if self.current_chars < len(self.texts[self.text_index]):
                    self.letter_index += self.max_chars_per_frame
                    if self.letter_index >= len(self.texts[self.text_index]):
                        self.current_chars = len(self.texts[self.text_index])
                    else:
                        self.current_chars += self.max_chars_per_frame

                screen_width, screen_height = screen.get_size()
                box_width, box_height = self.box.get_size()
                x = (screen_width - box_width) // 2
                y = screen_height - box_height
                screen.blit(self.box, (x, y))

                if not self.text_lines:
                    self.text_lines = self.wrap_text(self.texts[self.text_index], self.font, box_width - 20)

                text_y = y + 20
                for i in range(len(self.text_lines)):
                    line = self.text_lines[i][0:self.current_chars]
                    text_surface = self.font.render(line, False, (0, 0, 0))
                    text_rect = text_surface.get_rect()
                    text_rect.centerx = self.box.get_rect().centerx
                    text_rect.top = text_y
                    screen.blit(text_surface, text_rect)
                    text_y += self.font.get_height() + self.line_spacing

                if self.current_chars >= len(self.texts[self.text_index]):
                    break

    def next_text(self):
        self.text_index += 1
        self.letter_index = 0
        self.current_chars = 0
        self.text_lines = []

        if self.text_index >= len(self.texts):
            self.reading = False
