import matplotlib.pyplot as plt
import numpy as np
import json
def bar_chart(numbers, labels, pos):
    c = ['black', 'grey']
    x = np.arange(0,move,10)
    plt.bar(pos, numbers, color=c)
    plt.xticks(x)
    plt.title(title)
    plt.xlabel("moves")
    plt.ylabel("cop")
    
    plt.show()
if __name__ == '__main__':
    numbers = []
    labels = []
    move = 0
    title = input("game number:")
    while True:
        print("")
        cop = int(input("cop: "))
        if cop > 0:
                numbers.append(cop)
                move += 1
                labels.append(move)
                pos = list(range(move))
                print(numbers)
                print(move)
        else:
            jsonStr = json.dumps(numbers)
            with open(title, "w") as tiedosto:
                tiedosto.write(jsonStr)
            bar_chart(numbers, labels, pos)
            quit()
        