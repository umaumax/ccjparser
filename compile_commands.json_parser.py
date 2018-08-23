#!/usr/bin/env python3

import re
import json
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-exec-format', default='clang-tidy {file} -- {command}')
    parser.add_argument('-file-pattern', default='.*')
    parser.add_argument('-disable-echo-divider', default=False, type=bool)
    parser.add_argument('filepath')

    args, extra_args = parser.parse_known_args()
    file_pattern = args.file_pattern
    exec_format = args.exec_format
    disable_echo_divider = args.disable_echo_divider
    target_filepath = args.filepath

    with open(target_filepath, 'r', encoding='utf-8') as f:
        json_dict = json.loads(f.read())

    for compile_command in json_dict:
        directory = compile_command['directory']
        command = compile_command['command']
        file = compile_command['file']
        if re.search(file_pattern, file):
            command = command.replace("/usr/bin/c++", "")
            if not disable_echo_divider:
                print("echo '#----'")
                print("echo '#---- {file}'".format(file=file))
                print("echo '#----'")
            print(exec_format.format(file=file, command=command, directory=directory))
            if not disable_echo_divider:
                print("echo ''")
                print("echo ''")
                print("echo ''")


if __name__ == '__main__':
    main()
