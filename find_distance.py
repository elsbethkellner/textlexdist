#!/usr/local/bin/python3
from textdist.finder import find_shortest_distance_iterator, iterator_from_file
from argparse import ArgumentParser
import sys


def parse_args():
    parser = ArgumentParser(
        description="Searches text in <filename> for the occurance of <word1> and <word2>,"
        "and returns the distance between them, measured in words.")
    parser.add_argument('filename', type=str,
                        help="filename of file search")
    parser.add_argument('word1', help="first word to search for")
    parser.add_argument('word2', help="second word to search for")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    with open(args.filename) as fd:
        iter = iterator_from_file(fd)
        try:
            distance = find_shortest_distance_iterator(iter, args.word1, args.word2)
            print(f"Shortest distance between {args.word1} and {args.word2}: {distance}")
        except UnicodeDecodeError as exc:
            print("Binary or non-utf8 file.", file=sys.stderr)
            exit(1)
