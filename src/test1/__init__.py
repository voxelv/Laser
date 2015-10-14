import pygame
import visuals as vis
import random as rand

__author__ = "Tim Slippy"


class NanoTech:

    visual_set = vis.Visuals
    screen = pygame.display.set_mode(visual_set.size)

    def __init__(self):
        pygame.init()
        pass

    @staticmethod
    def rand_pair(max1, max2):
        return rand.randint(0, max1), rand.randint(0, max2)

    def run(self):

        pygame.display.set_caption("NanoTech")

        # Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # -------- Main Program Loop -----------
        while not done:
            # --- Main event loop
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop

            # --- Game logic should go here

            # --- Drawing code should go here
            vis.Visuals.redLaser.draw_laser(
                self.screen,
                self.rand_pair(self.visual_set.max_width, self.visual_set.max_height),
                self.rand_pair(self.visual_set.max_width, self.visual_set.max_height), 5)

            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
            self.screen.fill(self.visual_set.whiteColor)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game1 = NanoTech()
    game1.run()
