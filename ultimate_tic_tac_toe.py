import pygame
pygame.init()
win = pygame.display.set_mode((999,999))
pygame.display.set_caption("Ultimate Tic-Tac-Toe")
myfont = pygame.font.SysFont('Times New Roman', 30)
xdisp = myfont.render('X', False, (0, 0, 0))
odisp = myfont.render('O', False, (0, 0, 0))
counter = "X"
def clicked(rect):
    if pygame.mouse.get_pressed()[0] and rect.collidepoint(pygame.mouse.get_pos()):
        return True
class Board(object):
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
    def draw1(self):
        for y in self.squares:
            for x in y:
                x.draw()
    def update1(self):
        for square in self.squares:
            for indiv in square:
                indiv.update()
class Square(object):
    def __init__(self,x,y):
        self.rect = (x,y,111,111)
        self.y = y
        self.x = x
        self.clickable = True
        self.done = False
        self.value = ""
        self.rect = pygame.Rect(self.x,self.y,111,111)
    def draw(self):
        if self.clickable == True:
            pygame.draw.rect(win,(0,200,0),(self.x,self.y,100,100))
        if self.clickable == False or self.done == True:
            pygame.draw.rect(win,(200,0,0),(self.x,self.y,100,100))
        if self.value == "X":
            win.blit(xdisp,(self.x+36,self.y+36))
        if self.value == "O":
            win.blit(odisp,(self.x+36,self.y+36))
    def update(self):
        global counter
        if clicked(self.rect) and self.clickable == True:
            self.value == counter
            if counter == "X":
                counter = "O"
            else:
                counter = "X"
            self.done = True
            self.clickable = False
        
run_game = True
screen = []
for y in range(3):
    for x in range(3):
        screen.append(Board(x*333,y*333))
while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
    win.fill((255,255,255))
    for space in screen:
        space.draw1()
        space.update1()
    pygame.display.update()
pygame.quit()
print(screen)
