import pygame

def main():
    pygame.init()

    game = Game()
    snake = Snake()

    window = pygame.display.set_mode((game.width,game.height))

    pygame.display.set_caption("Snake")

    run = True
    while run:
        pygame.time.delay(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        checkCollision()
        
        keyCheck(snake)

        renderScreen(window,snake)
        

def keyCheck(snake):

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and snake.dir is not 'right':
        snake.dir = 'left'

    if keys[pygame.K_RIGHT] and snake.dir is not 'left':
        snake.dir = 'right'

    if keys[pygame.K_UP] and snake.dir is not 'down':
        snake.dir = 'up'

    if keys[pygame.K_DOWN] and snake.dir is not 'up':
        snake.dir = 'down'
        
def checkCollision():
    pass

def randomiseFood():
    pass

def renderScreen(window,snake):
    window.fill((0, 0, 0))

    pygame.draw.rect(window, (255, 0, 0), (snake.head_x_pos, snake.head_y_pos, snake.width, snake.height))

    pygame.display.update()
        

class Cell(object):

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.isFood = False
        self.isSnake = False

    
class Snake(object):

    def __init__(self):
        self.head_x_pos = 50
        self.head_y_pos = 50
        self.dir = 'right'
        self.length = 3
        self.queue = []
        self.vel = 5
        self.width = 50
        self.height = 50

    def hasEaten(self):
        self.length += 1
        self.queue.append()
        

class Game(object):

    def __init__(self):
        self.width = 500
        self.height = 500

    
if __name__ == '__main__':
    main()
