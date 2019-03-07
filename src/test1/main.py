import pygame
import visuals as vis
import random as rand

__author__ = "Tim Slippy (VoxelV), Nathan Hale (NrdyN8)"


class Game:

    def __init__(self):
        pygame.init()
        self.visual_set = vis.Visuals
        self.screen = pygame.display.set_mode(self.visual_set.size)

    @staticmethod
    def rand_pair(max1, max2):
        return rand.randint(0, max1), rand.randint(0, max2)

    def run(self):

        pygame.display.set_caption("NanoTech")

        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # Loop until the user clicks the close button.
        # -------- Main Program Loop -----------
        while not done:
            # --- Controls
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 1 = left, 2 = middle
                    if event.button == 1:
                        pass

            # --- Game logic should go here

            # --- Drawing code should go here
            # Clear the screen
            self.screen.fill(self.visual_set.bgColor)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)

        # Quit when done
        pygame.quit()

# Execute this script
if __name__ == "__main__":
    game1 = Game()
    game1.run()
