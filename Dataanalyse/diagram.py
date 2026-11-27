import matplotlib.pyplot as plt
def show_histogram(data):
    plt.hist(data, bins=20)
    plt.title("Fördelning")
    plt.xlabel("Värde")
    plt.ylabel("Antal")
    plt.show()
