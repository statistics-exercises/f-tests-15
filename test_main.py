import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_testStatistic(self) : 
        mu, sig = np.zeros(5), np.zeros(5) 
        for i in range(5) : 
            mu[i] = sum( mydata[:,i] ) / 50
            sig[i] = ( 50 / 49 )*( sum( mydata[:,i]*mydata[:,i] ) / 50 - mu[i]*mu[i] )

        sse, mut, sst = 49*sum(sig), sum(mu) / 5, 0 
        for i in range(5) : sst = sst + 50*( mu[i] - mut )*( mu[i] - mut )
        F = ( sst / 4 )  / ( sse / 245 )
        self.assertTrue( np.abs( F - testStatistic( mydata ) )<1e-4, "Your code for calculating the test statistic is not working correctly" )
        
    def test_pvalue(self) : 
        F = testStatistic( mydata )
        pval = 1 - scipy.stats.f.cdf( F, 4, 245 )
        self.assertTrue( np.abs( pval - pvalue( mydata ) )<1e-7, "Your code for calculating the p-value is not working correctly" ) 
