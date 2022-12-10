import cv2
import matplotlib.pyplot as plt
import numpy as np


def gist_one(path, g):
    img = cv2.imread(path,  cv2.IMREAD_GRAYSCALE)
    gist = [0 for i in range(2 ** g)]
    for i in range(112):
        for j in range(92):
            gist[int(img[i][j] // 2 ** (8 - g))] += 1
    return gist


def gist_all(n, g):
    otvet = [[[] for i in range(10)] for j in range(n)]
    for j in range(n):
        otvet[j][0] = gist_one(f"img/etalon/{j+1}.pgm", g)
    for i in range(n):
        for h in range(9):
            otvet[i][h+1] = gist_one(f"img/sh/s{i+1}/{h+2}.pgm", g)
    return otvet

def sravnenie_gist(n, g):
    otvet = gist_all(n, g)
    pravilno = 0
    count = 0
    for i in range(n):
        for h in range(9):
            minimum = 100000000
            mesto = 0
            for j in range(n):
                gist1 = otvet[j][0]
                gist2 = otvet[i][h+1]
                raznica = 0
                for a in range(2 ** g):
                    raznica += abs(gist1[a] - gist2[a])
                if raznica < minimum:
                    mesto = j
                    minimum = raznica
            print(mesto, end=", ")
            if mesto == i:
                pravilno += 1
            count += 1
    #print(pravilno/count, n)


#sravnenie_gist(40, 5)
def gist_one16(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    gist = [[0 for i in range(32)] for j in range(16)]
    for i in range(112):
        for j in range(92):
            gist[(i // 28) * 4 + (j // 23)][int(img[i][j]) // 8] += 1
    otvet = []
    for i in range(16):
        for j in range(32):
            otvet.append(gist[i][j])
    return otvet


def gist_all16(n):
    otvet = [[[] for i in range(10)] for j in range(n)]
    for j in range(n):
        otvet[j][0] = gist_one16(f"img/etalon/{j + 1}.pgm")
    for i in range(n):
        for h in range(9):
            otvet[i][h + 1] = gist_one16(f"img/sh/s{i + 1}/{h + 2}.pgm")
    return otvet


vse_rezultati = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 17], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [16, 16, 16], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 4, 4], [22, 2, 2], [22, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2], [3, 3, 3], [12, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [4, 4, 4], [4, 4, 4], [4, 4, 4], [39, 4, 4], [39, 4, 4], [4, 4, 4], [39, 4, 39], [39, 4, 39], [39, 39, 39], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5], [6, 6, 6], [6, 6, 6], [6, 6, 6], [6, 6, 6], [6, 6, 6], [6, 6, 6], [6, 6, 6], [6, 6, 6], [6, 6, 6], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 3, 7], [8, 8, 8], [8, 8, 8], [8, 8, 8], [8, 8, 8], [37, 37, 37], [37, 37, 37], [37, 22, 22], [8, 8, 8], [3, 8, 8], [9, 9, 9], [9, 8, 8], [9, 8, 8], [9, 22, 22], [9, 22, 22], [9, 9, 9], [9, 9, 9], [9, 37, 37], [9, 3, 3], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 14, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [10, 10, 10], [11, 11, 11], [25, 11, 11], [25, 11, 11], [25, 11, 11], [11, 11, 11], [25, 2, 11], [11, 11, 11], [11, 11, 11], [11, 11, 11], [12, 12, 12], [12, 12, 12], [12, 12, 12], [12, 12, 12], [3, 17, 17], [12, 12, 12], [12, 12, 12], [12, 12, 12], [12, 12, 12], [13, 13, 13], [13, 13, 13], [13, 13, 13], [13, 13, 13], [13, 13, 13], [13, 13, 13], [13, 13, 13], [13, 21, 21], [13, 13, 13], [34, 4, 4], [14, 14, 14], [14, 14, 14], [34, 4, 29], [14, 14, 14], [34, 4, 4], [14, 14, 14], [34, 4, 39], [34, 4, 29], [0, 23, 15], [0, 23, 23], [16, 17, 17], [6, 17, 17], [15, 15, 15], [0, 16, 14], [0, 26, 26], [0, 0, 0], [0, 23, 23], [16, 16, 16], [6, 2, 2], [6, 22, 22], [16, 16, 16], [16, 22, 22], [16, 23, 23], [16, 22, 6], [16, 22, 22], [16, 22, 23], [17, 17, 17], [17, 4, 4], [17, 17, 17], [17, 17, 17], [17, 17, 17], [17, 17, 17], [17, 17, 17], [17, 17, 17], [17, 17, 17], [18, 18, 18], [18, 18, 18], [18, 18, 18], [18, 18, 18], [18, 18, 18], [18, 18, 18], [26, 18, 18], [18, 1, 14], [18, 18, 18], [29, 28, 29], [32, 29, 29], [19, 28, 28], [19, 19, 19], [19, 28, 28], [19, 19, 19], [29, 29, 29], [19, 19, 19], [32, 28, 28], [20, 20, 20], [20, 20, 20], [30, 20, 20], [30, 20, 20], [30, 20, 30], [29, 20, 20], [20, 20, 20], [29, 20, 20], [30, 20, 20], [21, 21, 21], [21, 21, 21], [21, 21, 21], [21, 21, 21], [21, 21, 21], [21, 21, 21], [21, 21, 21], [21, 21, 21], [21, 21, 21], [22, 22, 22], [22, 22, 22], [22, 22, 37], [2, 8, 8], [22, 22, 22], [22, 22, 22], [22, 22, 22], [22, 22, 37], [22, 22, 22], [23, 23, 23], [23, 23, 23], [23, 23, 23], [23, 23, 23], [23, 23, 23], [23, 23, 23], [23, 23, 23], [23, 23, 23], [23, 23, 23], [24, 24, 24], [24, 24, 24], [24, 4, 4], [24, 4, 4], [24, 24, 24], [24, 24, 24], [24, 4, 4], [24, 24, 24], [24, 24, 24], [25, 25, 25], [25, 25, 25], [25, 25, 25], [25, 25, 25], [25, 25, 25], [25, 25, 25], [25, 39, 39], [25, 25, 25], [25, 39, 39], [26, 26, 26], [26, 26, 26], [26, 26, 26], [26, 26, 26], [26, 26, 3], [26, 10, 10], [26, 26, 26], [26, 26, 26], [26, 26, 26], [13, 14, 14], [27, 27, 27], [13, 18, 18], [13, 14, 14], [27, 27, 27], [13, 18, 18], [27, 36, 36], [16, 16, 16], [27, 27, 27], [28, 28, 28], [28, 28, 28], [29, 28, 28], [29, 28, 28], [29, 28, 28], [29, 28, 28], [37, 28, 28], [28, 28, 28], [28, 28, 28], [29, 29, 29], [29, 29, 29], [29, 29, 29], [29, 29, 29], [29, 29, 29], [29, 29, 29], [29, 29, 29], [29, 29, 29], [29, 29, 29], [33, 21, 21], [33, 33, 33], [33, 33, 33], [33, 33, 33], [30, 30, 30], [30, 30, 30], [30, 30, 30], [30, 30, 30], [33, 33, 33], [31, 31, 31], [31, 31, 31], [31, 31, 31], [31, 31, 31], [31, 31, 31], [31, 6, 14], [31, 31, 31], [31, 31, 31], [31, 1, 31], [32, 32, 32], [32, 32, 32], [32, 32, 32], [32, 32, 32], [32, 32, 32], [32, 32, 32], [29, 29, 29], [32, 32, 32], [32, 32, 32], [33, 33, 33], [33, 33, 33], [33, 33, 33], [33, 33, 33], [33, 33, 33], [33, 33, 33], [33, 33, 33], [33, 33, 33], [33, 33, 33], [34, 24, 24], [34, 4, 4], [34, 24, 24], [34, 39, 39], [2, 3, 24], [34, 24, 24], [34, 24, 24], [27, 39, 39], [34, 39, 39], [23, 22, 22], [15, 6, 6], [16, 6, 6], [35, 35, 35], [15, 16, 23], [23, 23, 23], [16, 6, 6], [14, 6, 6], [15, 16, 16], [25, 13, 13], [36, 36, 36], [25, 13, 13], [25, 13, 13], [25, 13, 13], [36, 36, 36], [25, 21, 13], [36, 36, 36], [36, 36, 36], [37, 22, 22], [37, 37, 37], [37, 3, 3], [37, 37, 37], [37, 37, 37], [37, 37, 37], [37, 22, 22], [37, 37, 37], [37, 22, 22], [38, 38, 38], [38, 38, 38], [38, 38, 38], [38, 38, 38], [28, 28, 28], [38, 38, 38], [38, 38, 38], [38, 38, 38], [28, 28, 28], [39, 39, 39], [39, 39, 39], [4, 4, 4], [39, 39, 39], [34, 4, 4], [39, 39, 39], [2, 39, 39], [39, 39, 39], [4, 4, 4]]
gist_results = [0, 0, 26, 26, 0, 0, 26, 26, 26, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 25, 25, 25, 25, 25, 25, 25, 3, 3, 3, 3, 25, 25, 3, 4, 4, 4, 39, 39, 4, 39, 39, 17, 5, 5, 17, 17, 17, 17, 17, 17, 17, 6, 6, 22, 22, 6, 6, 6, 6, 16, 7, 7, 7, 13, 7, 7, 11, 7, 7, 8, 8, 25, 25, 25, 25, 25, 25, 25, 9, 9, 13, 13, 9, 9, 10, 10, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 25, 25, 25, 25, 11, 25, 11, 11, 11, 12, 12, 12, 17, 12, 17, 17, 12, 17, 13, 13, 13, 13, 13, 13, 13, 13, 13, 34, 14, 14, 34, 14, 34, 14, 34, 34, 0, 0, 6, 16, 15, 0, 0, 0, 0, 16, 16, 16, 16, 6, 6, 18, 6, 6, 17, 17, 17, 4, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 30, 30, 30, 19, 30, 19, 30, 19, 30, 20, 20, 29, 29, 29, 29, 29, 29, 29, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 8, 2, 8, 2, 8, 22, 22, 22, 23, 14, 14, 18, 23, 23, 23, 29, 29, 24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26, 27, 27, 16, 16, 27, 16, 27, 27, 27, 28, 28, 29, 29, 29, 29, 29, 28, 28, 29, 29, 33, 30, 29, 33, 33, 29, 29, 30, 4, 4, 4, 30, 30, 30, 30, 33, 31, 31, 31, 31, 31, 14, 31, 31, 31, 32, 32, 32, 29, 29, 29, 29, 29, 32, 33, 33, 33, 29, 33, 29, 33, 33, 33, 34, 34, 34, 39, 39, 39, 24, 12, 39, 23, 15, 13, 35, 15, 15, 15, 15, 26, 6, 36, 6, 6, 6, 36, 6, 36, 36, 8, 19, 37, 19, 37, 19, 37, 37, 2, 38, 38, 38, 38, 38, 38, 38, 38, 38, 24, 39, 24, 39, 24, 39, 24, 17, 24]
gist16_results = []
'''
x = np.arange(0, 32)
for i in range(40):
    for j in range(9):
        y = gist_one(f"img/etalon/{i+1}.pgm", 5)
        z = gist_one(f"img/sh/s{i+1}/{j+2}.pgm", 5)
        w = gist_one(f"img/etalon/{gist_results[i * 9 + j]+1}.pgm", 5)
        plt.plot(x, y, 'g')
        plt.plot(x, z, 'r')
        plt.plot(x, w, 'b')
        plt.savefig(f"img/gist/{i + 1}.{j + 2}.png")
        plt.close()

'''
x = np.arange(0, 32*16)
for i in range(40):
    for j in range(9):
        y = gist_one16(f"img/etalon/{i+1}.pgm")
        z = gist_one16(f"img/sh/s{i+1}/{j+2}.pgm")
        w = gist_one16(f"img/etalon/{vse_rezultati[i*9 + j][0]+1}.pgm")
        plt.plot(x, y, 'g')
        plt.plot(x, z, 'r')
        plt.plot(x, w, 'b')
        plt.savefig(f"img/gist16/{i + 1}.{j + 2}.png")
        plt.close()
