# %%
l = [4, 1, 3, 5, 2]
dummy = l.copy()

# %%
' '.join([str(_) for _ in l])
# %%

# %%
import math
dummy.sort()
rule = dummy[math.floor((len(dummy)/2))]
# %%
base=[_ for _ in l if _>=rule]
add = [_ for _ in l if _<rule]
re = []
while base or add:
	if base:re.append(base.pop(0))
	if add:re.append(add.pop(0))
print(re)
# %%
