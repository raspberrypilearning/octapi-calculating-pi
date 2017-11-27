# Viete example
import math

purple = math.sqrt(2)
answer = purple/2

for i in range(25):
    purple = math.sqrt(2+purple)
    answer = answer * (purple / 2)

    print("Pi = " + str(2/answer) )
