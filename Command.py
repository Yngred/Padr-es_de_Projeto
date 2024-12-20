rom typing import List

class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

class GarageDoorOpenCommand(Command):
    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.open()

class GarageDoorCloseCommand(Command):
    def __init__(self, garage_door):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.close()


class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")

class GarageDoor:
    def open(self):
        print("Garage Door is OPEN")

    def close(self):
        print("Garage Door is CLOSED")


class RemoteControl:
    def __init__(self):
        self.commands: List[Command] = []

    def set_command(self, command: Command):
        self.commands.append(command)

    def press_button(self):
        for command in self.commands:
            command.execute()
        self.commands.clear()  


def main():
    
    living_room_light = Light()
    garage_door = GarageDoor()

    light_on_command = LightOnCommand(living_room_light)
    light_off_command = LightOffCommand(living_room_light)
    garage_door_open_command = GarageDoorOpenCommand(garage_door)
    garage_door_close_command = GarageDoorCloseCommand(garage_door)

   
    remote = RemoteControl()

    remote.set_command(light_on_command)
    remote.set_command(garage_door_open_command)
    remote.press_button()  

    remote.set_command(light_off_command)
    remote.set_command(garage_door_close_command)
    remote.press_button()  

if __name__ == "__main__":
    main()