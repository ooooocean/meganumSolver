import pytest
import pandas as pd
import main

def test_generate_dataframe():
    puzzle = [[0,14,13,20,21,8,0],
          [17,8,4,4,7,2,17],
          [19,4,4,1,8,6,19],
          [9,5,6,6,4,3,9],
          [14,5,8,7,2,4,14],
         [17,3,9,8,8,9,17],
          [0,14,13,20,21,8,0]]

    output = main.generate_dataframe(puzzle)
    assert output[1] == 6
    assert output[2] == 6


def test_intermediate_grid_addition():
    puzzle =    [[0,14,13,20,21,8,0],
                [17,8,4,4,7,2,17],
                [19,4,4,1,8,6,19],
                [9,5,6,6,4,3,9],
                [14,5,8,7,2,4,14],
                [17,3,9,8,8,9,17],
                [0,14,13,20,21,8,0]]

    output = main.generate_dataframe(puzzle)

    inter = main.generate_intermediate("addition",output, 6, 6)
    assert inter.at[1,6] == 8+4+4+7+2
    assert inter.at[2,6] == 4+4+1+8+6
    assert inter.at[3,6] == 5+6+6+4+3
    assert inter.at[4,6] == 5+8+7+2+4
    assert inter.at[5,6] == 3+9+8+8+9

    assert inter.at[6,1] == 8+4+5+5+3
    assert inter.at[6,2] == 4+4+6+8+9
    assert inter.at[6,3] == 4+1+6+7+8
    assert inter.at[6,4] == 7+8+4+2+8
    assert inter.at[6,5] == 2+6+3+4+9

def test_addition_slice():
    test = [[8, True], [4, True], [4, True], [7, True], [2, True]]
    assert main.addition_slice(test) == 25

    test = [[8, True], [4, True], [4, False], [7, True], [2, True]]
    assert main.addition_slice(test) == 21

    test = [[8, False], [4, True], [4, False], [7, True], [2, True]]
    assert main.addition_slice(test) == 13

    test = [[8, False], [4, False], [4, False], [7, False], [2, False]]
    assert main.addition_slice(test) == 0

