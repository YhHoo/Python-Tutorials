'''
THIS IS BUCKY 'Class' and 'Object' EXAMPLES ****
'''


class Enemy:
    life = 10  # This is field of class

    def attack(self):  # this is method one, use self to indicate it is own field
        print("Ouch!")
        self.life -= 1

    def checkLife(self):  # this is method two
        if self.life <= 0:
            print("Enemy is dead")
        else:
            print(self.life)


ali = Enemy()  # this is instantiate a class object
ahkao = Enemy()  # this is instantiate a class object


# this is calling methods from the class
ali.attack()  # -> Ouch!
ali.attack()  # -> Ouch!
ali.checkLife()  # -> 8
ahkao.checkLife()  # -> 10

'''
[CONSOLE]
Ouch!
Ouch!
8
10
'''




'''
THIS IS ‘init’ ****
'''


class Enemy:

    def __init__(self, x):  # this init is a sth that will always be done when we first
        self.energy = x     # instantiate an Obj. All actions will be carried out here
        print("Object initialized Completed")  # energy is initialized as a field now

    def get_energy(self):
        print(self.energy)  # jz normal method


Jason = Enemy(100)
Jason.get_energy()

'''
[CONSOLE]
Object initialized Completed
100
'''





'''
THIS IS Class variable vs Instance Variable ****
'''

class Girl:

    gender = 'Female'  # this is a class variable

    def __init__(self, name):
        self.name = name  # name is called instance variable, it varies for every obj


g1 = Girl('Tracy')
g2 = Girl('Jenny')

print(g1.name)
print(g2.name)
print(g1.gender)
print(g2.gender)

'''
[CONSOLE]
Tracy
Jenny
Female
Female
'''




'''
THIS IS Inheritance ****
'''


class Parent:
    def print_last_name(self):
        print('Roberts')


class Child(Parent):
    def print_first_name(self):
        print('Bucky')

    def print_last_name(self):  # this method wil override the inherited parent method.
        print('Statham')        # bt if no this method, it will not override, and print 'Robert'


human1 = Child()
human1.print_first_name()
human1.print_last_name()


'''
[CONSOLE]
Bucky
Statham
'''



'''
THIS IS MULTIPLE Inheritance ****
'''


class Parent:
    def print_last_name(self):
        print('Roberts')


class Grandparent:
    def print_final_name(self):
        print('Lycan')


class Child(Parent, Grandparent):  # this class inherit 2 other classes
    pass  # this is jz to tell compiler this class has no own methods, all jz inherit, orelse, Error!



human1 = Child()
human1.print_last_name()
human1.print_final_name()

'''
[CONSOLE]
Roberts
Lycan
'''

