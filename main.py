import sys

import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
	pygame.init()
	screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	font = pygame.font.Font(pygame.font.get_default_font(), 20)

	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	Shot.containers = (shots, updatable, drawable)

	AsteroidField()
	player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill((0, 0, 0))
		point_label = pygame.font.Font.render(font, f"Score: {player.get_points()}", True, "blue")
		screen.blit(point_label, (0, 0))

		updatable.update(dt)
		for element in drawable:
			element.draw(screen)

		for asteroid in asteroids:
			if player.check_collision(asteroid):
				print(f"Points: {player.get_points()}")
				print("Game over!")
				sys.exit()
			for shot in shots:
				if asteroid.check_collision(shot):
					shot.kill()
					asteroid.split()
					player.add_points()

		pygame.display.flip()
		tick = clock.tick(60)
		dt = tick / 1000


if __name__ == "__main__":
	main()
