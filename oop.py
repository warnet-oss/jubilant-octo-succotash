import math


FIGURES = [
    {'type' : 'round','params' : [3]},
    {'type':'round','params': [3, 4]},
    {'type':'round','params': [4, 10]},
    {'type':'round','params': [9] },
]


class Figure:
    def square(self) -> float:
        raise Exception('use subclass')


class Round(Figure):
    def __init__(self,radius) -> None:
        self.radius = radius
        
    def square(self) -> float:
        return math.pi * self.radius * self.radius
    
    
class Rectangle(Figure):
    def __init__(self, a, b) -> None:
        super().__init__(a, b)
        
    def square(self) -> float:
        return self.a * self.b
    
class Square(Rectangle):
    def __init__(self, a) -> None:
        super().__init__(a, a) 
        
class FiguresList:
    def __init__(self, figures) -> None:
        self.figures: list[Figure] = []
        for f in figures:
            if f['type'] == 'round':
                self.figures.append(
                 Round(f['params'][0])   
                )
                continue
            if f['type'] == 'rectangle':
                self.figures.append(
                 Rectangle(*f['params'])
                )
                continue
                raise Exception('unknown figure')
        
    def square(self):
        return sum(f.square() for  f in self.figures )
    

figures_list = FiguresList(FIGURES)
print(figures_list.square())