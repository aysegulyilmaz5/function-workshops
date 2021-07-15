x = [[3,4],[2,7]]
y = [[5,2],[9,4]]

result = [[0,0],[0,0]]

for i in range(len(x)):
  for j in range(len(y)):
    result[i][j] = x[i][j] + y[i][j]
print(result)

