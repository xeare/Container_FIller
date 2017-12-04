TEASPOONS_PER_PINT = 96
TEASPOONS_PER_TABLESPOON = 3


class ContainerFiller:

    @staticmethod
    def calculate(teaspoons):
        filled_pints = int(teaspoons / TEASPOONS_PER_PINT)
        teaspoons_remaining = teaspoons % TEASPOONS_PER_PINT
        filled_tablespoons = int(
            teaspoons_remaining / TEASPOONS_PER_TABLESPOON)
        teaspoons_remaining = teaspoons_remaining % TEASPOONS_PER_TABLESPOON
        return (
            ('pints', filled_pints),
            ('tablespoons', filled_tablespoons),
            ('teaspoons', teaspoons_remaining))
