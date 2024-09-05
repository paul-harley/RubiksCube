import pygame
import globals
import matrix

screen = pygame.display.set_mode((globals.SCREEN_HEIGHT, globals.SCREEN_WIDTH))

bigCubePoints = globals.cubePoints
cube2DPoints = []
lineToDraw = globals.linesToDrawIndicies()
print(lineToDraw)

for p in bigCubePoints:
    for i in range(3):
        p[0][i] = p[0][i] * globals.cubeScale


def update2DCords():
    cube2DPoints.clear()
    for p in bigCubePoints:
        cube2DPoints.append(matrix.multiplyMatrix(p, matrix.orthographicProjectionMatrix))
    
    for p in cube2DPoints:
        p[0][0] += globals.SCREEN_WIDTH/2
        p[0][1] += globals.SCREEN_HEIGHT/4

update2DCords()
print(cube2DPoints)


clock = pygame.time.Clock()
resume = True
while resume:

    key = pygame.key.get_pressed()

    #ROTATING OVERALL CUBE
    if key[pygame.K_w]: #UP
        if key[pygame.K_d]: #RIGHT
                globals.rotateAngle = 0.05
                bigCubePoints = matrix.rotateCube(bigCubePoints, 'z', globals.rotateAngle)
                update2DCords()
        globals.rotateAngle = -0.05
        bigCubePoints = matrix.rotateCube(bigCubePoints, 'x', globals.rotateAngle)
        update2DCords()

    if key[pygame.K_s]: #DOWN
        if key[pygame.K_a]: #LEFT
            globals.rotateAngle = 0.05
            bigCubePoints = matrix.rotateCube(bigCubePoints, 'z', globals.rotateAngle)
            update2DCords()
        globals.rotateAngle = 0.05
        bigCubePoints = matrix.rotateCube(bigCubePoints, 'x', globals.rotateAngle)
        update2DCords()

    if key[pygame.K_a]: #LEFT
        globals.rotateAngle = 0.05
        bigCubePoints = matrix.rotateCube(bigCubePoints, 'y', globals.rotateAngle)
        update2DCords()

    if key[pygame.K_d]: #RIGHT
        globals.rotateAngle = -0.05
        bigCubePoints = matrix.rotateCube(bigCubePoints, 'y', globals.rotateAngle)
        update2DCords()
    
    #DRAWING BIG CUBE
    screen.fill(globals.BLACK)
    #verticies
    for p in cube2DPoints:
        pygame.draw.circle(screen, globals.WHITE, (p[0][0], p[0][1]), 5)
    
    #edges
    for i in range(len(lineToDraw)):
        xCordStart = cube2DPoints[lineToDraw[i][0]][0][0]
        yCordStart = cube2DPoints[lineToDraw[i][0]][0][1]

        xCordEnd = cube2DPoints[lineToDraw[i][1]][0][0]
        yCordEnd = cube2DPoints[lineToDraw[i][1]][0][1]

        pygame.draw.line(screen, globals.WHITE, [xCordStart, yCordStart], [xCordEnd, yCordEnd])
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False 
    pygame.display.update()
    clock.tick(10)
pygame.quit()