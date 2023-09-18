class Fish():
    def __init__(self):
        self.excess = 0
        self.fine = 0

    def read_num(self):
        self.excess = float(input("Write the weight of the amount of fish you've got: ")) - 50

    def execute(self):
        self.fine = self.excess * 4
        print(f'The fine João has to pay R${self.fine:.2f}')

value = Fish()
value.read_num()
value.execute()

    
