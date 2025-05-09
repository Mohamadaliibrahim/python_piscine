import matplotlib.pyplot as plt
from load_csv import load


def main():
    try:
        df = load("../assets/life_expectancy_years.csv")
    except Exception as e:
        print(e)
        exit(0)
    if 'country' not in df.columns:
        print("Not the expected CSV file")
        exit(0)
    df = df.set_index('country')
    if 'France' not in df.index:
        print("Not the expected CSV file")
        exit(0)
    try:
        [int(x) for x in df.loc['France'].index]
    except Exception:
        print("Not the expected CSV file")
        exit(0)
    plt.plot(df.loc['France'])
    plt.title('France Life expectancy Projections')
    plt.ylabel('Life expectancy')
    plt.xlabel('Year')
    plt.xticks([x for x in df.loc['France'].index if (int(x) % 40 == 0)])
    plt.show()


if __name__ == "__main__":
    main()
