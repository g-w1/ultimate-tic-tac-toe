import pygame
pygame.init()
win = pygame.display.set_mode((999,999))
pygame.display.set_caption("Ultimate Tic-Tac-Toe")
myfont = pygame.font.SysFont('Times New Roman', 30)
xdisp = myfont.render('X', False, (0, 0, 0))
odisp = myfont.render('O', False, (0, 0, 0))
counter = "X"
def clicked(rect):
    if pygame.mouse.get_pressed()[0] and pygame.Rect(rect).collidepoint(pygame.mouse.get_pos()):
        return true
class Board:
    def __init__(self,x,y):
        self.rect = (x,y,333,333)
        self.x = x
        self.y = y
        self.width = 333
        self.clickable = True
        self.done = False
        self.x0 = self.x
        self.x1 = self.x +111
        self.x2 = self.x+222
        self.y0 = self.y
        self.y1 = self.y +111
        self.y2 = self.y+222
        self.squares = [[Square(self.x0,self.y0),Square(self.x1,self.y0),Square(self.x2,self.y0)],
                        [Square(self.x0,self.y1),Square(self.x1,self.y1), Square(self.x2,self.y1)],
                        [Square(self.x0,self.y2), Square(self.x1,self.y2),Square(self.x2,self.y2)]]
class Square:
    def __init__(self,x,y):
        self.rect = (x,y,111,111)
        self.y = y
        self.x = X
        self.clickable = True
        self.done = False
        self.value = ""
run_game = True
while run_game:
    win.fill((255,255,255))
    pygame.display.update()
    pass
