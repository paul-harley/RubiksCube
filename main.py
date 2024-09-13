import pygame
import globals
import matrix
import cube

screen = pygame.display.set_mode((globals.SCREEN_HEIGHT, globals.SCREEN_WIDTH))

bigCube = cube.Cube(globals.cubeScale, 'b', [])
smallCubes = []

for x in range(3):
    for y in range(3):
        for z in range(3):
            smallCube = cube.Cube(globals.cubeScale/3, 's', [x,y,z])
            smallCubes.append(smallCube)



bigCube.update2DCords()
for myCube in smallCubes:
    myCube.update2DCords()

def rotateAllCubes(direction):

    bigCube.rotateCube(direction, globals.rotateAngle)
    bigCube.update2DCords()

    print("top", bigCube.position[1][0][2])
    print("bottom",bigCube.position[7][0][2])
    print("DONE")

    for myCube in smallCubes:
        myCube.rotateCube(direction, globals.rotateAngle)
        myCube.update2DCords()


clock = pygame.time.Clock()
resume = True
while resume:

    key = pygame.key.get_pressed()

    #ROTATING OVERALL CUBE
    if key[pygame.K_w]: #UP
        globals.rotateAngle = -0.05
        rotateAllCubes('x')

    if key[pygame.K_s]: #DOWN
        globals.rotateAngle = 0.05
        rotateAllCubes('x')

    if key[pygame.K_a]: #LEFT
        globals.rotateAngle = 0.05
        rotateAllCubes('y')

    if key[pygame.K_d]: #RIGHT
        globals.rotateAngle = -0.05
        rotateAllCubes('y')

    #DRAWING TO SCREEN
    screen.fill(globals.BLACK)
    bigCube.draw(screen)

    for myCube in smallCubes:
        myCube.draw(screen)

    #EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False 
    pygame.display.update()
    clock.tick(10)
pygame.quit()