#!/bin/python3

import os
import subprocess
import math
import time

from my_color import *
from my_box import *

d_source = os.path.dirname(os.path.realpath(__file__))
d_dir = os.path.dirname(d_source)
d_config = f"{d_dir}/config"
f_command = f"{d_config}/commands.txt"

final_results = []

def create_bar(percentage: int, name: str) -> str:

    show_percentage = (str(percentage) + "%").ljust(4) if percentage != 100 else "Done".ljust(4)
    number = math.ceil((percentage / 100) * 20)
    fill = '=' * number + ('>' if percentage != 100 else '')

    col = my_color.green if percentage > 66 else my_color.orange if percentage > 33 else my_color.red
    bar = '[' + col + fill.ljust(20) + my_color.default + ']'
    ret = f"{show_percentage} {bar} {name}"
    return ret


def display(n: float, name: str):
    print("{}".format(create_bar(round(n * 100), name)))


def my_tests() -> float:
    f = open(f_command, "r+")
    array, name, i, test_times = [], "", 0, {}
    testing_cathegory = ""
    beforecommand = ""

    for command in f:
        command = command[:-1] if command[-1] == '\n' else command

        i += 1
        if command[0:2] == "::":
            i -= 1
            continue
        if command[0:4] == ">>> ":
            name = command[4:len(command)]
            if name.lower() == "end":
                results = [sum(array) / len(array), testing_cathegory]
                final_results.append(results)
                array, name, testing_cathegory, i = [], "", "", 2
                print()
            else:
                testing_cathegory, i = name, 2
                print(testing_cathegory.upper() + ":")
            continue
        if command[0:2] == '$ ':
            beforecommand = command[2:len(command)]
            i -= 1
            continue
        if i % 3 == 0:
            continue
        if i % 3 == 1:
            name = command
            continue

        name = name[2:]
        start_time = time.time()
        valid_output = subprocess.getoutput(f"{command} | {beforecommand} tcsh")
        end_time = time.time()
        execution_time = end_time - start_time
        your_output = subprocess.getoutput(f"{command} | {beforecommand} ./mysh")
        beforecommand = ""

        res = valid_output == your_output
        array.append(res)
        test_times[name] = execution_time

        if not res:
            f = open(f"{d_config}/test.log", "a")
            f.write(name + ":\n")
            f.write(f"Execution time: {execution_time:.4f} seconds\n")

            box1, size1 = box_that("Yours", your_output.split('\n'))
            box2, size2 = box_that("Correct", valid_output.split('\n'))

            if size2 > size1:
                box1, size1 = box_that("Yours", your_output.split('\n'), size2)
            else:
                box2, size2 = box_that("Correct", valid_output.split('\n'), size1)
            f.write(box1)
            f.write(box2 + "\n\n")
            f.close()

        execution_info = f" ({execution_time:.4f}s)"
        showing = f"{my_color.green}[S]{my_color.default}" if res else f"{my_color.red} [X]{my_color.default}"
        showing = showing.ljust(16).rjust(17)
        print(f"{showing} {name}{execution_info}")
    f.close()


if __name__ == "__main__":
    subprocess.run(["make", "-s", "re"])
    subprocess.run(["make", "-s", "clean"])

    if os.path.exists(f"{d_config}/test.log"):
        os.remove(f"{d_config}/test.log")

    print()
    my_tests()
    [display(x[0], x[1]) for x in final_results]

    print()
    total = sum([x[0] for x in final_results])
    display(total / len(final_results), "Overall")
