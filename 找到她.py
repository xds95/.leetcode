#%%
x_,y_=5,5
tar='HELLOWORLD'
mix='CPUCY\nEKLQH\nCHELL\nLROWO\nDGRBC'
map_o = [list(_) for _ in mix.split('\n')]
# print(map_)
# %%
def findher(map_,tar,x,y):
	if x<0 or x>x_-1 or y<0 or y>y_-1: return False
	if len(tar)>1 and tar[0]==map_[x][y]:
		map_[x][y]='0'
		if findher(map_,tar[1:],x+1,y) or \
		findher(map_,tar[1:],x-1,y) or \
		findher(map_,tar[1:],x,y+1) or \
		findher(map_,tar[1:],x,y-1):
			return True
	elif len(tar)==1 and tar[0]==map_[x][y]:
		return True
	else:
		return False
# %%
for i in range(x_):
	for j in range(y_):
		if findher(map_o,tar,i,j):
			print(i+1,j+1)
# %%

# %%
#x_,y_=5,5
tar='HELLOWORLD'
mix='CPUCY\nEKLQH\nCHELL\nLROWO\nDGRBC'
map_o = [list(_) for _ in mix.split('\n')]

def findher(map_,tar,x,y):
	if x<0 or x>x_-1 or y<0 or y>y_-1: return False
	if len(tar)>1 and tar[0]==map_[x][y]:
		map_[x][y]='0'
		if findher(map_,tar[1:],x+1,y) or \
		findher(map_,tar[1:],x-1,y) or \
		findher(map_,tar[1:],x,y+1) or \
		findher(map_,tar[1:],x,y-1):
			return True
	elif len(tar)==1 and tar[0]==map_[x][y]:
		return True
	else:
		return False

for i in range(x_):
	for j in range(y_):
		if findher(map_o,tar,i,j):
			print(i+1,j+1)