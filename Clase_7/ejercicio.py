class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []
        self.status = False

    def power_on(self):
        print('Encendido')
        self.status = True

    def power_off(self):
        print('Apagado')
        self.status = False

    def install_apps(self, app):
        self.apps.append(app)

    def uninstall_apps(self, app):
        if app in self.apps:
            self.apps.remove(app)


galaxy = MobilePhone('Samsung', 6.4, 8)
print(galaxy.manufacturer, galaxy.screen_size, galaxy.num_cores)
