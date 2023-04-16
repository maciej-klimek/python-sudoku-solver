import time


def drawBoard(brd):
    for y in range(len(brd)):
        if y % 3 == 0 and y != 0:
            print("\n-------------------------------",
                  end=" ")  # rysuje pozdział poziomy
        for x in range(9):
            if x == 0:
                print("\n", end="")
            if x % 3 == 0 and x != 0:
                print("|  ",  end="")  # rysuje pozdział pionowy

            if brd[y][x] == 0:  # zamienia zera na puste pola
                print(" ", " ", end="")
            else:
                print(brd[y][x], " ", end="")
    print("\n")


def checkIfValid(brd, y, x):
    for i in range(0, len(brd)):  # sprawdza pion
        if i != y and brd[y][x] == brd[i][x]:
            return False

    for j in range(0, 9, 1):  # sprawdza poziom
        if j != x and brd[y][x] == brd[y][j]:
            return False

    # ustala współrzędzne kwadratu na planszy
    sqrY = (y//3)*3
    sqrX = (x//3)*3

    for i in range(sqrY, sqrY+3):  # sprawdza kwadrat
        for j in range(sqrX, sqrX+3):
            if (j != x) or (i != y):
                if brd[i][j] == brd[y][x]:
                    return False
    return True


# tworzy liste ze współrzędnymi pól do uzupełnienia
def findOsInBoard(brd):
    resultList = []
    for i in range(0, 9):
        for j in range(0, 9):
            if brd[i][j] == 0:
                resultList.append([i, j])

    return resultList


def solveBoard(brd):
    osList = findOsInBoard(brd)  # lista do uzupełniania
    k = 0
    while k < len(osList):
        y, x = osList[k][0], osList[k][1]  # leci po kolei po tych elementach
        brd[y][x] += 1
        if checkIfValid(brd, y, x) and brd[y][x] <= 9:
            k += 1
            drawBoard(brd)
        else:
            if brd[y][x] >= 9:  # jak dojdzie do 10 bez żadnego solva to znaczy że wcześniej jest błąd ->  zaczyna backtrackować
                brd[y][x] = 0
                k -= 1


def main():

    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    drawBoard(board)
    input()
    solveBoard(board)
    input()


main()
