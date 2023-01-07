__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"


class Homeowner:
    def __init__(self, name, address, needs):
        self.name = name
        self.address = address
        self.needs = needs
        self.contracts = []

    def addContracts(self, specialists: list):
        for specialist in specialists:
            if specialist.profession in self.needs:
                self.contracts.append(specialist.name)

    def printContracts(self):
        print(self.contracts)


class Specialist:
    def __init__(self, name):
        self.name = name


class Electrician(Specialist):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "electrician"
        specialists.append(self)


class Painter(Specialist):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "painter"
        specialists.append(self)


class Plumber(Specialist):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "plumber"
        specialists.append(self)


if __name__ == "__main__":
    specialists = []
    alice = Electrician("Alice Aliceville")
    bob = Painter("Bob Bobsville")
    craig = Plumber("Craig Craigsville")

    alfred = Homeowner("Alfred Alfredson", "Alfredslane 123", ["painter", "plumber"])
    bert = Homeowner("Bert Bertson", "Bertslane 123", ["plumber"])
    candice = Homeowner(
        "Candice Candicedottir", "Candicelane 123", ["electrician", "painter"]
    )

    alfred.addContracts(specialists)
    bert.addContracts(specialists)
    candice.addContracts(specialists)

    alfred.printContracts()
    bert.printContracts()
    candice.printContracts()
