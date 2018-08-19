import subprocess


def test_cli():
    "tests CLI calls library correctly"
    completed = subprocess.run(
        ["./find_distance.py",
         "tests/fixtures/example",
         "motivation",
         "development"],
        stdout=subprocess.PIPE)

    output = completed.stdout.decode("utf8")
    assert output == "Shortest distance between motivation and development: 2\n"
