# The hypothesis test (again)

Let's just consolidate what you have learned by doing all that again.  This time I have loaded data you are going to test from a file called `mydata.dat`.  The data sampled from each of the 5 distributions I have sampled from are in the __columns__ of this file.  __Your task is to perform a hypothesis test to determine if the expectations of these nine sampled distributions are all the same or not.__

To complete the task you need to complete the code in the two functions in the panel on the left.  These functions are:

1. `testStatistic` - this function takes a 2D NumPy array called `data` in input.  The samples from the four different distribution are contained in the columns of this NumPy array.  You need to calculate the error (SSE) and treatment sum of squares (SST) from `data`.  You then calculate the test statistic from these values.

2. `pvalue` - this function takes a 2D NumPy array called `data` in input.  This function should calculate and return the p-value for the hypothesis test.
