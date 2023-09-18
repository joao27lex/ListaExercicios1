class Calc: 
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0

    def read_nums(self):
        self.n1 = int(input('Write an integer number: '))
        self.n2 = int(input('Write another integer number: '))
        self.n3 = float(input('Write a real number: '))

    def a(self):
        result = (2 * self.n1) * (self.n2/2)
        print(f'The result of option A is {result}')

    def b(self):
        resultado = (3 * self.n1) + self.n3
        print(f'The result of option B is: {resultado}')

    def c(self):
        resultado = (self.n3)**3
        print(f'The result of option C is: {resultado}')

    def execute(self):
        print('What do you want to do with your input numbers?')
        print('=-'*15)
        print(f'A = (2x{self.n1}) * ({self.n2}/2)')
        print(f'B = (3x{self.n1}) + ({self.n3})')
        print(f'C = ({self.n3})³')
        print('=-'*15)
        choice = str(input('Choose between options A, B or C: ')).title().strip()[0]

        if choice == 'A':
            self.a()
        elif choice == 'B':
            self.b()
        elif choice == 'C':
            self.c()
        else:
            print('Choose an existing option.')

calculator = Calc()
calculator.read_nums()
calculator.execute()