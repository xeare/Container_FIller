TEASPOONS_PER_PINT = 96
TEASPOONS_PER_TABLESPOON = 3
# unit = [pint, tablespoons, teaspoons]


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

        if isinstance(teaspoons, str):
            raise WrongInputType
            print("Please enter a number")

        filled_pints, teaspoons_remaining = self._div_and_mod(
            teaspoons, TEASPOONS_PER_PINT)
        filled_tablespoons, teaspoons_remaining = self._div_and_mod(
            teaspoons_remaining, TEASPOONS_PER_TABLESPOON)
        return self._filled_only([
            ('pints', filled_pints),
            ('tablespoons', filled_tablespoons),
            ('teaspoons', teaspoons_remaining)])
