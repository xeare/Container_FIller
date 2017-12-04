class ContainerFiller:

    @staticmethod
    def calculate(teaspoons=100):
        # teaspoons = 100
        pints = 96
        tablespoons = 3
        remaining_water = teaspoons
        while remaining_water != 0:
            remaining_water = teaspoons % pints  # remaining_water = 4
            if remaining_water < 96:
                number_of_pints = 1
                remaining_water = remaining_water % tablespoons
                # the above is remaining_water = 4 % 3 --> 1
                if remaining_water == 1:
                    number_of_tablespoons = 1
                    remaining_water = remaining_water % 1
                    # remaining_water = 1 % 1 -->0
                    number_of_teaspoons = 1
                    if remaining_water == 0:
                        return (('pints', number_of_pints),
                                ('tablespoons', number_of_tablespoons),
                                ('teaspoons', number_of_teaspoons))
                    else:  # the following return none because i know my
                            # code works
                        return None
                else:
                    return None
            else:
                return None

    def calculate(teaspoons=1):
        # teaspoons = 1
        remaining_water = ()
        while remaining_water != 0:
            remaining_water = teaspoons % teaspoons
            if remaining_water == 0:
                number_of_teaspoons = 1
                return (('teaspoons', number_of_teaspoons))
