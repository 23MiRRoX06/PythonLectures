from abc import ABC, abstractmethod


class AbstractParent(ABC):

    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError


class Mother:

    def __init__(self, age):
        self.age = age
        print("mother constructor")

    def do_work(self):
        print("I am working")

    def do_house_work(self):
        print("listening to music")


class Father(AbstractParent):

    def hello_friend(self):
        pass

    def __init__(self):
        print("father constructor")

    def play_guitar(self):
        print("play guitar")

    def do_house_work(self):
        print("sitting on the sofa and drink beer")


class Daughter(Mother, Father):

    def __init__(self, age=0):
        Mother.__init__(self, age=age)
        Father.__init__(self)

    def do_work(self):
        print("I am working like a horse")

    def hello_friend(self):
        print("hello friend")


class Friend:
    pass


def greet_mother(mother: Mother):
    print("hello mother")
    mother.do_work()


def greet_father(father: Father):
    print("time for beer")
    father.play_guitar()


if __name__ == "__main__":
    daughter = Daughter()
    # daughter.__class__ = Friend
    greet_mother(daughter)
    greet_father(daughter)
    daughter.hello_friend()
    daughter.do_house_work()

    #list
    for x in [daughter]:
        x.do_house_work()

    list_of_shane = ["mother", "pfp", "surprise"]

    #tuple
    vasian = ("11 years", 12, 3.14, daughter)

    #set
    my_set = {23, 11, 10, "call"}
    print(my_set)

    #frozen_set: cannot delete any object(imutable)
    another_set = frozenset("ce")

    #dictionary
    my_dict = {1: "first", "2": 123, (1, 2, 3): "tuple as key"}

