

class Servo:
    def __init__(self):
        self.y_min = 0
        self.y_max = 100
        self.steps_per_rev = 400
        self.revs_per_coordinate = 2
        self.current_pos = 30
        self.next_pos = 0
        self.planned_steps = None
        self.direction = False

    def calc_planned_coordinates(self):
        return self.next_pos - self.current_pos

    def calc_planned_revs(self):
        return self.calc_planned_coordinates() * self.revs_per_coordinate

    def update_planned_steps(self):
        self.planned_steps = self.calc_planned_revs() * self.steps_per_rev



    def print_info(self):
        print('-------------------INFO----------------------')
        print('current position: {}'.format(self.current_pos))
        print('moving to: {}'.format(self.next_pos))
        print('y_coordinates to go: {}'.format(str(self.calc_planned_coordinates())))
        print('revs to go: {}'.format(str(self.calc_planned_revs())))
        print('steps to go: {}'.format(str(self.planned_steps)))

        dir = None
        if self.direction == True:
            dir = 'down'
        else:
            dir = 'up'
        print('direction: {}'.format(dir))
        print('---------------------------------------------')


    def run(self):
        self.update_planned_steps()
        if self.planned_steps == 0:
            print("I'm where I'm supposed to be! :--)")
            return

        if self.planned_steps < 0:
            self.direction = False
            self.planned_steps = self.planned_steps - self.steps_per_rev * self.revs_per_coordinate
            self.current_pos -= 1
        else:
            self.direction = True
            self.planned_steps = self.planned_steps + self.steps_per_rev * self.revs_per_coordinate
            self.current_pos += 1
        self.print_info()


    def set_pos(self, pos):
        print('position set to: {}'.format(pos))
        self.next_pos = pos

if __name__ == '__main__':
        s = Servo()

        while True:
            inp = input("next position?")
            if inp < 101:
                s.set_pos(inp)
            s.run()
