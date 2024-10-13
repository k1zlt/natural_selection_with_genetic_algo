import random as ran

class Specimen:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def reproduce(self):
        return [
            Specimen(self.x + 2 * (ran.random() - 0.5), self.y + 2 * (ran.random() - 0.5)),
            Specimen(self.x + 2 * (ran.random() - 0.5), self.y + 2 * (ran.random() - 0.5))
        ]
    
    def __str__(self):
        return f"Specimen({self.x}, {self.y})"
        
if __name__ == "__main__":
    a = Specimen(1, 1)
    print(a)
    b = a.reproduce()
    for i in b:
        print(i)
    

