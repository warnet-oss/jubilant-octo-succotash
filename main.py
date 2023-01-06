import math


FIGURES = [
    {'type' : 'round','params' : [3]},
    {'type':'round','params': [3, 4]},
    {'type':'round','params': [4, 10]},
    {'type':'round','params': [9] },
]


def get_square(figure):
    if figure['type'] == 'round':
        return math.pi * figure['params'][0] * figure['params'][0]
    if figure['type'] == 'rectangle':
        return math.pi * figure['params'][0] * figure['params'][1]
    
print(
    sum(
        map(
            get_square,
            FIGURES
        )
    )
)

result = 0
for f in FIGURES:
    result += get_square(f)
print(result)