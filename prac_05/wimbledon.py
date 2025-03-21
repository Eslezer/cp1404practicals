"""
CP1404/CP5632 Practical
Wimbledon Champions
Estimate: 30 minutes
Actual: 45 minutes
"""

FILENAME = "wimbledon.csv"

def load_data(filename):
    """load data from the csv file"""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header
        for line in in_file:
            parts = line.strip().split(',')
            data.append(parts)
    return data


def process_champions(data):
    """count champions and countries"""
    champions = {}
    countries = set()
    for row in data:
        champion = row[2]
        country = row[1]
        champions[champion] = champions.get(champion, 0) + 1
        countries.add(country)
    return champions, countries


def display_results(champions, countries):
    """display champions and countries neatly"""
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def main():
    data = load_data(FILENAME)
    champions, countries = process_champions(data)
    display_results(champions, countries)


main()