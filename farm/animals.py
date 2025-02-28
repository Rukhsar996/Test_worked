class Animal:
    """Base class for all animals.

    Attributes:
        name (str): The name of the animal.
        product (str): The product of the animal (e.g., Milk, wool, eggs).
    """

    def __init__(self, name, product):
        """Initialize the animal with a name and product.

        Args:
            name (str): The name of the animal.
            product (str): The product the animal produces.
        """
        self.name = name
        self.product = product
        print('I am inside the class, I was called to make', name, 'to produce', product)


class Cow(Animal):
    def __str__(self):
        return f"{self.name} is giving {self.product}"

    def speak(self, sound):
        """Makes the Animal speak.

        Args:
            sound (str): The sound the animal makes.

        Returns:
            str: A message indicating what sound the animal is making.
        """
        return f"{self.name} is making this sound: {sound}"


class Hen(Animal):
    def __str__(self):
        return f"{self.name} is producing {self.product}"

    def eating(self, food):
        """Shows what Hens eat.

        Args:
            food (str): The food Hens eat.

        Returns:
            str: A message indicating what food Hens eat.
        """
        return f"{self.name} is eating {food}"


class Horse(Animal):
    def __str__(self):
        return f"{self.name} is producing {self.product}"

    def type(self, horse_type):
        """Shows what type of Horse is in the Farm.

        Args:
            horse_type (str): The type of horse.

        Returns:
            str: A message indicating the horse type.
        """
        return f"{self.name} is a {horse_type}"


class Sheep(Animal):
    def __str__(self):
        return f"{self.name} is producing {self.product}"

    def type(self, sheep_type):
        """Shows what type of Sheep is in the Farm.

        Args:
            sheep_type (str): The type of sheep.

        Returns:
            str: A message indicating the sheep type.
        """
        return f"{self.name} is a {sheep_type}"


class Barn:
    """Representing the barn in the farm.

    Attributes:
        capacity (int): Capacity of the Barn in the farm.
        animals_here (list): The number of Animals in the barn.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.animals_here = []

    def move_animal_in(self, animal):
        """Checks if the barn has capacity for the selected animal and moves it in if possible.

        Args:
            animal (Animal): The animal to move in.

        Returns:
            str: A message indicating which animal has been moved in or if capacity is full.
        """
        if len(self.animals_here) < self.capacity:
            self.animals_here.append(animal)
            return f"{animal.name} has been moved in"
        else:
            return "There is not enough capacity in the barn. Please remove one animal before adding a new one!"

    def move_animal_out(self, animal):
        """Moves the selected animal out of the barn.

        Args:
            animal (Animal): The animal to move out.

        Returns:
            str: A message indicating which animal has been removed or if it is not in the barn.
        """
        if animal in self.animals_here:
            self.animals_here.remove(animal)
            return f"{animal.name} has been removed"
        else:
            return f"{animal.name} is not in the barn, check the Field!"

    def check_capacity(self):
        """Checks the current capacity of the barn.

        Returns:
            str: A message indicating the current number of animals in the barn.
        """
        return f"The barn has {len(self.animals_here)} out of {self.capacity} places."


class Field:
    """Representing the Field of the farm.

    Attributes:
        food (str): The available food in the field.
        capacity (int): The capacity of the field.
        on_field_animals (list): The number of animals on the field.
    """

    def __init__(self, food, capacity):
        self.food = food
        self.capacity = capacity
        self.on_field_animals = []

    def add(self, animal):
        """Checks if the field has capacity for the selected animal and moves it in if possible.

        Args:
            animal (Animal): The animal to add to the field.

        Returns:
            str: A message indicating which animal has been brought to the field or if capacity is full.
        """
        if len(self.on_field_animals) < self.capacity:
            self.on_field_animals.append(animal)
            return f"{animal.name} has been brought to the Field"
        else:
            return "There is not enough space on the field, check out the barn!"

    def remove(self, animal):
        """Removes the selected animal from the field.

        Args:
            animal (Animal): The animal to remove from the field.

        Returns:
            str: A message indicating the status of the animal removal.
        """
        if animal in self.on_field_animals:
            self.on_field_animals.remove(animal)
            return f"{animal.name} has been removed from the field"
        else:
            return f"{animal.name} is not on the field, check out the Barn."



