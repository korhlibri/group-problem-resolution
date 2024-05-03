import numpy as np
import matplotlib.pyplot as plt

def plot_score(scores):
    t = [i for i in range(len(scores))]
    print(t)
    print(scores)
    plt.plot(t, scores)
    plt.xlabel("Time") 
    plt.ylabel("Score") 
    plt.savefig('Scores over Epochs.jpg')
    plt.show()

