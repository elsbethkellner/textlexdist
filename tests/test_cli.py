import subprocess
import os

def test_cli():
    "tests CLI calls library correctly"
    os.chdir(os.path.dirname(__file__))
    completed = subprocess.run(
        ["../find_distance.py",
         "fixtures/example",
         "motivation",
         "development"],
        stdout=subprocess.PIPE)

    output = completed.stdout.decode("utf8")
    assert output == "Shortest distance between motivation and development: 2\n"


def test_binary():
    "tests CLI gives useful error on utf8 decode failure"
    os.chdir(os.path.dirname(__file__))
    completed = subprocess.run(
        ["../find_distance.py",
         "fixtures/binary",
         "motivation",
         "development"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    assert completed.returncode != 0
    output = completed.stderr.decode("utf8")
    assert output == "Binary or non-utf8 file.\n"
