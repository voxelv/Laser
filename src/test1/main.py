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

    @staticmethod
    def rand_pair(max1, max2):
        return rand.randint(0, max1), rand.randint(0, max2)

    # TEMPORARY <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def create_rand_so(self):
        for i in range(100):
        #if rand.randint(0, 1000) < 500:
            pos = self.rand_pair(self.visual_set.max_width, self.visual_set.max_height)
            # for obj in self.sobjects:
            #     if obj.in_range(pos, 20):
            #         return
            r = rand.randint(0, 1)
            x = space_object.ConnectibleSpaceObject(self, pos, 'red' if r == 1 else 'blue',
                                                    self.visual_set.redLaser if r == 1 else self.visual_set.blueLaser)
            self.sobjects.append(x)

    def draw_sobjects(self):
        for so in self.sobjects:
            if rand.randint(0, 1000) < 50:
                so.move(5)
        for so in self.sobjects:
            so.recalculate_connections(0, 100)
        for so in self.sobjects:
            so.draw_connections()
        for so in self.sobjects:
            so.render()

    def save_laser(self, start, stop, color):
        self.saved_lasers.append((start, stop, color))

    ###
    #   draw_saved_lasers
    #
    #   Def: draws lasers saved in array
    # Testing this location
    ###
    def draw_saved_lasers(self, surface):
        for laser in self.saved_lasers:
            if laser[2] == "blue":
                vis.Visuals.blueLaser.draw_laser(surface, laser[0], laser[1], 5)
            if laser[2] == "red":
                vis.Visuals.redLaser.draw_laser(surface, laser[0], laser[1], 5)

    def run(self):

        pygame.display.set_caption("NanoTech")

        done = False
        rstart_mouse_pos = (0, 0)
        lstart_mouse_pos = (0, 0)
        lmouse_clicked = False
        rmouse_clicked = False

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
                    # 1 = left, 2 = middle
                    if event.button == 1:
                        if not lmouse_clicked:
                            lmouse_clicked = True
                            lstart_mouse_pos = pygame.mouse.get_pos()
                        elif lmouse_clicked:
                            self.save_laser(lstart_mouse_pos, pygame.mouse.get_pos(), "red")
                            lmouse_clicked = False

                    # 3 = right mouse
                    if event.button == 3:
                        if not rmouse_clicked:
                            rmouse_clicked = True
                            rstart_mouse_pos = pygame.mouse.get_pos()
                        elif rmouse_clicked:
                            self.save_laser(rstart_mouse_pos, pygame.mouse.get_pos(), "blue")
                            rmouse_clicked = False

            # --- Game logic should go here

            # --- Drawing code should go here
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
            self.screen.fill(self.visual_set.bgColor)

            if lmouse_clicked:
                vis.Visuals.redLaser.draw_laser(self.screen, lstart_mouse_pos, pygame.mouse.get_pos(), 5)
            if rmouse_clicked:
                vis.Visuals.blueLaser.draw_laser(self.screen, rstart_mouse_pos, pygame.mouse.get_pos(), 5)

            self.draw_saved_lasers(self.screen)
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
