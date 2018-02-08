
### How to group elements in python by n elements? [duplicate]


#####################################################################

theList = ['toi', 'ten', 'la', 'nguyen', 'van', 'minh', 'thaibinh']
N = 3
subList = [theList[n:n+N] for n in range(0, len(theList), N)]

#####################################################################

### output: [['toi', 'ten', 'la'], ['nguyen', 'van', 'minh'], ['thaibinh']]
