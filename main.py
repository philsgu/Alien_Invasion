import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create the game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # The self arugment gives Ship access to the game's resources e.g. screen object
        self.ship = Ship(self)

        # Set the background color:
        self.bg_color = (230, 230, 230)
      

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # helper method
            self._check_events()
            self.ship.update()
            self._update_screen()
            

    # Watch for keyboard and mouse events.
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
              self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
              self._cehck_keyup_events(event)
    
    def _check_keydown_events(self, event):
      """Respond to keypresses."""
      if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
      elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True
      elif event.key == pygame.K_q:
        sys.exit()
    
    def _cehck_keyup_events(self, event): 
      """Respond to key releases."""
      if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False
      elif event.key == pygame.K_LEFT:
        self.ship.moving_left = False

            

    # Redraw the screen during each pass through the loop
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


ai = AlienInvasion()
ai.run_game()
