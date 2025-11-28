import pandas as pd
import numpy as np
from numpy.random import randn

my_data = randn(4,3)
my_rows = ["a", "b","c","d"]
my_cols = ["Monday","Tuesday","wednesday"]
my_df = pd.DataFrame(my_data,my_rows, my_cols) #first data then rows and columns
print(my_df)

