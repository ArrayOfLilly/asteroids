import pygame
import constants as c

def main():
    pygame.init()
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    print("Starting asteroids!")
    print(f"Screen width: {c.SCREEN_WIDTH}")
    print(f"Screen height: {c.SCREEN_HEIGHT}")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
