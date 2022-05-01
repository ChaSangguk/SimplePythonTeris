import pygame
import random
from pygame.locals import *

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 700

GRID_SIZE = 25
GRID_WIDTH = WINDOW_WIDTH / GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT / GRID_SIZE


COLORS=(
    (255, 255, 255),
    (255, 85, 85),
    (100, 200, 115),
    (120, 108, 245),
    (255, 140, 50),
    (50, 120, 52),
    (146, 202, 73),
    (150, 161, 218)
)
BLOCKS=[ 
    [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],#O미노
    [[0, 0, 2, 0], [0, 0, 2, 0], [0, 0, 2, 0], [0, 0, 2, 0]],#I미노
    [[3, 3, 3, 0], [0, 3, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],#T미노
    [[0, 4, 4, 0], [4, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],#S미노
    [[5, 5, 0, 0], [0, 5, 5, 0], [0, 0, 0, 0], [0, 0, 0, 0]],#Z미노
    [[0, 6, 0, 0], [0, 6, 0, 0], [6, 6, 0, 0], [0, 0, 0, 0]],#J미노
    [[7, 0, 0, 0], [7, 0, 0, 0], [7, 7, 0, 0], [0, 0, 0, 0]] #L미노
]
SPEED = 5
GRID = [[0 for x in range(int(GRID_WIDTH))] for x in range(int(GRID_HEIGHT))]
class Block:
    count = 0
    def __init__(self):
        self.postion=[0,0]
    def create(self):
        self.postion=[0,0]
        self.blockType=BLOCKS[random.randrange(0,len(BLOCKS))]
        for i in range(len(self.blockType)):
            for j in range(len(self.blockType)):
                if(self.blockType[i][j]!=0):
                    GRID[self.postion[0]+i][self.postion[1]+j]==self.blockType[i][j]
    def moveDown(self):
        self.deleteTrace()
        if self.isCrashed('Down'):
            self.drawList()
            return False
        
        self.postion[0]+=1
        self.drawList()
        return True
    def moveLeft(self):
        self.deleteTrace()
        if self.isCrashed('Left'):
            self.drawList()
            return
        
        self.postion[1]-=1
        self.drawList()
        pass
    def moveRight(self):
        self.deleteTrace()
        if self.isCrashed('Right'):
            self.drawList()
            return
        self.postion[1]+=1
        self.drawList()
        pass
    def blockRotate(self):
        self.deleteTrace()
        if self.isCrashed('Rotate'):
            return self.blockType
        tempList=ListRotate(self.blockType)
        return tempList
    def drawList(self):
        for i in range(len(self.blockType)):
            for j in range(len(self.blockType)):
                try:
                    if self.blockType[i][j]!=0:
                        GRID[self.postion[0]+i][self.postion[1]+j]=self.blockType[i][j]
                except:
                    continue
    def isCrashed(self,direction):
        match direction:
            case 'Down':
                for i in range(len(self.blockType)):
                    for j in range(len(self.blockType)):
                        if(self.blockType[i][j]!=0):
                            if(self.postion[0]+i>=GRID_HEIGHT-1):
                                return True
                for i in range(len(self.blockType)):
                    for j in range(len(self.blockType)):
                        if(self.blockType[i][j]!=0):
                            if(GRID[self.postion[0]+i+1][self.postion[1]+j]!=0):
                                return True
                            
            case 'Left':
                for i in range(len(self.blockType)):
                    for j in range(len(self.blockType)):
                        if(self.blockType[i][j]!=0):
                            if(self.postion[1]+j<=0):
                                return True
                for i in range(len(self.blockType)):
                    for j in range(len(self.blockType)):
                        if(self.blockType[i][j]!=0):
                            if(GRID[self.postion[0]+i][self.postion[1]+j-1]!=0):
                                return True
            case 'Right':
                for i in range(len(self.blockType)):
                    for j in range(len(self.blockType)):
                        if(self.blockType[i][j]!=0):
                            if(self.postion[1]+j>=GRID_WIDTH-1):
                                return True
                for i in range(len(self.blockType)):
                    for j in range(len(self.blockType)):
                        if(self.blockType[i][j]!=0):
                            if(GRID[self.postion[0]+i][self.postion[1]+j+1]!=0):
                                return True
            case 'Rotate':
                for i in range(len(self.blockType)):
                    for j in range(len(self.blockType)):
                        if(self.blockType[i][j]!=0):
                            if(self.postion[1]+j>=GRID_WIDTH-1):
                                return True
                for i in range(len(self.blockType)):
                    for j in range(len(self.blockType)):
                        if(self.blockType[i][j]!=0):
                            if(self.postion[1]+j<=0):
                                return True
                for i in range(len(self.blockType)):
                    for j in range(len(self.blockType)):
                        if(self.blockType[i][j]!=0):
                            if(self.postion[0]+i>=GRID_HEIGHT-1):
                                return True
                for i in range(len(self.blockType)):
                    for j in range(len(self.blockType)):
                        if(self.blockType[i][j]!=0):
                            if(GRID[self.postion[0]+i+1][self.postion[1]+j]!=0):
                                return True
                            if(GRID[self.postion[0]+i][self.postion[1]+j+1]!=0):
                                return True
                            if(GRID[self.postion[0]+i][self.postion[1]+j-1]!=0):
                                return True
        return False
    def deleteTrace(self):
        for i in range(len(self.blockType)):
            for j in range(len(self.blockType)):
                if(self.blockType[i][j]!=0):
                    #if(self.postion[0]+i<GRID_HEIGHT and self.postion[1]+j<GRID_WIDTH and self.postion[1]+j>=0):
                    GRID[self.postion[0]+i][self.postion[1]+j]=0
        pass

def deleteLine(i):
    for j in range(int(GRID_WIDTH)):
        if (isBlockFilled(i,j)):
            continue
        else:
            return
    Block.count+=1
    GRID.pop(i)
    GRID.insert(0,[0 for k in range(int(GRID_WIDTH))])
def isBlockFilled(x,y):
    if(GRID[x][y]==0):
        return False
    else:
        return True
def isGameOver():
    for i in range(len(GRID[0])):
        if GRID[0][i]!=0:
            return True
    return False
def ListRotate(List):
    NList=[[0 for i in range(len(List))] for j in range(len(List))]
    for i in range(len(List)):
        for j in range(len(List)):
            NList[j][len(List)-1-i]=List[i][j]
    return NList
def main():
    global GRID
    pygame.init()
    

    screen=pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])
    clock=pygame.time.Clock()
    block=Block()
    block.create()
    while 1:
        while True:
            screen.fill((0,0,0))
            for x in range(int(GRID_WIDTH)):
                for y in range(int(GRID_HEIGHT)):
                    num = GRID[y][x]
                    rect = pygame.Rect(x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE, GRID_SIZE)
                    pygame.draw.rect(screen, COLORS[num], rect, 0 if num!=0 else 1)
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    move(event.key,block)
                elif event.type == QUIT:
                    return
            if(not(block.moveDown())):
                for i in range(int(GRID_HEIGHT)):
                    deleteLine(i)
                if isGameOver():
                    break
                block.create()
            pygame.display.flip()
            clock.tick(SPEED)
        
        GRID=[[0 for x in range(int(GRID_WIDTH))] for x in range(int(GRID_HEIGHT))]
def move(key,block):
    match key:
        case pygame.K_DOWN:
            if(not(block.moveDown())):
                for i in range(int(GRID_HEIGHT)):
                    deleteLine(i)
                block.create()
        case pygame.K_LEFT:
            block.moveLeft()
        case pygame.K_RIGHT:
            block.moveRight()
        case pygame.K_UP:
            block.blockType=block.blockRotate()
            block.drawList()
        case pygame.K_SPACE:
            while block.moveDown():
                pass

main()
