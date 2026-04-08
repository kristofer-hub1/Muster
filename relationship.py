from enum import Enum


class Person:
    def __init__(self, name):
        self.name = name


class Relationship(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3


class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))


class Research:
    def __init__(self, relationships):
        # Loeme otse relationships.relations nimekirjast
        for r in relationships.relations:
            person1, rel, person2 = r
            if person1.name == "John" and rel == Relationship.PARENT:
                print(f"John has a child called {person2.name}")


# Näidiskasutus
parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)