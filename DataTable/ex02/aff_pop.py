from load_csv import load
import matplotlib.pyplot as plt


def clean(pop_str):
    """
    Preprocesses the population string to convert it into
    a numeric value in standard form.

    Args:
        pop_str (str): Population string with or without
        the 'M' suffix for million.

    Returns:
        float: Numeric population value.
    """
    if pop_str.endswith("M"):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith("k"):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)


def main():
    """
    main
    """
    data = load("population_total.csv")

    campus = "Lebanon"
    country = "Germany"

    germany_data = data[data['country'] == campus].iloc[:, 1:]
    Lebanon_data = data[data['country'] == country].iloc[:, 1:]

    germany_pop = germany_data.values.flatten()
    Lebanon_pop = Lebanon_data.values.flatten()
    years = germany_data.columns.astype(int)

    germany_pop = [clean(pop) for pop in germany_pop]
    Lebanon_pop = [clean(pop) for pop in Lebanon_pop]

    plt.plot(years, germany_pop, label=campus)
    plt.plot(years, Lebanon_pop, label=country)

    plt.title("Population in {}, {}".format(campus, country))
    plt.xlabel("Year")
    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)
    plt.ylabel("Population")
    plt.legend()
    plt.tight_layout()
    max_pop = max(max(germany_pop), max(Lebanon_pop))
    y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
    plt.show()


if __name__ == "__main__":
    main()
