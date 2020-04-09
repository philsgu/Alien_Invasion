import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

class AlienInvasion:
  """Overall class to manage game assets and behavior."""

  def __init__(self):
    """Initialize the game, and create the game resources."""
    pygame.init()

    self.screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")