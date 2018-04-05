from .fifo_animal_shelter import Dog, Cat, AnimalShelter
import pytest


def test_empty_val_on_enqueue(empty_animalShelter):
    """test if we try to push a value of None a type erreor will be thrown and the correct message will be displayed"""
    with pytest.raises(TypeError) as e:
        empty_animalShelter.enqueue(None)
    assert str(e.value) == 'Cannot enqueue a value of none'


def test_enqueue_on_small_AnimalShelter(small_animalShelter):
    """test we can push a value into the back of the AnimalShelter"""
    small_animalShelter.enqueue('cat')
    assert isinstance(small_animalShelter.cat_shelter.back.val, Cat)
    assert isinstance(small_animalShelter.long_queue.back.val, str)


def test_dog_dequeue_on_small_AnimalShelter(small_animalShelter):
    """test we can remove the proper animal from an AnimalShelter, decrement the ._size and return the value"""
    assert isinstance(small_animalShelter.dog_shelter.back.val, Dog)
    assert isinstance(small_animalShelter.long_queue.back.val, str)

def test_dog_dequeue_on_cat_AnimalShelter(cat_animalShelter):
    """test we return the proper message if the animal shelter does not contain any matching animals"""
    assert cat_animalShelter.dequeue('dog') == 'Sorry we do not have any of those at this time'

