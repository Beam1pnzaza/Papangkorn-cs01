from numpy import random
import numpy as np

ran = random.randint(100, size=(5, 10))
NewRan = np.sort(ran)

print(NewRan)