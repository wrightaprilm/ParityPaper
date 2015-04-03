import pandas as pd
from pandas import *
import matplotlib.pyplot as plt
import sys


data = pd.read_csv(sys.argv[1], index_col = False, header = False)
data.columns = ['A','B','C']
h_data = data.pivot(index='A', columns='B', values='C')
h_data.ix[0.1,0.1] = .00012
plt.pcolor(h_data,cmap=plt.cm.RdBu,edgecolors='k')
plt.xticks(np.arange(0.5, len(h_data.columns), 1), h_data.columns)
plt.yticks(np.arange(0.5, len(h_data.index), 1), h_data.index)
cbar = plt.colorbar()
plt.tight_layout()
plt.savefig(sys.argv[2], bbox_inches='tight', dpi=300)

# Copyright (c) <2014> <April Wright, wright.aprilm@gmail.com>
# 
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



