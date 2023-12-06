class TV():
    def __init__(self):
        self.is_on = False
    def is_on(self):
        is_on = True
    def is_off(self):
        is_on = False
    def show_status(self):
        if self.is_on == True:
            print(f"TV is on")
        else:
            print(f"TV is off")

tv = TV()
tv.show_status()

tv.is_on()
tv.show_status()
