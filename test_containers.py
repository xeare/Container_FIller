from unittest import TestCase, main, skip

from expects import expect, equal

from container_filler import ContainerFiller


class TestContainers(TestCase):

    # @skip('')
    def test_leaves_no_air(self):
        # sut = system under test, in this case the containers
        sut = ContainerFiller()
        containers = sut.calculate(teaspoons=100)
        expect(containers).to(equal(
            (
                [('pints', 1),
                    ('tablespoons', 1),
                    ('teaspoons', 1)])))

    # @skip('')
    def test_string_as_input(self):
        sut = ContainerFiller()
        try:
            sut.calculate(teaspoons=('aardvark'))
            assert False, 'No exception was raised'
        except TypeError:
            pass

    # @skip('')
    def test_exception_error_text(self):
        try:
            pass
        except WrongInputType as e:
            expect(str(e)).to(equal('Please give a number'))

    # @skip('')
    def test_ten_thousand_teaspoons(self):
        sut = ContainerFiller()
        containers = sut.calculate(teaspoons=10000)
        expect(containers).to(equal(
            (
                [('pints', 104),
                    ('tablespoons', 5),
                    ('teaspoons', 1)])))

    # @skip('')
    def test_one_teaspoon(self):
        sut = ContainerFiller()
        containers = sut.calculate(teaspoons=1)
        expect(containers).to(equal(
            (
                [('teaspoons', 1)])
        ))

    @skip('')
    def test_contains_all_water(self):
        pass


class WrongInputType(Exception):
    pass


if "__main__" == __name__:
    main()
