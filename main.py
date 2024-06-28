import pandas as pd

# take input
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
    # convert grid numbers to include boolean
    for i in range(1, xsize):
        for j in range(1, ysize):
            temp = output.at[i,j]
            output.at[i,j] = [temp, True]
    return output, xsize, ysize

# define helper function for adding values based on operation
def addition_slice(x):
    total = 0
    for gridnum in x:
        if gridnum[1]:
            total += gridnum[0]
    return total

# generate end values
def generate_intermediate(operation, df_nums, xsize, ysize):
    nums = df_nums[0]
    if operation == "addition":
        for i in range(1, xsize):
            temp = nums.loc[i,1:ysize-1]
            nums.at[i, ysize] = addition_slice(temp)
            temp = nums.loc[1:ysize-1, i]
            nums.at[xsize, i] = addition_slice(temp)
    return nums

grid = generate_dataframe(input)
xsize = grid[1]
ysize = grid[2]

# perform logic on each row