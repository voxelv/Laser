import pygame
import space_object
import laser
import visuals as vis
import random as rand

__author__ = "Tim Slippy (VoxelV), Nathan Hale (NrdyN8)"


class NanoTech:
    visual_set = vis.Visuals
    screen = pygame.display.set_mode(visual_set.size)
    saved_lasers = []
    sobjects = []  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def __init__(self):
        pygame.init()
        self.laser_types = [['red', self.visual_set.redLaser],
                            ['blue', self.visual_set.blueLaser],
                            ['green', self.visual_set.greenLaser],
                            ['yellow', self.visual_set.yellowLaser]
                            ]

    @staticmethod
    def rand_pair(max1, max2):
        return rand.randint(0, max1), rand.randint(0, max2)

    # TEMPORARY <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def create_rand_so(self):
        for i in range(12):
            # if rand.randint(0, 1000) < 500:
            pos = self.rand_pair(self.visual_set.max_width, self.visual_set.max_height)
            # for obj in self.sobjects:
            #     if obj.in_range(pos, 20):
            #         return
            r = rand.randint(0, 1)
            #r = rand.randint(0, len(self.laser_types) - 1)
            x = space_object.ConnectibleSpaceObject(self, pos, self.laser_types[r][0], self.laser_types[r][1])
            self.sobjects.append(x)

    def draw_sobjects(self):
        for so in self.sobjects:
            if rand.randint(0, 1000) < 950:
                so.move(0)

        for so in self.sobjects:
            so.recalculate_connections(0, 500)
        for so in self.sobjects:
            so.draw_connections()
        for so in self.sobjects:
            so.render()

    def run(self):

        pygame.display.set_caption("NanoTech")

        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        self.create_rand_so()  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        # Loop until the user clicks the close button.
        # -------- Main Program Loop -----------
        while not done:
            # --- Main event loop

            # --- Controls
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 1 = left
                    if event.button == 1:
                        x = space_object.ConnectibleSpaceObject(self, pygame.mouse.get_pos(), self.laser_types[0][0], self.laser_types[0][1])
                        self.sobjects.append(x)

                    # 2 = middle
                    if event.button == 2:
                        self.sobjects = []
                        #self.create_rand_so()

                    # 3 = right mouse
                    if event.button == 3:
                        x = space_object.ConnectibleSpaceObject(self, pygame.mouse.get_pos(), self.laser_types[1][0], self.laser_types[1][1])
                        self.sobjects.append(x)


            # --- Game logic should go here

            # --- Drawing code should go here
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
            self.screen.fill(self.visual_set.bgColor)

            self.draw_sobjects()  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            # Draw a laser
            # vis.Visuals.redLaser.draw_laser(
            #    self.screen,
            #    self.rand_pair(self.visual_set.max_width, self.visual_set.max_height),
            #    self.rand_pair(self.visual_set.max_width, self.visual_set.max_height),
            #    5)

            # pygame.draw.line(self.screen, (0, 0), (self.visual_set.max_width, self.visual_set.max_height), width=5)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game1 = NanoTech()
    game1.run()
