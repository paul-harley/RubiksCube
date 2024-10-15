import puzzle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

#COLOURS
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
ORANGE = (255,165,0)

coloursDict = {
        0: WHITE,
        1: RED,
        2: ORANGE,
        3: BLUE,
        4: YELLOW,
        5: GREEN
    }


rotateAngle = 0
cubeScale = 200


cubeSides = {
            "left" : 0,
            "front" : 1,
            "right": 2,
            "back": 3,
            "top": 4,
            "bottom": 5
        }
sideWalls = ["left", "front", "right", "back"]

fullPuzzle = puzzle.Puzzle()


#ANGLES BEING ROTATED
# (1 h right) (-1 h left)
# (2 v up) (-2 v down)   



