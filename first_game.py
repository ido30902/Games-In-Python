import pygame

def main():
    pygame.init()

    window = pygame.display.set_mode((500,500))

    pygame.display.set_caption("First Game")

    player = Player()

    run = True
    while run:
        pygame.time.delay(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player.vel
        if keys[pygame.K_RIGHT] and player.x < (500 - player.width):
            player.x += player.vel
        if not(player.isJump):
            if keys[pygame.K_UP] and player.y > 0:
                player.y -= player.vel
            if keys[pygame.K_DOWN] and player.y < (500 - player.height):
                player.y += player.vel
            if keys[pygame.K_SPACE]:
                player.isJump = True
        else:
            if player.jumpCount >= - 10:
                neg = 1
                if player.jumpCount < 0:
                    neg = -1
                player.y -= (player.jumpCount ** 2) / 2 * neg
                player.jumpCount -= 1

            else:
                player.isJump = False
                player.jumpCount = 10



        window.fill((0,0,0))
        pygame.draw.rect(window,(255,0,0),(player.x,player.y,player.width,player.height))
        pygame.display.update()

    pygame.quit()


class Player(object):

    def __init__(self):
        self.x = 50
        self.y = 50
        self.width = 20
        self.height = 20
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10

if __name__ == '__main__':
    main()
