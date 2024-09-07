import pygame
import globals
import matrix
import cube

screen = pygame.display.set_mode((globals.SCREEN_HEIGHT, globals.SCREEN_WIDTH))

bigCube = cube.Cube(globals.cubeScale, 'b')
smallCube = cube.Cube(globals.cubeScale/3, 's')
smallCubePoints = globals.getBasicCube()
smallCube2DPoints = []

#smallCubes
for p in smallCubePoints:
    for i in range(3):
        p[0][i] = (p[0][i] * (globals.cubeScale/3))
        #CONTROLS X CORDS
        if i == 0:
            p[0][i] += globals.cubeScale*(2/3)
        if i == 2:
            p[0][i] += (globals.cubeScale/3)*2




def update2DCords():

    #SMALLS
    smallCube2DPoints.clear()
    for p in smallCubePoints:
        smallCube2DPoints.append(matrix.multiplyMatrix(p, matrix.orthographicProjectionMatrix))
    
    for p in smallCube2DPoints:
        p[0][0] += (globals.SCREEN_WIDTH/2) #+ (globals.cubeScale/3)*2
        p[0][1] += (globals.SCREEN_HEIGHT/4) #+ globals.cubeScale/1




bigCube.update2DCords()
smallCube.update2DCords()

clock = pygame.time.Clock()
resume = True
while resume:

    key = pygame.key.get_pressed()

    #ROTATING OVERALL CUBE
    if key[pygame.K_w]: #UP
        globals.rotateAngle = -0.05
        bigCube.rotateCube('x', globals.rotateAngle)
        bigCube.update2DCords()
        
        #GOING TO HAVE A LIST OF ALL SMALL CUBES
        #LOOP THROUGH AND DO THIS
        smallCube.rotateCube('x', globals.rotateAngle)
        smallCube.update2DCords()

    if key[pygame.K_s]: #DOWN
        globals.rotateAngle = 0.05
        bigCube.rotateCube('x', globals.rotateAngle)
        bigCube.update2DCords()
        smallCube.rotateCube('x', globals.rotateAngle)
        smallCube.update2DCords()

    if key[pygame.K_a]: #LEFT
        globals.rotateAngle = 0.05
        bigCube.rotateCube('y', globals.rotateAngle)
        bigCube.update2DCords()
        smallCube.rotateCube('y', globals.rotateAngle)
        smallCube.update2DCords()

    if key[pygame.K_d]: #RIGHT
        globals.rotateAngle = -0.05
        bigCube.rotateCube('y', globals.rotateAngle)
        bigCube.update2DCords()
        smallCube.rotateCube('y', globals.rotateAngle)
        smallCube.update2DCords()

    screen.fill(globals.BLACK)
    
    bigCube.draw(screen)
    
    #trying to colour stuff
    #pygame.draw.polygon(screen, globals.RED, [(bigCube2DPoints[0][0]), (bigCube2DPoints[1][0]), (bigCube2DPoints[3][0]), (bigCube2DPoints[2][0])])

    #DRAWING SMALLCUBE

    #verticies
    #for p in smallCube2DPoints:
    #    pygame.draw.circle(screen, globals.WHITE, (p[0][0], p[0][1]), 2)
    
    bigCube.draw(screen)
    smallCube.draw(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False 
    pygame.display.update()
    clock.tick(10)
pygame.quit()