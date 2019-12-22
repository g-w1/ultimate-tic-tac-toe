import pygame
pygame.init()
win = pygame.display.set_mode((999,999))
pygame.display.set_caption("Ultimate Tic-Tac-Toe")
myfont = pygame.font.SysFont('Times New Roman', 30)
xdisp = myfont.render('X', False, (0, 0, 0))
odisp = myfont.render('O', False, (0, 0, 0))
counter = "X"
index = []
wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
xcount = 0
ocount = 0
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
        self.long = [Square(self.x0,self.y0),Square(self.x1,self.y0),Square(self.x2,self.y0),
                        Square(self.x0,self.y1),Square(self.x1,self.y1), Square(self.x2,self.y1),
                        Square(self.x0,self.y2), Square(self.x1,self.y2),Square(self.x2,self.y2)]
    def draw1(self):
        for y in range(3):
            for x in range(3):
                self.squares[y][x].draw()
        pygame.draw.line(win,(0,0,0),(self.x1-6,self.y0),(self.x1-6,self.y2+100),11)
        pygame.draw.line(win,(0,0,0),(self.x2-6,self.y0),(self.x2-6,self.y2+100),11)
        pygame.draw.line(win,(0,0,0),(self.x0,self.y1-6),(self.x2+100,self.y1-6),11)
        pygame.draw.line(win,(0,0,0),(self.x0,self.y2-6),(self.x2+100,self.y2-6),11)
    def update1(self):
        global index
        global counter
        for y in range(3):
            for x in range(3):
                if self.clickable == True:
                    self.squares[y][x].clickable = True
                if self.clickable == False:
                    self.squares[y][x].clickable = False
                if clicked(self.squares[y][x].rect) and self.squares[y][x].clickable == True:
                    self.squares[y][x].value = counter
                    if counter == "X":
                        counter = "O"
                    else:
                        counter = "X"
                    self.squares[y][x].done = True
                    self.squares[y][x].clickable = False
                    index = [x,y]
                    return
    def check_win(self):
        global wins
        global xcount
        global ocount
        self.long = []
        for row in self.squares:
            for item in row:
                self.long.append(item)
        for test in wins:
            xcount = 0
            for squares in test:
                if self.long[squares].value == "X":
                    xcount += 1
                if self.long[squares].value == "O":
                    ocount +=1
                if ocount == 3:
                    return "owin"
                if xcount == 3:
                    return "xwin"
                else:
                    return "nullwin"

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
            pygame.draw.rect(win,(140,200,250),(self.x,self.y,100,100))
        if self.done == True:
            pygame.draw.rect(win,(255,100,100),(self.x,self.y,100,100))
        if self.value == "X":
            win.blit(xdisp,(self.x+36,self.y+36))
        if self.value == "O":
            win.blit(odisp,(self.x+36,self.y+36))
screen = [[Board(0*333,0*333),Board(1*333,0*333),Board(2*333,0*333)],
[Board(0*333,1*333),Board(1*333,1*333),Board(2*333,1*333)],
[Board(0*333,2*333),Board(1*333,2*333),Board(2*333,2*333)]]
win.fill((255,255,255))        
run_game = True
while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
    for row in screen:
        for space in row:
            space.update1()
            space.draw1()
            print(space.check_win())
            space.clickable = False
    if index == []:
        for row in screen:
            for space in row:
                space.clickable = True
    else:
        screen[index[1]][index[0]].clickable = True
    pygame.display.update()
pygame.quit()
