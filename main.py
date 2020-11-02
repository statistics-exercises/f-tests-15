import numpy as np
import scipy.stats

def testStatistic( data ) : 
  # Your code to calculate the test statistic from the input data
  # goes here
  

def pvalue( data ) : 
  # Your code to compute the p-value goes here
  
  
mydata = np.loadtxt("mydata.dat")
print("Null hypothesis: The expectations of the distributions that have been sampled are all identical")
print("Alternative hypothesis: The expectations of the distributions are not all identical")
print("The p-value for this hypothesis test is", pvalue( mydata ) )
