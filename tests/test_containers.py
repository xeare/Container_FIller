from unittest import TestCase, main, skip

from expects import expect, equal, raise_error

from container_filler import ContainerFiller, WrongInputType


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
    def test_raises_wrong_input_type_on_str(self):
        sut = ContainerFiller()

        def attempt():
            sut.calculate(teaspoons=('aardvark'))
        expect(attempt).to(raise_error(WrongInputType))

    # @skip('')
    def test_exception_msg_on_str(self):
        sut = ContainerFiller()

        def attempt():
            sut.calculate(teaspoons=('aardvark'))
        expect(attempt).to(raise_error(Exception, 'Please give a number'))

    def test_raises_wrong_input_type_on_dict(self):
        sut = ContainerFiller()

        def attempt():
            sut.calculate(teaspoons=({'spam': 42, 'eggs': 'ximinez'}))
        expect(attempt).to(raise_error(WrongInputType))

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


if "__main__" == __name__:
    main()
