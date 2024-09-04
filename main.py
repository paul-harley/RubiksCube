import pygame
import globals
import matrix

screen = pygame.display.set_mode((globals.SCREEN_HEIGHT, globals.SCREEN_WIDTH))

cubePoints = [
    [[0,0,0]],
    [[0,0,1]],
    [[1,0,0]],
    [[1,0,1]],
    [[1,1,0]],
    [[1,1,1]],
    [[0,1,0]],
    [[0,1,1]],
]

cube2DPoints = []

for p in cubePoints:
    for i in range(3):
        p[0][i] = p[0][i] * globals.cubeScale
        
        #just a random num so its fully on screen
        #will centre in future
        p[0][i] += 70


def update2DCords():
    cube2DPoints.clear()
    for p in cubePoints:
        cube2DPoints.append(matrix.multiplyMatrix(p, matrix.orthographicProjectionMatrix))

update2DCords()


clock = pygame.time.Clock()
resume = True
while resume:

    key = pygame.key.get_pressed()

    if key[pygame.K_w]: #UP
        globals.rotateAngle = -0.05
        cubePoints = matrix.rotateCube(cubePoints, 'x', globals.rotateAngle)
        update2DCords()
        print(cube2DPoints)

    if key[pygame.K_s]: #DOWN
        globals.rotateAngle = 0.05
        cubePoints = matrix.rotateCube(cubePoints, 'x', globals.rotateAngle)
        update2DCords()
        print(cube2DPoints)

    if key[pygame.K_a]: #LEFT
        globals.rotateAngle = 0.05
        cubePoints = matrix.rotateCube(cubePoints, 'y', globals.rotateAngle)
        update2DCords()
        print(cube2DPoints)

    if key[pygame.K_d]: #RIGHT
        globals.rotateAngle = -0.05
        cubePoints = matrix.rotateCube(cubePoints, 'y', globals.rotateAngle)
        update2DCords()
        print(cube2DPoints)

    screen.fill(globals.BLACK)
    for p in cube2DPoints:
        pygame.draw.circle(screen, globals.WHITE, (p[0][0], p[0][1]), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False 
    pygame.display.update()
    clock.tick(10)
pygame.quit()