class Dog:
    """A class reprensenting a real-life [dog](https://en.wikipedia.org/wiki/Dog).

    Attributes
    ----------
    name: str
        The name of the dog
    age: int
        The age of the dog
    race: str
        The name of the dog's race
    """

    def __init__(self, name: str, age: int, race: str) -> None:
        self.name = name
        self.age = age
        self.race = race

    def bark(self) -> str:
        """Create a text of the dog barking

        Returns
        -------
        str
            A text describing the dog barking
        """
        return f"{self.name} says: Woof!"

    def wave_tail(self) -> str:
        """Create a text of the dog waving its tail

        Returns
        -------
        str
            A text describing the dog waving its tail
        """
        return f"{self.name} waves its tail!"

    def info(self) -> str:
        """Create an informational text about the dog

        Returns
        -------
        str
            The informational string about the dog
        """
        return f"{self.name} is a {self.age} year old {self.race}."


# Test av klassen
if __name__ == "__main__":
    my_dog = Dog("Rex", 5, "Schäfer")
    print(my_dog.bark())
    print(my_dog.wave_tail())
    print(my_dog.info())
