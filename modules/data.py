import numpy as np
import pandas as pd

def convertDiagnosis(data, col):
    for i in range(len(data[col])):
        if data[col][i] == 0:
            data[col][i] = 18

        elif data[col][i] == -1:
            data[col][i] = 19

        elif data[col][i] <= 139:
            data[col][i] = 1

        elif data[col][i] <= 239:
            data[col][i] = 2

        elif data[col][i] <= 279:
            data[col][i] = 3

        elif data[col][i] <= 289:
            data[col][i] = 4

        elif data[col][i] <= 319:
            data[col][i] = 5

        elif data[col][i] <= 389:
            data[col][i] = 6

        elif data[col][i] <= 459:
            data[col][i] = 7

        elif data[col][i] <= 519:
            data[col][i] = 8

        elif data[col][i] <= 579:
            data[col][i] = 9

        elif data[col][i] <= 629:
            data[col][i] = 10

        elif data[col][i] <= 679:
            data[col][i] = 11

        elif data[col][i] <= 709:
            data[col][i] = 12

        elif data[col][i] <= 739:
            data[col][i] = 13

        elif data[col][i] <= 759:
            data[col][i] = 14

        elif data[col][i] <= 779:
            data[col][i] = 15

        elif data[col][i] <= 799:
            data[col][i] = 16

        else:
            data[col][i] = 17
            
    return data