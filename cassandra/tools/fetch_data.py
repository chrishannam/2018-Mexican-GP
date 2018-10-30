import typing as t


class Driver(t.NamedTuple):
    name: str


class Lap(t.NamedTuple):
    number: int
    times: []


def fetch_race_data_csv(file: str):
    with open(file) as f:
        raw_csv = f.read()
    return raw_csv


def main(url: str):
    fetch_race_data_csv(url)


if __name__ == '__main__':
    # execute only if run as a script
    main('../../data/mexico/lap_data.csv')
