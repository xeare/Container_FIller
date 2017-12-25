from operator import itemgetter

conversion = [
(24192, 'barrels'),
(768, 'gallons'),
(192, 'quarts'),
(96, 'pints'),
(49, 'cups'),
(24, 'gills'),
(6, 'fluid ounces'),
(3, 'tablespoons')]

def calculate(teaspoons):
    for value, unit in conversion:        
        #conversion.sort(key=itemgetter(0), reverse=True)
        filled = int(teaspoons/value) 
        teaspoons_remaining = teaspoons % value
        if filled:
            teaspoons = teaspoons_remaining
            print ((unit, filled))
            if teaspoons_remaining == 1 and 2:
                print (('teaspoons', teaspoons_remaining))
            
calculate(10000)
