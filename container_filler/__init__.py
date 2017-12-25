conversion = [(24192, 'barrels'),  # US liquid
              (768, 'gallons'),
              (192, 'quarts'),
              (96, 'pints'),
              (49, 'cups'),  # exactly 48.6922
              (24, 'gills'),
              (6, 'fluid ounces'),  # equivalent to 'shot'
              (3, 'tablespoons'),
              (1, 'teaspoons')]


class WrongInputType(Exception):
    pass


class ContainerFiller:
    def calculate(self, teaspoons):

        if not isinstance(teaspoons, int):
            raise WrongInputType("Please give a number")

        for value, unit in conversion:
            #  conversion.sort(key=itemgetter(0), reverse=True)
            filled = int(teaspoons/value)
            teaspoons_remaining = teaspoons % value
            teaspoons = teaspoons_remaining
            if filled:
                return [(unit, filled)]


'''
possible?
    def _div_and_mod(self,teaspoons, conversion):
        filled = int(teaspoons / conversion)
        teaspoons_remaining = teaspoons % conversion
        return filled, teaspoons_remaining
    def calculate(self, teaspoons):
        for value, unit in conversion:
        unit, teaspoons_remaining = self._div_and_mod(teaspoons, conversion)
            if filled:
                teaspoons = teaspoons_remaining
                print ((unit, filled))
'''
