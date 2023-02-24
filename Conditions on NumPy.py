import numpy as np

v = np.array([1, 2, 3, 4, 5])

### with the classical python


ab = []
ab


 for i in v:
     if i < 3:
         ab.append(i)


####################
### with NumPy
#####################################

 v[v <3 ]

 v[v == 3]