
import pygame
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from enum import Enum, auto

from random import random
from time import perf_counter
from Timer import Timer
from Fraction import Fraction
from Vec2 import Vec2

class Edge(Enum):
    RIGHT  = auto()
    LEFT   = auto()
    TOP    = auto()
    BOT    = auto()
    CENTER = auto()

class Game:
    def __init__(self) -> None:

        self.res = 1.0
        self.screenX = int(1920 * self.res)
        self.screenY = int(1080 * self.res)
        self.squareOffset = int(30 * self.res)
        
        self.points = 0
        self.inCicrcle = 0
        self.pointsPerFrame = 10
        self.fps = 60.0

        self.inCircleList = [0, 0, 0, 0, 0, 0, 0, 0]
        self.piAproxList = [0, 0, 0, 0, 0, 0, 0, 0]

        self.relationTextPos = Vec2(self.screenX * 0.6, self.screenY * 0.05)
        self.aproxPiPos = Vec2(self.screenX * 0.6, self.screenY * 0.09)
        self.solutionPiPos = Vec2(self.screenX * 0.615, self.screenY * 0.13)
        self.fpsPos = Vec2(self.screenX * 0.6, self.screenY * 0.17)

        self.setupPygame()
    
    def update(self):
        if self.points >= 50_000_000:
            self.pointsPerFrame = 1_000_000
        elif self.points >= 10_000_000:
            self.pointsPerFrame = 100_000
        elif self.points >= 5_000_000:
            self.pointsPerFrame = 50_000
        elif self.points >= 1_000_000:
            self.pointsPerFrame = 10_000
        elif self.points >= 500_000:
            self.pointsPerFrame = 5_000
        elif self.points >= 200_000:
            self.pointsPerFrame = 1_000
        elif self.points >= 150_000:
            self.pointsPerFrame = 500
        elif self.points >= 50_000:
            self.pointsPerFrame = 200
        elif self.points >= 5_000:
            self.pointsPerFrame = 100
        else:
            self.pointsPerFrame = 10

        self.pointsPerFrame = int(self.pointsPerFrame / 2)

        if self.points >= 1000 and self.inCircleList[0] == 0:
            self.inCircleList[0] = self.inCicrcle
            self.piAproxList[0] = str(round(4 * self.inCicrcle / self.points, 14))
        
        if self.points >= 10_000 and self.inCircleList[1] == 0:
            self.inCircleList[1] = self.inCicrcle
            self.piAproxList[1] = str(round(4 * self.inCicrcle / self.points, 14))
        
        if self.points >= 1_000_000 and self.inCircleList[2] == 0:
            self.inCircleList[2] = self.inCicrcle
            self.piAproxList[2] = str(round(4 * self.inCicrcle / self.points, 14))
        
        if self.points >= 100_000_000 and self.inCircleList[3] == 0:
            self.inCircleList[3] = self.inCicrcle
            self.piAproxList[3] = str(round(4 * self.inCicrcle / self.points, 14))

        self.spawnRandomPoint()
        self.drawOutline()
        
        self.updateText()
        self.updateTable()

    def setupPygame(self):
        pygame.init()
        self.myFont = pygame.font.SysFont("Comic Sans MS", int(30 * self.res))
        self.screen = pygame.display.set_mode((self.screenX, self.screenY))
        # pygame.display.iconify()
        self.screen.fill((0, 0, 0))
        self.clock = pygame.time.Clock()

        self.size = self.screenY - self.squareOffset
        self.squareCorners = [
            (self.squareOffset, self.squareOffset),
            (self.squareOffset, self.size),
            (self.size, self.size),
            (self.size, self.squareOffset)
        ]

        self.center = ((self.squareOffset + self.size) / 2.0, (self.squareOffset + self.size) / 2.0)
        self.radius = (self.size - self.squareOffset) / 2.0

    def drawOutline(self):
        pygame.draw.lines(self.screen, (255, 255, 255), True, self.squareCorners, width=3)
        pygame.draw.circle(self.screen, (255, 255, 255), self.center, self.radius, width=3)

    def spawnRandomPoint(self):
        for _ in range(self.pointsPerFrame):
            x = random() - 0.5
            y = random() - 0.5

            if (x * x + y * y) <= 0.25:
                self.inCicrcle += 1
            self.points += 1

            minVal = self.squareOffset
            maxVal = self.size

            xpos = minVal + (x + 0.5) * (maxVal - minVal)
            ypos = minVal + (y + 0.5) * (maxVal - minVal)
            
            if self.points < 10_000_000:
                pygame.draw.circle(self.screen, (0, 255, 150), (xpos, ypos), 1)

    def updateTable(self):
        top = 0.3 * self.screenY
        bot = 0.42 * self.screenY
        left = 0.65 * self.screenX
        right = 0.7 * self.screenX

        def down(val: Fraction):
            return top - (top - bot) * val.value_aprox()

        def across(val: Fraction):
            return left + (right - left) * val.value_aprox()

        downThird = bot + (top - bot) / 1.5
        upThird = bot + (top - bot) / 3

        third = Fraction(1, 3)
        sixht = Fraction(1, 6)
        offset = self.screenX / 500

        if self.inCircleList[0] != 0:
            self.writePermanent("Points: ", Vec2(left, top), Edge.RIGHT)
            self.writePermanent("In circle: ", Vec2(left, down(third)), Edge.RIGHT)
            self.writePermanent("Pi aprox: ", Vec2(left, down(third * 2)), Edge.RIGHT)
            self.writePermanent("1.000", Vec2(right, top), Edge.RIGHT, offset = offset)
            self.writePermanent(f"{self.inCircleList[0]}", Vec2(right, down(third)), Edge.RIGHT, offset = offset)
            self.writePermanent(f"{self.piAproxList[0]}", Vec2(right, down(third * 2)), Edge.RIGHT, offset = offset)

            pts = [
                (left, top),
                (left, bot),
                (right, bot),
                (right, upThird),
                (left, upThird),
                (left, downThird),
                (right, downThird),
                (right, bot),
                (right, top)
            ]
            pygame.draw.lines(self.screen, (255, 255, 255), True, pts, width=2)
        
        if self.inCircleList[1] != 0:
            new_right = 0.76 * self.screenX
            new_left = right

            self.writePermanent("10.000", Vec2(new_right, top), Edge.RIGHT, offset = offset)
            self.writePermanent(f"{self.inCircleList[1]}", Vec2(new_right, down(third)), Edge.RIGHT, offset = offset)
            self.writePermanent(f"{self.piAproxList[1]}", Vec2(new_right, down(third * 2)), Edge.RIGHT, offset = offset)
            
            pts = [
                (new_left, top),
                (new_right, top),
                (new_right, downThird),
                (new_left, downThird),
                (new_left, upThird),
                (new_right, upThird),
                (new_right, top),
                (new_right, bot),
                (new_left, bot)
            ]

            pygame.draw.lines(self.screen, (255, 255, 255), False, pts, width=2)

        if self.inCircleList[2] != 0:
            new_left = new_right
            new_right = 0.83 * self.screenX

            self.writePermanent("1 million", Vec2(new_right, top), Edge.RIGHT, offset = offset)
            self.writePermanent(f"{self.inCircleList[2]}", Vec2(new_right, down(third)), Edge.RIGHT, offset = offset)
            self.writePermanent(f"{self.piAproxList[2]}", Vec2(new_right, down(third * 2)), Edge.RIGHT, offset = offset)
            
            pts = [
                (new_left, top),
                (new_right, top),
                (new_right, downThird),
                (new_left, downThird),
                (new_left, upThird),
                (new_right, upThird),
                (new_right, top),
                (new_right, bot),
                (new_left, bot)
            ]

            pygame.draw.lines(self.screen, (255, 255, 255), False, pts, width=2)
        
        if self.inCircleList[3] != 0:
            new_left = new_right
            new_right = 0.92 * self.screenX

            self.writePermanent("100 million", Vec2(new_right, top), Edge.RIGHT, offset = offset)
            self.writePermanent(f"{self.inCircleList[3]}", Vec2(new_right, down(third)), Edge.RIGHT, offset = offset)
            self.writePermanent(f"{self.piAproxList[3]}", Vec2(new_right, down(third * 2)), Edge.RIGHT, offset = offset)
            
            pts = [
                (new_left, top),
                (new_right, top),
                (new_right, downThird),
                (new_left, downThird),
                (new_left, upThird),
                (new_right, upThird),
                (new_right, top),
                (new_right, bot),
                (new_left, bot)
            ]

            pygame.draw.lines(self.screen, (255, 255, 255), False, pts, width=2)

    def updateText(self):
        l = self.squareCorners[1][1] + self.squareOffset
        big_rect = pygame.Rect(l, 0, self.screenX, self.screenY)
        self.screen.fill((0, 0, 0), big_rect)
        
        relationText = f"Points in circle vs total: {self.inCicrcle}/{self.points}"
        self.writePermanent(relationText, self.relationTextPos, Edge.LEFT)
        
        piAproxText = f"Aprox value of pi: "
        aproxValue = f"{round(4 * self.inCicrcle / self.points, 14)}"
        
        while len(aproxValue) < 10:
            aproxValue += "0"

        self.writePermanent(piAproxText + aproxValue, self.aproxPiPos, Edge.LEFT)

        piText = f"Real value of pi: 3.1415926535897..."
        self.writePermanent(piText, self.solutionPiPos, Edge.LEFT)

        fpsText = f"{self.pointsPerFrame} points per frame at {round(self.fps)} fps."
        self.writePermanent(fpsText, self.fpsPos, Edge.LEFT)

    def writePermanent(self, text, point: Vec2, edge: Edge = Edge.CENTER, offset: int = 0, fontSize: int = 30):
        if fontSize == int(30 * self.res):
            textRender = self.myFont.render(text, True, (255, 255, 255))
        else:
            fontObj = pygame.font.SysFont("Comic Sans MS", fontSize)
            textRender = fontObj.render(text, True, (255, 255, 255))

        sizeX = textRender.get_width()
        sizeY = textRender.get_height()

        match edge:
            case Edge.CENTER:
                x = point.x - sizeX / 2 - offset
                y = point.y - sizeY / 2
            
            case Edge.RIGHT:
                x = point.x - sizeX - offset
                y = point.y
            
            case Edge.LEFT:
                x = point.x + offset
                y = point.y

        self.screen.blit(textRender, (x, y))

def userInput(key, event):
    global running
    
    if key == K_ESCAPE: 
        running = False

def main():
    global running
    running = True
    
    game = Game()

    iters = 0
    t0_main = perf_counter()
    try:
        while running:
            
            t0 = perf_counter()
            
            for event in pygame.event.get():
                if event.type == QUIT: 
                    running = False

                elif event.type == KEYDOWN: 
                    userInput(event.key, event)

            game.update()
            pygame.display.update()

            t1 = perf_counter()
            game.fps = 1.0 / (t1 - t0)

            iters += 1
            print(f"Current iteration: {iters} in {round(perf_counter() - t0_main)} seconds.", end = "\r")
            pygame.image.save(game.screen, f"images/{iters}.png")
    
    finally:
        pygame.quit()
        print()

if __name__ == "__main__":
    main()
