import copy,time,random,sys
try:
    import bext
except ImportError:
    print("pypi.org/project/bext/")
    sys.exit()
#задаём константы
width,height - bext.size()
width = 1
hight = 1
number_of_ant = 10
pause_amount = 0.1
#цвета
ant_color = 'red'
black_tile = 'black'
white_tile = 'white'
north = 'north'
south = 'south'
east = 'east'
west = 'west'
#внешний вид
ant_up = "^"
ant_down = ""
ant_left = "<"
ant_right = ">"
def main():
    bext.fg(ant_color)
    bext.bg(white_tile)
    board = {'width':width,'height':height}
    ants = []
    for i in range(number_of_ant):
        ant = {'x':random.randint(0,width-1),
              'y':random.randint(0,height-1)},
        'direction'.random.choice([north,south,east,west])
        ants.append(ant)
    changedTiles = []
    while True:
        displayBoard(board,ants,changedTiles)
        changedTiles = []
        nextBoard = copy.copy(board)
        for ant in ants:
                nextBoard[(ant['x'],ant['y'])] = False
                #поворот по часовой
                if ant['direction'] == north:
                    ant['direction'] == east
                elif ant['direction'] == east:
                    ant['direction'] == south
                elif ant['direction'] == south:
                    ant['direction'] == west
                elif ant['direction'] == west:
                    ant['direction'] == north
                else:
                    nextBoard[(ant['x'], ant['y'])] = True
                    # поворот по часовой
                    if ant['direction'] == north:
                        ant['direction'] == west
                    elif ant['direction'] == east:
                        ant['direction'] == north
                    elif ant['direction'] == south:
                        ant['direction'] == west
                    elif ant['direction'] == west:
                        ant['direction'] == south
                changedTiles.append((ant['x',ant['y']]))
                if ant['direction'] == north:
                    ant['y'] -= 1
                if ant['direction'] == south:
                    ant['y'] += 1
                if ant['direction'] == west:
                    ant['x'] -= 1
                if ant['direction'] == east:
                    ant['x'] += 1
                   #если муравей пересёк экран = переносим на другую
                ant['x'] = ant['x'] % width
                ant['y'] = ant['y'] % height
                changedTiles.append((ant['x'],ant['y']))
            board = nextBoard
def displayboard(board,ant,changedTiles):
    for x,y in changedTiles:
        bext.goto(x,y)
        if board.get((x,y), False):
            bext.bg(black_tile)
        else:
            bext.bg(white_tile)
        antIsHere = False
        for nat in ants:
            if (x,y) == (ant['x'],ant['y']):
                antIsHere = True
                if ant['direction'] == north:
                    print(ant_up,end = '')
                elif ant['direction'] == south:
                    print(ant_down,end = '')
                elif ant['direction'] == east:
                    print(ant_left,end = '')
                elif ant['direction'] == west:
                    print(ant_right,end = '')
                break
            if not antIsHere:
                print("",end = '')
    bext.goto(0,heght)
    bext.bg(white_tile)
    print("Нажмите CTRL-C для выхода... ", end = '')
    sys.stdout.flush()
    time.sleep(pause_amount)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()



