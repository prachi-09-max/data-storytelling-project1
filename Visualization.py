#customizing histogram for visualization
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

dataframe=pd.read_csv('0047_Back_Bone_Rd_0.csv')
dataframe.head()
plt.hist(dataframe['frame_number'], color='blue',bins=50)
plt.show()
