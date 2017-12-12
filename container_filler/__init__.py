TEASPOONS_PER_PINT = 96
TEASPOONS_PER_TABLESPOON = 3


class ContainerFiller:
    # below function is us in the next one so start with the next one
    def _div_and_mod(self, teaspoons, conversion):
        filled = int(teaspoons / conversion)
        teaspoons_remaining = teaspoons % conversion
        return filled, teaspoons_remaining

    def _only_return_non_zero_values(self, teaspoons):
        return 0

    def calculate(self, teaspoons):
        filled_pints, teaspoons_remaining = self._div_and_mod(
            teaspoons, TEASPOONS_PER_PINT)
        filled_tablespoons, teaspoons_remaining = self._div_and_mod(
            teaspoons_remaining, TEASPOONS_PER_TABLESPOON)
        if filled_pints == 0 and filled_tablespoons == 0:
            return ('teaspoons', teaspoons_remaining)
        else:
            return (
                ('pints', filled_pints),
                ('tablespoons', filled_tablespoons),
                ('teaspoons', teaspoons_remaining))
