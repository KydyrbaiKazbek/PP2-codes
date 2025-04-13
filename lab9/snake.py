import pygame
import random

pygame.init()

# Colors
colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

# Display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

CELL = 25
COLS = WIDTH // CELL
ROWS = HEIGHT // CELL


def draw_grid():
    for i in range(ROWS):
        for j in range(COLS):
            if i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1:
                pygame.draw.rect(screen, colorBLACK, (j * CELL, i * CELL, CELL, CELL))
            else:
                col = colorWHITE if (i + j) % 2 == 0 else colorGRAY
                pygame.draw.rect(screen, col, (j * CELL, i * CELL, CELL, CELL))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        init_x = COLS // 2
        init_y = ROWS // 2
        self.body = [Point(init_x, init_y), Point(init_x, init_y + 1)]
        self.dx = 0
        self.dy = -1  # derection is up

    def move(self):
        # moving body
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        # moving head
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def grow(self):
        tail = self.body[-1]
        self.body.append(Point(tail.x, tail.y))

    def check_food(self, food):
        head = self.body[0]
        return head.x == food.pos.x and head.y == food.pos.y

    def check_self(self):
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

class Food:
    def __init__(self, snake, stable=False):
        self.stable = stable
        self.generate(snake)

    def generate(self, snake):
        valid = False
        while not valid:
            x = random.randint(1, COLS - 2)
            y = random.randint(1, ROWS - 2)
            valid = True
            for segment in snake.body:
                if segment.x == x and segment.y == y:
                    valid = False
                    break
        self.pos = Point(x, y)
        self.weight = random.choice([1, 2, 3])
        if self.stable:
            self.color = colorRED
        else:
            unstable_colors = [colorGREEN, colorBLUE, colorYELLOW]
            self.color = random.choice(unstable_colors)
            self.spawn_time = pygame.time.get_ticks()
            self.lifetime = random.randint(5000, 10000)

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

# speed
FPS = 5
new_level_increment = 3

clock = pygame.time.Clock()
snake = Snake()
stable_food = Food(snake, stable=True)
unstable_food = Food(snake, stable=False)

score = 0
level = 1
foods_eaten = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # limiting directions
            if event.key == pygame.K_UP and snake.dy != 1:
                snake.dx = 0
                snake.dy = -1
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1
                snake.dy = 0

    if not unstable_food.stable:
        current_time = pygame.time.get_ticks()
        if current_time - unstable_food.spawn_time > unstable_food.lifetime:
            unstable_food.generate(snake)

    # Взрезаться в Вorder
    next_x = snake.body[0].x + snake.dx
    next_y = snake.body[0].y + snake.dy
    if next_x == 0 or next_x == COLS - 1 or next_y == 0 or next_y == ROWS - 1:
        running = False
    else:
        snake.move()

    if snake.check_self():
        running = False

    # Checking if it has eaten a food
    if snake.check_food(stable_food):
        score += stable_food.weight
        foods_eaten += 1
        snake.grow()
        stable_food.generate(snake)

    if snake.check_food(unstable_food):
        score += unstable_food.weight
        foods_eaten += 1
        snake.grow()
        unstable_food.generate(snake)

    if foods_eaten >= new_level_increment:
        level += 1
        foods_eaten = 0
        FPS = int(FPS * 1.1)

    draw_grid()
    snake.draw()
    stable_food.draw()
    unstable_food.draw()

    # SCOre
    font = pygame.font.SysFont("Verdana", 20)
    info_text = font.render(f"Score: {score}  Level: {level}", True, colorWHITE)
    screen.blit(info_text, (5, 5))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
