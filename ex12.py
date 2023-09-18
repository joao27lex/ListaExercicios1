class Weight():
    def __init__(self):
        self.height = 0

    def read_num(self):
        self.height = int(input('Write your height in centimeters: '))/100

    def execute(self):
        result = (72.7 * self.height) - 58
        print(f'Your ideal weight is {result:.2f}kg')

    
ideal_weight = Weight()
ideal_weight.read_num()
ideal_weight.execute()