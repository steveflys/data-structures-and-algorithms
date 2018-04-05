from .fifo_animal_shelter import Dog, Cat, AnimalShelter
import pytest


@pytest.fixture
def small_animalShelter():
    s = AnimalShelter()
    s.enqueue('dog')
    s.enqueue('cat')
    s.enqueue('dog')
    return s

@pytest.fixture
def cat_animalShelter():
    c = AnimalShelter()
    c.enqueue('cat')
    c.enqueue('cat')
    c.enqueue('Cat()')
    return c


@pytest.fixture
def empty_animalShelter():
    e = AnimalShelter()
    return e