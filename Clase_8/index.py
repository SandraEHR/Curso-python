class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type


gato = Animal('Matt', 'angora')
print(gato.type)
gato.type ='bengali'
print(gato.type)

print('------------')

class Droid:
    def __init__(self, name):
        self.hidden_name = name

    @property
    def name(self) -> str:
        return self.hidden_name

    @name.setter
    def name(self, name: str) -> None:
        self.hidden_name = name

android = Droid('Arthur')        

print(android.name)
android.name = 'C3PO'
print(android.name)

android.hidden_name = 'Sheldon'
print(android.hidden_name)
print(android.name)


print('----------')
class CalculatedValue:
    def __init__(self, name, height):
        self.name = name
        self.height = height

@property
def get_calculate_value(self) -> float:
    return 0.35 * self.height

valuex = CalculatedValue('ratio', 10)

print(f'El {valuex.name} es: {valuex.get_calculate_value}')

print('--------')

class Dog:
    def __init__(self, name):
        self.name = name

#@property
#def 




dog_one.obeys_owner = False
Dog.obeys_owner = False
print(f'{dog_one.name} obedece a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obedece a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obedece a su dueño {dog_three.obeys_owner}')



