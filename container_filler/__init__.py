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
        end_result = []
        if not isinstance(teaspoons, int):
            raise WrongInputType("Please give a number")

        for value, unit in conversion:
            filled = int(teaspoons/value)
            teaspoons_remaining = teaspoons % value
            teaspoons = teaspoons_remaining
            if filled:
                end_result = end_result + [(unit,filled)]
        return end_result
