class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation #Stores the operation function 

    def get_result(self):
        #Call the stored operation
        return self.operation(self.a, self.b)