#!/bin/env python3
"""This file just generates bullshit"""


def filter_out_sentences(raw_korpus: str):
    """
    This should take some crazy string and filter out only complete sentences
    consisting of only words, commas and dots, exclamation marks and question
    marks. Beginning of sentence is capitalized. Return type is string.

    Something like:
    >>> filter_out_sentences("Banik #$%^ pico!!!")
    "Banik pico!"
    """

    return raw_korpus


def build_probabilities(korpus_fn: str, len_of_sequence):
    """
    Takes a filename, reads the content and prepares list of words to use
    and probabilities of word sequences.
    """

    with open(korpus_fn) as f:
        raw_korpus = f.read()

    korpus = filter_out_sentences(raw_korpus)

    return korpus.split(" "), dict()


def generate_bullshit(words: list, probabilities: dict):
    return " ".join(words)


if __name__ == "__main__":
    words, probabilities = build_probabilities("sample_korpus_text_1.txt", 2)
    print(generate_bullshit(words, probabilities))
