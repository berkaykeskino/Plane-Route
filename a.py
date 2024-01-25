import pygame
import math

pygame.init()

buyutmeOrani = 1

screenWidth = 360 * buyutmeOrani
screenHeight = 180 * buyutmeOrani

screen=pygame.display.set_mode((screenWidth,screenHeight))

map = pygame.image.load("map.jpg")
map = pygame.transform.scale(map, (screenWidth, screenHeight))

go = True

def drawPoints(posX, posY):
    pygame.draw.circle(screen, (10,10,10),(posX[0], posX[1]),screenWidth / 120)
    pygame.draw.circle(screen, (10,10,10),(posY[0], posY[1]),screenWidth / 120)


point1Coordinates = [screenWidth / 2,screenHeight / 2]
point2Coordinates = [screenWidth / 2 + 50,screenHeight / 2]

def pointTouched(mouseCoord, pointCoord):
    x = (mouseCoord[0] - pointCoord[0])**2
    y = (mouseCoord[1] - pointCoord[1])**2
    return (x + y) <= (screenWidth / 120) ** 2

touched1 = False
touched2 = False

def konum(mouseCoord):
    x = mouseCoord[0] - (screenWidth / 2)
    y = -(mouseCoord[1] - (screenHeight / 2))
    meridyen = 180 * x / (screenWidth / 2)
    paralel = 90 * y / (screenHeight / 2)
    return [meridyen, paralel]

radiusOfEarth = 6371
def toSpherical(location):
    y = radiusOfEarth * location[1] / 90
    x = (abs((radiusOfEarth**2 - y**2) ** 0.5)) * math.sin(math.radians(location[0]))
    z = (abs(radiusOfEarth**2 - x**2 - y**2))**0.5
    if not(-90<=location[0]<=90):
        z = -z
    
    return [x, y, z]



def drawLine3D(location1, location2):
    numberOfPoints = 1000
    liste = [[0,0,0] for i in range(numberOfPoints + 1)]
    for i in range(3):
        aralik = (location2[i] - location1[i]) / numberOfPoints
        for j in range(numberOfPoints + 1):
            liste[j][i] = location1[i] + j * aralik
    return liste




def projectLine3D(line):
    for i in range(len(line)):
        element = line[i]
        vectorLength = (abs(element[0] ** 2 + element[1] ** 2 + element[2] ** 2)) ** 0.5
        if vectorLength == 0:
            continue
        multiplier = radiusOfEarth / vectorLength
        for j in range(3):
            line[i][j] *= multiplier
    return line



def findLatitudeLongitude(x, y, z):
    boylam = y * 90 / radiusOfEarth
    if z != 0:
        enlem = math.degrees(math.atan(x/z))
    else:
        enlem = (radiusOfEarth**2 - y**2)**0.5
        if x < 0:
            enlem = -90
        else:
            enlem = 90
    if z < 0 and x <= 0:
        enlem = enlem - screenWidth / (2 * buyutmeOrani)
    elif z < 0 and x > 0:
        enlem = enlem + screenWidth / (2 * buyutmeOrani)
    

    return [enlem, boylam]


bu = True

def drawLine2D(line3D):
    line = [findLatitudeLongitude(i[0],i[1],i[2]) for i in line3D]
    for i in range(len(line) - 1):
        ith = line[i][0]
        next = line[i+1][0]
        if abs(ith - next) > 179 and ith != 180 and ith != -180 and next != 180 and next != -180:
            
            if ith < 0:
                line = line[0:i+1] + [[-180, line[i][1] + (line[i+1][1] - line[i][1])/2]] + [[180, line[i][1] + (line[i+1][1] - line[i][1])/2]] + line[i+1:]
            else:
                line = line[0:i+1] + [[180, line[i][1] + (line[i+1][1] - line[i][1])/2]] + [[-180, line[i][1] + (line[i+1][1] - line[i][1])/2]] + line[i+1:]
            
        if abs(ith - next) == 360:
            continue
        if (i == 0 or i == len(line) - 2) and (ith == 180 or ith == -180):
            continue
        pygame.draw.line(screen, (20,20,20),(ith * screenWidth / 360 + screenWidth / 2,screenHeight / 2 - line[i][1] * screenHeight / 180),(line[i+1][0] * screenWidth / 360 + screenWidth / 2,screenHeight / 2 - line[i+1][1] * screenHeight / 180))
        
    

loc1 = konum(point1Coordinates)
loc1Spherical = toSpherical(loc1)
loc2 = konum(point2Coordinates)
loc2Spherical = toSpherical(loc2)
line = drawLine3D(loc1Spherical, loc2Spherical)
projectLine = projectLine3D(line)

drawLine2D(projectLine)




while go:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go=False
            break
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            if pointTouched(mousePos, point1Coordinates):
                touched1 = not touched1
            elif pointTouched(mousePos, point2Coordinates):
                touched2 = not touched2
            

    screen.blit(map,(0,0))


    
    if touched1:
        point1Coordinates = pygame.mouse.get_pos()
        loc1 = konum(point1Coordinates)
        loc1Spherical = toSpherical(loc1)
        loc2 = konum(point2Coordinates)
        loc2Spherical = toSpherical(loc2)
        line = drawLine3D(loc1Spherical, loc2Spherical)
        projectLine = projectLine3D(line)
        

    if touched2:
        point2Coordinates = pygame.mouse.get_pos()
        loc1 = konum(point1Coordinates)
        loc1Spherical = toSpherical(loc1)
        loc2 = konum(point2Coordinates)
        loc2Spherical = toSpherical(loc2)
        line = drawLine3D(loc1Spherical, loc2Spherical)
        projectLine = projectLine3D(line)
    
    drawLine2D(projectLine)

    drawPoints(point1Coordinates, point2Coordinates)


    pygame.display.update()