m = [[1,2,3],[3,4,5],[5,6,7]]

for row in m :
	print(row)
  
rez = [[m[i][j] for j in range(len(m))] for i in range(2))] # 'm[j][i]' changed to 'm[i][j]', 'for i in range(len(m[0]))' changed to 'for i in range(2))'

print("\n")

for row in rez:
	print(row)
