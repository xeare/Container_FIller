TEASPOONS_PER_TABLESPOON = 3
TEASPOONS_PER_FLUID_OUNCE = 6  # equivalent to 'shot'
TEASPOONS_PER_GILL = 24
TEASPOONS_PER_CUP = 49  # exactly 48.6922
TEASPOONS_PER_PINT = 96
TEASPOONS_PER_QUART = 192
TEASPOONS_PER_GALLON = 768
TEASPOONS_PER_BARREL = 24192  # US liquid


class WrongInputType(Exception):
    pass


class ContainerFiller:
    def _div_and_mod(self, teaspoons, conversion):
        filled = int(teaspoons / conversion)
        teaspoons_remaining = teaspoons % conversion
        return filled, teaspoons_remaining

    def _filled_only(self, containers):
        return [(unit, filled) for unit, filled in containers if filled]

    def calculate(self, teaspoons):

        if not isinstance(teaspoons, int):
            raise WrongInputType("Please give a number")

        filled_barrels, teaspoons_remaining = self._div_and_mod(
            teaspoons, TEASPOONS_PER_BARREL)
        filled_gallons, teaspoons_remaining = self._div_and_mod(
            teaspoons_remaining, TEASPOONS_PER_GALLON)
        filled_quarts, teaspoons_remaining = self._div_and_mod(
            teaspoons_remaining, TEASPOONS_PER_QUART)
        filled_pints, teaspoons_remaining = self._div_and_mod(
            teaspoons_remaining, TEASPOONS_PER_PINT)
        filled_cups, teaspoons_remaining = self._div_and_mod(
            teaspoons_remaining, TEASPOONS_PER_CUP)
        filled_gills, teaspoons_remaining = self._div_and_mod(
            teaspoons_remaining, TEASPOONS_PER_GILL)
        filled_fluid_ounces, teaspoons_remaining = self._div_and_mod(
            teaspoons_remaining, TEASPOONS_PER_FLUID_OUNCE)
        filled_tablespoons, teaspoons_remaining = self._div_and_mod(
            teaspoons_remaining, TEASPOONS_PER_TABLESPOON)
        return self._filled_only([
            ('barrels', filled_barrels),
            ('gallons', filled_gallons),
            ('quarts', filled_quarts),
            ('pints', filled_pints),
            ('cups', filled_cups),
            ('gills', filled_gills),
            ('fluid ounces', filled_fluid_ounces),
            ('tablespoons', filled_tablespoons),
            ('teaspoons', teaspoons_remaining)])
