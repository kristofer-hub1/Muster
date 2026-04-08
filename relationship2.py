from abc import ABC, abstractmethod
from enum import Enum


# ---- ENUM ----
class Relationship(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3


# ---- MODEL ----
class Person:
    def __init__(self, name):
        self.name = name


# ---- ABSTRAKTSIOON ----
class RelationshipBrowser(ABC):

    @abstractmethod
    def find_all_children_of(self, name):
        pass


# ---- LOW-LEVEL (realiseerib abstraktsiooni) ----
class Relationships(RelationshipBrowser):

    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


# ---- HIGH-LEVEL ----
class Research:

    def __init__(self, browser: RelationshipBrowser):
        for child in browser.find_all_children_of("John"):
            print(f"John has a child called {child}")


# ---- MAIN ----
parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)