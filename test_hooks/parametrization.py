import pathlib

import pandas


def pytest_generate_tests(metafunc):
    test_scenarios_path = pathlib.Path(f"params/{metafunc.function.__name__}.csv")
    test_params = None
    test_scenarios = None
    if test_scenarios_path.exists():
        tmp = pandas.read_csv(test_scenarios_path, sep=";", header=0).to_dict(orient="records")
        print(tmp)
        test_params = ",".join(list(tmp[0].keys()))
        test_scenarios = [i.values() for i in tmp]

    if test_scenarios:
        metafunc.parametrize(test_params, test_scenarios)