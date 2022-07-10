class Layer:
    def __init__(self):
        self.input = None
        self.output = None
    
    def forward(self, x):
        pass

    def backward(self, gradient, lr=0.01):
        pass