# Creando una clase

class Transporte:
    pass  # palabra reservada que declara una clase vacía

# Instanciar la clase y crear un objeto
# -declarar una variable y asignar un nombre


transporte_1 = Transporte()
transporte_2 = Transporte()

print(type(transporte_1))

print('-----------')


class Droid:
    def __init__(self):
        self.power_on = False

    def switch_on(self):
        print('Hola soy un droid y estoy a tu orden')
        self.power_on = True

    def switch_off(self):
        print('Adios, enciendeme cuando me necesites')
        self.power_on = False


k8_arthur = Droid()
k8_C3PO = Droid()

k8_arthur.switch_on()
print('power on Arthur: ', k8_arthur.power_on)
k8_C3PO.switch_off()
print('power on C3PO: ', k8_C3PO.power_on)
k8_arthur.switch_off()
print(k8_arthur.power_on)

print('--------------')

class Vehicle:
    def __init__(self, type, model):
        self.type_vehicle = type
        self.model_vehicle = model

sedan = Vehicle('Sedan', 'Aveo')        
print(sedan.type_vehicle, sedan.model_vehicle)
pickup = Vehicle('Pickup', 'Ranger')
print(pickup.type_vehicle, pickup.model_vehicle)



