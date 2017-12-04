from unittest import TestCase, main, skip

from expects import expect, equal

from container_filler import ContainerFiller


class TestContainers(TestCase):

    def test_leaves_no_air(self):
        # sut = system under test, in this case the containers
        sut = ContainerFiller()
        containers = sut.calculate(teaspoons=100)
        expect(containers).to(equal(
            (
                ('pints', 1),
                ('tablespoons', 1),
                ('teaspoons', 1))))

    def test_one_teaspoon(self):
        sut = ContainerFiller()
        containers = sut.calculate(teaspoons=1)
        expect(containers).to(equal(
            (
                ('teaspoons', 1))
        ))

    @skip('')
    def test_contains_all_water(self):
        pass


if "__main__" == __name__:
    main()
