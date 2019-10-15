#!/usr/bin/python3
import argparse

DEBUG = False

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="pattern, space sepated values wrapped in quotes")
    parser.add_argument("-d", action="store_true", help="If flag is provided debug statements will print to STDOUT")
    parser.add_argument("STRING", help="string to compare to the given pattern")

    return parser.parse_args()


def debug(msg):
    if DEBUG:
        print(f'===>{__name__}:\t{msg} <===')

def is_match(string, pattern):
    string = string.split()
    pattern = pattern.split()
    dict_mapping = dict(zip(string, pattern))
    for index, item in enumerate(string):
        debug(f'ITEM: {item}\t PATTERN: {pattern[index]}\t DICT_MAPPING: {dict_mapping[item]}')
        if pattern[index] != dict_mapping[item]:
            return False
    return True

if __name__ == '__main__':
    args = init()
    DEBUG = args.d

    match = is_match(args.STRING, args.p)
    print(match)
