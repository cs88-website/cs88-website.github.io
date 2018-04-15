import re
emails = ["abc@gmail.com", "xyz@hotmail.com", "cat@yahoo.com", "dog@yahoo.com", "giraffe@hotmail.com", "bob@gmail.com", "alice@gmail.com", "tom@gmail.com"] 

def count_addresses_v2(emails):
	counts = {} 
	for s in emails: 
		address = re.search(r'@[a-z]*', s).group(0)[1:] 
		if address in counts.keys(): 
			counts[address] += 1
		else: 
			counts[address] = 1
	return counts 

# Question 1
"*** YOUR CODE HERE ***"

def match_example():
    """Choose a string that will match the given pattern.

    >>> match_example()
    True
    """
    global example
    pattern = r'^[a-z]+$'
    return re.findall(pattern, example)

# Question 2
def match_names(s):
    """Return a list of all the names in the given string.

    >>> match_names("name: Bob, age: 14, name: Amanda, age: 17, name: Tim, age: 30")
    """
    "*** YOUR CODE HERE ***"

# Question 3
def find_vowels(s):
    """Return a list of all the words that start with a vowel in the given string.

    >>> find_vowels('Alpha is the first greek alphabet.')
    ['Alpha', 'is', 'alphabet']
    >>> find_vowels('Eve is an amateur cook.')
    ['Eve', 'is', 'an', 'amateur']
    >>> find_vowels('random words')
    []
    """
    "*** YOUR CODE HERE ***"

# Question 4
def find_gpas(s):
    """Return a list of all the words that start with a vowel in the given string.

    >>> find_gpas('<html><HEAD><TITLE>List of Students</TITLE></HEAD><body BGCOLOR="FFFFFFF"><HR><H1>This is a List of Students in a class at Berkeley</H1><HR><table style="width:20%"><tr><th>Name</th><th>Gender</th> <th>GPA</th></tr><tr><td>Jill Smith</td><td>Female</td> <td>3.7</td></tr><tr><td>Eve Jackson</td><td>Female</td> <td>3.5</td></tr><tr><td>Hannah Summers</td><td>Female</td> <td>2.3</td></tr><tr><td>Noah Johnson</td><td>Male</td> <td>3.2</td></tr><tr><td>Henry Tanner</td><td>Male</td><td>3.6</td></tr><tr><td>Tom Cook</td><td>Male</td><td>2.6</td></tr></table></body></html>')
    ['3.7', '3.5', '2.3', '3.2', '3.6', '2.6']
    """
    "*** YOUR CODE HERE ***"

# Question 5
def find_names(s):
    """Return a list of all the words that start with a vowel in the given string.

    >>> find_names('<html><HEAD><TITLE>List of Students</TITLE></HEAD><body BGCOLOR="FFFFFFF"><HR><H1>This is a List of Students in a class at Berkeley</H1><HR><table style="width:20%"><tr><th>Name</th><th>Gender</th> <th>GPA</th></tr><tr><td>Jill Smith</td><td>Female</td> <td>3.7</td></tr><tr><td>Eve Jackson</td><td>Female</td> <td>3.5</td></tr><tr><td>Hannah Summers</td><td>Female</td> <td>2.3</td></tr><tr><td>Noah Johnson</td><td>Male</td> <td>3.2</td></tr><tr><td>Henry Tanner</td><td>Male</td><td>3.6</td></tr><tr><td>Tom Cook</td><td>Male</td><td>2.6</td></tr></table></body></html>')
    ['Jill Smith', 'Eve Jackson', 'Hannah Summers', 'Noah Johnson', 'Henry Tanner', 'Tom Cook']
    """
    "*** YOUR CODE HERE ***"
