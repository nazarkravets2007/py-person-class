class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict[str, object]]) -> list[Person]:
    # Create Person instances using list comprehension
    person_list = [
        Person(
            name=person_data["name"],
            age=person_data["age"],
        )
        for person_data in people
    ]

    # Assign wife / husband using dict.get()
    for person_data in people:
        person = Person.people[person_data["name"]]

        wife_name = person_data.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]

        husband_name = person_data.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]

    return person_list
t
