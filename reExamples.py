import re

# find the word pretty
def hasPretty(inp):
    return re.search(r'pretty', inp) != None
print hasPretty('i am pretty so yeah')
print hasPretty('i am not that ahhh')
    
def whichPet(inp):
    result = re.search(r'pet (cat|dog)', inp)
    if result == None:
        return None
    return result.group(1)
print whichPet('my pet cat')
print whichPet('my pet dog was cool')
print whichPet('my pet donkey')


def getAdjs(inp):
    return re.findall(r'\w+y', inp)
    #return re.findall(r'[a-zA-Z0-9_]+y', inp) # the same thing
    #return re.findall(r'\w{1,}y', inp) # the same thing
print getAdjs('the funny book was goofy')

def isEmail(inp):
	result = re.search(r'\w+@\w.+\D{2,4}', inp)
	return result != None
print isEmail('blah@hello.com')
print isEmail('sd$sd@hello.com')

def getTxts(inp):
	tuples = re.findall(r'(\w+.txt )+',inp)
	return tuples

print getTxts('yo.html blah.txt woah.txt he ')		

#str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
#tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
#print tuples  ## [('alice', 'google.com'), ('bob', 'abc.com')]
#for tuple in tuples:
#  print tuple[0]  ## username
#  print tuple[1]  ## host

def percAwesome(inp):
	