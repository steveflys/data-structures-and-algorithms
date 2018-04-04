from fifo_animal_shelter import AnimalShelter
import pytest


def test_size(empty_animalShelter):
    """test that we can push a val into an empty AnimalShelter and increment the ._size of the AnimalShelter"""
    empty_animalShelter.enqueue('cat').val == 'cat'
    assert empty_animalShelter._size == 1


def test_empty_val_on_enqueue(empty_animalShelter):
    """test if we try to push a value of None a type erreor will be thrown and the correct message will be displayed"""
    with pytest.raises(TypeError) as e:
        empty_animalShelter.enqueue(None)
    assert str(e.value) == 'Cannot enqueue a value of none'


def test_enqueue_on_small_AnimalShelter(small_animalShelter):
    """test we can push a value into the back of the AnimalShelter"""
    small_animalShelter.enqueue('cat')
    assert small_animalShelter.stack_back.top.val == 'cat'


def test_dog_dequeue_on_cat_AnimalShelter(cat_animalShelter):
    """test we can remove a node from the front of a AnimalShelter, decrement the ._size and return the value"""
    cat_animalShelter.dequeue('dog')
    assert empty_animalShelter.dequeue().val == 'Sorry we do not have any dog\'s at this time'
    assert empty_animalShelter._size == 3
