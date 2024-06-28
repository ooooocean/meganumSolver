import pandas as pd

# take input

# input should be a y+1 by y+1 grid, with no entries in the corners

input = [[0,14,13,20,21,8,0],
          [17,8,4,4,7,2,17],
          [19,4,4,1,8,6,19],
          [9,5,6,6,4,3,9],
          [14,5,8,7,2,4,14],
         [17,3,9,8,8,9,17],
          [0,14,13,20,21,8,0]]

# generate dataframe from input
def generate_dataframe(grid):
    output = pd.DataFrame(grid).astype(object)
    xsize = output.shape[0] - 1
    ysize = output.shape[1] - 1
    return output, xsize, ysize


# generate end values
def generate_intermediate(type, df_nums):
    nums = df_nums[0]
    xsize = df_nums[1]
    ysize = df_nums[2]
    if type == "addition":
        for i in range(1, xsize):
            nums.at[i, ysize] = sum(nums.loc[i,1:ysize-1])
            nums.at[xsize, i] = sum(nums.loc[1:ysize-1, i])
    return nums

