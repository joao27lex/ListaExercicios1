class Weight():
    def __init__(self):
        self.height = 0

    def read_num(self):
        self.height = int(input('Write your height in centimeters: ')) / 100

    def man(self):
        result = (72.7 * self.height) - 58
        print(f'Your ideal weight as a man is {result:.2f}kg')

    def woman(self):
        result = (62.1 * self.height) - 44.7
        print(f'Your ideal weight as a woman is {result:.2f}kg')

    def execute(self):
        sex = str(input('Are you a Man or a Woman [M/W]?  ')).title().strip()[0]
        print('-'*30)

        if sex == 'M':
            self.man()
        elif sex == 'W':
            self.woman()


ideal_weight = Weight()
ideal_weight.read_num()
ideal_weight.execute()
