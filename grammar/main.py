matrix = [[1,2],[3,4]]
row=[1 in row for row in matrix]
print(row)
col=[2 in col for col in zip(*matrix)]
print(col)