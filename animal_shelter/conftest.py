from fifo_animal_shelter import AnimalShelter


@pytest.fixture
def small_animalShelter():
    s = AnimalShelter()
    s.enqueue('dog')
    s.enqueue('cat')
    s.enqueue('dog')
    return s

@pytest.fixture
def cat_animalShelter():
    s = AnimalShelter()
    s.enqueue('cat')
    s.enqueue('cat')
    s.enqueue('cat')
    return c


@pytest.fixture
def empty_animalShelter():
    e = AnimalShelter()
    return e