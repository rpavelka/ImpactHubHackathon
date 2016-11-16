#!/bin/env python3
"""This file just generates bullshit"""


def filter_out_sentences(raw_korpus: str):
    return ""


def build_probabilities(korpus_fn: str, len_of_sequence):
    """
    Takes a filename, reads the content and prepares list of words to use
    and probabilities of wrod sequences
    """
    with open(korpus_fn) as f:
        raw_korpus = f.read()
    korpus = filter_out_sentences(raw_korpus)
    return korpus.split(" "), dict()


def generate_bullshit(words: list, probabilities: dict):
    return ""


if __name__ == "__main__":
    words, probabilities = build_probabilities("sample_korpus_text_1.txt", 2)
    print(generate_bullshit(words, probabilities))
