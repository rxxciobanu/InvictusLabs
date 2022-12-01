import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np
from scipy import stats as stats
from scipy.stats import rv_continuous, rv_histogram, norm, beta, multivariate_normal
import numpy as np
N = 100000      # number of random variates to generate

def plothist(data, name):
    hist = np.histogram(data, bins=100)
    histdist = rv_histogram(hist)

    X = np.linspace(data.min(), data.max(), 100)
    plt.title(name)
    plt.hist(data, density=True, bins=100)
    plt.plot(X, histdist.pdf(X), label="pdf")
    plt.show()

    
class GenPert(rv_continuous):

 
    def _shape(self, min, mode, max, lmb):
        s_alpha = 1+ lmb*(mode - min)/(max-min)
        s_beta = 1 + lmb*(max - mode)/(max-min)
        return [s_alpha, s_beta]


    def _cdf(self, x, min, mode, max, lmb):
        s_alpha, s_beta = self._shape(min, mode, max, lmb)
        z = (x - min) / (max - min)
        cdf = beta.cdf(z, s_alpha, s_beta)
        return cdf

    def _ppf(self, p, min, mode, max, lmb):
        s_alpha, s_beta = self._shape(min, mode, max, lmb)
        ppf = beta.ppf(p, s_alpha, s_beta)
        ppf = ppf * (max - min) + min
        return ppf


    def _mean(self, min, mode, max, lmb):
        mean = (min + lmb * mode + max) / (2 + lmb)
        return mean

    def _var(self, min, mode, max, lmb):
        mean = self._mean(min, mode, max, lmb)
        var = (mean - min) * (max - mean) / (lmb + 3)
        return var

    def _skew(self, min, mode, max, lmb):
        mean = self._mean(min, mode, max, lmb)
        skew1 = (min + max - 2*mean) / 4
        skew2 = (mean - min) * (max  - mean)
        skew2 = np.sqrt(7 / skew2)
        skew = skew1 * skew2
        return skew

    def _kurt(self, min, mode, max, lmb):
        a1,a2 = self._shape(min, mode, max, lmb)
        kurt1 = a1 + a2 +1
        kurt2 = 2 * (a1 + a2)**2
        kurt3 = a1 * a2 * (a1 + a2 - 6)
        kurt4 = a1 * a2 * (a1 + a2 + 2) * (a1 + a2 + 3)
        kurt5 = 3 * kurt1 * (kurt2 + kurt3)
        kurt = kurt5 / kurt4 -  3                 # scipy defines kurtosis of std normal distribution as 0 instead of 3
        return kurt

    def _stats(self, min, mode, max, lmb):
        mean = self._mean(min, mode, max, lmb)
        var = self._var(min, mode, max, lmb)
        skew = self._skew(min, mode, max, lmb)
        kurt = self._kurt(min, mode, max, lmb)
        return mean, var, skew, kurt


pertm = GenPert(name="pertm")

# step 0: define your targeted correlation matrix

# targeted correlation matrix: volume, price, material unit cost
c_target = np.array(    [[  1.0, -0.3,  0.2],
                        [  -0.3,  1.0,  0.7],
                        [   0.2,  0.7,  1.0]])

# step 1: draw random variates from a multivariate normal distribution 
# with the targeted correlation structure

r0 = [0] * c_target.shape[0]                       # create vector r with as many zeros as correlation matrix has variables (row or columns)
mv_norm = multivariate_normal(mean=r0, cov=c_target)    # means = vector of zeros; cov = targeted corr matrix
rand_Nmv = mv_norm.rvs(N)                               # draw N random variates

# step 2: convert the r * N multivariate variates to scores 
rand_U = norm.cdf(rand_Nmv)   # use its cdf to generate N scores (probabilities between 0 and 1) from the multinormal random variates

# step 3: instantiate the 3 marginal distributions 

# distribution parameters:
min, mode, max, lmb = 8000.0, 12000.0, 18000.0, 4.0         # sales volume, PERT estimae
ms, ss = 20.0, 1.0                                          # selling price, normally distributed
mm, sm = 13.0, 0.7                                          # material unit cost, normally distributed 
o = 3.0                                                     # other unit cost, deterministic    

# instantiate the (uncorrelated) marginal distributions, one for each of the input variables
d_P = pertm(min, mode, max, lmb)                          
d_N1 = norm(ms, ss)                   
d_N2 = norm(mm, sm)      





# draw N random variates for each of the three marginal distributions
# WITHOUT applying a copula

rand_P = d_P.rvs(N)                    # sales volume
rand_N1 = d_N1.rvs(N)                  # selling price
rand_N2 = d_N2.rvs(N)                  # raw material unit cost

# initial correlation structure before applying a copula
c_before = np.corrcoef([rand_P, rand_N1, rand_N2])

def plotcorr(rand1, rand2, name1, name2):
    min1, max1, min2, max2 = rand1.min(), rand1.max(), rand2.min(), rand2.max()
    h = sns.jointplot(rand1, rand2, kind='kde', space=0, fill=True, xlim=(min1, max1), ylim=(min2, max2), stat_func=None);
    h.set_axis_labels(name1, name2, fontsize=16)

# step 4: draw N random variates for each of the three marginal disibutions
# and use as inputs the correlated uniform scores we have generated in step 2

rand_P = d_P.ppf(rand_U[:, 0])                            # sales volume
rand_N1 = d_N1.ppf(rand_U[:, 1])                          # selling price
rand_N2 = d_N2.ppf(rand_U[:, 2])                          # raw material unit cost

c_after = np.corrcoef([rand_P, rand_N1, rand_N2])


# discrepancy of copula-imposed correlations vs targeted correlations
print(c_after - c_target)
# input variables: assign the arrays of N random variables to shorter variable names
v = rand_P                           # sales volume, PERT distributed
p = rand_N1                          # selling price, normally distributed
m = rand_N2                          # material unit cost, normally distributed


# output variables
GP = v * (p - m - o)              # simulation output: Gross Profit
R = v * p                         # simulation output: Revenues
GM = GP / R                       # simulation output: Gross Margin
C = R - GP                        # simulation output: Total Cost





