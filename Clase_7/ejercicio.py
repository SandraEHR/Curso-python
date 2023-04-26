class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer_phone = manufacturer
        self.screen_size_phone = screen_size
        self.num_cores_phone = num_cores
        self.apps_phone = apps
        self.status_phone = False

    def power_on(self):
        print('Encendido')
        self.power_on = True

    def power_off(self):
        print('Apagado')
        self.power_on = False


galaxy = MobilePhone('Samsung', float(6.4), int(8), ['Whatsapp', 'Instagram', 'Maps'])
print(galaxy.manufacturer_phone, galaxy.screen_size_phone, galaxy.num_cores_phone, galaxy.apps_phone)
