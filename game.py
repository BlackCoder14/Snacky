import pygame

class Game:
    def __init__(self):
        # Window creation
        self.screen_width = 720
        self.screen_height = 480
        self.screen = pygame.display.set_caption("Snacky")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Snacke's variables
        self.snacke_position_x = self.screen_width / 2
        self.snacke_position_y = self.screen_height / 2
        self.snacke_direction_x = 0
        self.snacke_direction_y = 0

        # Border creation
        self.border_x = 0
        self.border_y = 0
        self.border = pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.screen_width, self.screen_height))

        # Main while condition
        self.run = True

    def check_limits(self):
        if self.snacke_position_x <= self.border_x or self.snacke_position_x >= self.border_x \
            or self.snacke_position_y <= self.border_x or self.snacke_position_y >= self.border_x:
            pygame.quit()

    def running(self):
        # Boucle creation
        while self.run:
            self.screen.fill((0, 0, 0))
            # Snacke creation
            pygame.draw.rect(self.screen, (255, 0, 0), (self.snacke_position_x, self.snacke_position_y, 10, 10))

            self.check_limits

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snacke_direction_x = 0
                        self.snacke_direction_y = -10

                    if event.key == pygame.K_RIGHT:
                        self.snacke_direction_x = 10
                        self.snacke_direction_y = 0

                    if event.key == pygame.K_DOWN:
                        self.snacke_direction_x = 0
                        self.snacke_direction_y = 10

                    if event.key == pygame.K_LEFT:
                        self.snacke_direction_x = -10
                        self.snacke_direction_y = 0

                    print(event.key)

                    self.snacke_position_x += self.snacke_direction_x
                    self.snacke_position_y += self.snacke_direction_y

            # Window update
            pygame.display.flip()