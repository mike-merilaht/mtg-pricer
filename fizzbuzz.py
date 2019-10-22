import sys
import json
import argparse

# Set up command line arguments
parser = argparse.ArgumentParser(description="Run customisable fizz buzz")
parser.add_argument(
    "rules", type=str, help="a json string defining the fizz buzz rules"
)
parser.add_argument(
    "--min", type=int, default=1, help="optional minimum value, defaults to 1"
)
parser.add_argument(
    "--max", type=int, default=100, help="optional maximum value, defaults to 100"
)

args = parser.parse_args()

rulesDict = json.loads(args.rules)


def parseOutput(number, ruleDict):
    out = ""
    for name, value in ruleDict.items():
        if number % value == 0:
            out += name
    return out


def checkRules(rules):
    # Make sure that each key in the rule dictionary has an integer as a value
    for key, value in rules.items():
        if (not isinstance(value, int)):
            raise ValueError(f'the key "{key}" in the rules does not have a valid')
    return True


def fizzBuzzRunner(rules, min, max):
    try:
        checkRules(rules)
        for i in range(min, max + 1):
            out = parseOutput(i, rules)
            if out.__len__() == 0:
                out = i
            print(out)
    except ValueError as ve:
        print(ve)

fizzBuzzRunner(rulesDict, args.min, args.max)
