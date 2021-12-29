

class Zoo:
    def __init__(self):
        self.animals = {'squirrel': 3}
        self.employees = ['John']
        self.animal_count = 3

    def add_animal(self, animal='squirrel'):
        if self.animal_count / len(self.employees) > 10:
            print('Not enough employees! Can not take care of a new animal!')
            return

        if animal in self.animals.keys():    # if animal in ['squirrel']
            # self.animals[animal] += 1 is = self.animals[animal] = self.animals[animal] + 1
            self.animals[animal] += 1      # self.animals[animal] is = self.animals['squirrel'] = 3
            self.animal_count += 1
        else:
            self.animals[animal] = 1
            self.animal_count += 1

        if self.animal_count / len(self.employees) > 10:
            print('Not enough employees for all animals! Hire someone new!')

    def remove_animal(self, animal):
        if animal not in self.animals.keys():
            print('Zoo does not have {}'.format(animal))
        else:
            self.animals[animal] -= 1

    def hire_employee(self, new_employee):
        self.employees.append(new_employee)
        print("{}, welcome to the team!".format(new_employee))

    def fire_employee(self, employee=None):
        if employee is None:
            self.employees.pop()
        elif employee not in self.employees:
            print("You are trying to fire someone who is not working in a Zoo!")
        else:
            self.employees.remove(employee)

    def __str__(self):
        output = "Animals\n"
        for animal, quantity in self.animals.items():
            output = output + animal + ": " + str(quantity) + '\n'
        output = output + 'Employees:\n'
        for employee in self.employees:
            output = output + employee + '\n'

        return output


# Testing our Class


zoo = Zoo()

zoo.add_animal('lion')
zoo.add_animal('fox')
zoo.add_animal('bear')
zoo.add_animal('lion')

print(zoo)
zoo.add_animal()
zoo.add_animal()
zoo.add_animal('fox')
zoo.add_animal('rabbit')
print(zoo)

zoo.hire_employee('Steve')
zoo.hire_employee('Yulia')
zoo.fire_employee('Andrew')
zoo.fire_employee()
print(zoo)
