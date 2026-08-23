import matplotlib.pyplot as plt

def read_txt(file_path):
    with open(file_path, 'r') as f:
        return [int(x) for x in f.read().split()]

def plot_histogram(numbers, bins=50):
    plt.hist(numbers, bins=bins, edgecolor='black', color='skyblue')

    plt.xlabel('Scores')
    plt.ylabel('Frequency')
    plt.title('Distribution of Scores')

    plt.grid(axis='y', alpha=0.75)

    plt.show()

if __name__ == "__main__":
    print(read_txt("snake_scores.txt"))
    plot_histogram(read_txt("snake_scores.txt"))
