class Lightbulb:
    def __init__(self):
        self.state = "off"

    def change_state(self):
        if self.state == 'on':
            self.state = 'off'
            print('Turning the light off')
        else:
            self.state = 'on'
            print('Turning the light on')
