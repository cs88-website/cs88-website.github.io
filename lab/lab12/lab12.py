#############
# Models as HOFs #
#############

# Q1
def polynomial(degree, coeffs):
    """
    >>> fourth = polynomial(4, [3,6,2,1, 100])
    >>> fourth(3)   # 3*(3**4) + 6*(3**3) + 2*(3**2) + 1*(3**1) + 100
    526
    >>> third = polynomial(3, [2, 0, 0, 0])
    >>> third(4)   # 2*(4**3) + 0*(4**2) + 0*(4**1) + 0
    128
    """
    "*** YOUR CODE HERE ***"
    return ______
    


# Q2
def mean(x):
	"""
	Return the mean of x, where x is a list of data points. 

	"""
	"*** YOUR CODE HERE ***"
	return ""

def testmean():
	assert mean([0,0,0,0,0]) == 0, "please pass me!"

	"""***PUT YOUR TEST HERE***"""

def sd(x):
	"""
	Return the standard deviation of x, where x is a list of data points. 

	"""
	"*** YOUR CODE HERE ***"
	return ""

def testsd():
	assert sd([0,0,0,0,0]) == 0, "pass me please!"

	"""***PUT YOUR TEST HERE***"""


def standard_units(x):
	"""
	Return the standard units of x, where x is a list of data points. 
	"""
	"*** YOUR CODE HERE ***"
	return ""

def testsu():
	"""***PUT YOUR TEST HERE***"""


def corr_coeff(x, y):
	"""
	Return the correlation coefficients (r) of x and y, where x is a list of
	data points and y is a list of data points corresponding to x. 

	"""
	"*** YOUR CODE HERE ***"
	return ""

def testcorr_coeff():
	"""***PUT YOUR TEST HERE***"""
	



def regression(points):
    """
    Return a function that takes in x and predicts y, based on a linear regression model. 
    
    >>> tempVIcecream = [[35,1], [33,2], [37,3], [45,5],[47,6],[42,8],[43,9],[51,10]]
    >>> predictor = regression(tempVIcecream)
    >>> predictor(62)    # Round to the third decimal place
    14.597
    """
    "*** YOUR CODE HERE ***"
    return ""

def testregression():
	"""***PUT YOUR TEST HERE***"""
    


