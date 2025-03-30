import pygame

#colors
colorRED = (255,0,0)
colorBLUE = (0,0,255)
colorWHITE = (255,255,255)
colorBLACK = (0,0,0)
colorGREEN = (0,255,0)

pygame.init()

# ---------- SETUP ----------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill(colorBLACK)  # Fill background with black

clock = pygame.time.Clock()
font = pygame.font.SysFont('None', 30)

# ---------- STATE ----------
draw = False
radius = 5
color = 'blue'       # Initial color
mode = 'circle'      # Initial mode

start_pos = (0, 0)
end_pos = (0, 0)

# ---------- DRAWING FUNCTIONS ----------

def drawCircle(surf, start, end, width, color):
    center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
    radius = min(abs(start[0] - end[0]), abs(start[1] - end[1])) // 2
    pygame.draw.circle(surf, pygame.Color(color), center, radius, width)

def drawRectangle(surf, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1,x2), min(y1,y2), abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(surf, pygame.Color(color), rect, width)

def drawSquare(surf, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    size = min(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(min(x1, x2), min(y1, y2), size, size)
    pygame.draw.rect(surf, pygame.Color(color), rect, width)

def drawRightTriangle(surf, start, end, color):
    x1, y1 = start
    x2, y2 = end
    points = [(x1, y1), (x1, y2), (x2, y2)]
    pygame.draw.polygon(surf, pygame.Color(color), points)

def drawEquilateralTriangle(surf, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    base = abs(x2 - x1)
    height = (3**0.5 / 2) * base
    mid_x = (x1 + x2) / 2
    if y2 > y1:
        points = [(x1, y2), (x2, y2), (mid_x, y2 - height)]
    else:
        points = [(x1, y1), (x2, y1), (mid_x, y1 - height)]
    pygame.draw.polygon(surf, pygame.Color(color), points, width)

def drawRhombus(surf, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    points = [
        (mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)
    ]
    pygame.draw.polygon(surf, pygame.Color(color), points, width)

def eraseRect(surf, start, end):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1,x2), min(y1,y2), abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(surf, colorBLACK, rect)

# ---------- MAIN LOOP ----------
running = True
while running:
    screen.blit(base_layer, (0, 0))  # Draw saved content

    # Show current color and mode
    pygame.draw.rect(screen, pygame.Color(color), (10, 10, 30, 30))
    color_label = font.render(f"Color: {color}", True, pygame.Color('white'))
    mode_label = font.render(f"Mode: {mode}", True, pygame.Color('white'))
    screen.blit(color_label, (50, 15))
    screen.blit(mode_label, (50, 45))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ---------- KEY CONTROLS ----------
        if event.type == pygame.KEYDOWN:
            # Color keys
            if event.key == pygame.K_r:
                color = 'red'
            elif event.key == pygame.K_g:
                color = 'green'
            elif event.key == pygame.K_b:
                color = 'blue'

            # Mode keys
            elif event.key == pygame.K_1:
                mode = 'circle'
            elif event.key == pygame.K_2:
                mode = 'rectangle'
            elif event.key == pygame.K_3:
                mode = 'square'
            elif event.key == pygame.K_4:
                mode = 'right_triangle'
            elif event.key == pygame.K_5:
                mode = 'equilateral_triangle'
            elif event.key == pygame.K_6:
                mode = 'rhombus'
            elif event.key == pygame.K_7:
                mode = 'erase'

        # ---------- MOUSE DRAWING ----------
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            draw = True
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and draw:
            end_pos = event.pos
            if mode == 'circle':
                drawCircle(base_layer, start_pos, end_pos, radius, color)
            elif mode == 'rectangle':
                drawRectangle(base_layer, start_pos, end_pos, radius, color)
            elif mode == 'square':
                drawSquare(base_layer, start_pos, end_pos, radius, color)
            elif mode == 'right_triangle':
                drawRightTriangle(base_layer, start_pos, end_pos, color)
            elif mode == 'equilateral_triangle':
                drawEquilateralTriangle(base_layer, start_pos, end_pos, radius, color)
            elif mode == 'rhombus':
                drawRhombus(base_layer, start_pos, end_pos, radius, color)
            elif mode == 'erase':
                eraseRect(base_layer, start_pos, end_pos)

            draw = False  # Stop drawing

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
