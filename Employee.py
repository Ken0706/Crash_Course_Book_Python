class Employee:
    def __init__(self, f_name, l_name, annual):
        self.firstname = f_name.title()
        self.lastname = l_name.title()
        self.annual = annual

    def give_raise(self, bonus=5000):
        self.annual += bonus
