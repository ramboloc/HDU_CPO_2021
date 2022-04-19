# SA Spade A - lab 1 - variant 6

## Project structure

- `Dictionary.py` -- implementation of `Dictionary` class.
- `mutable_test.py` -- unit tests for `Dictionary`.

## Features

- `set` : put V<key,value> to dictionary.
- `get` : get value by key.
- `next` : get next value in dictionary
- `next` : judge whether next value is exist.
- `remove` : remove V by key from dictionary.
- `to_list` : convert dictionary to list.
- `from_list` : convert list to dictionary.
- `size` : get the number of storage elements in dictionary.
- `filter` : filter the diction by judge function.
- `member` : query whether the key exists in the dictionary.
- `map` : use function f to map all value in the dictionary.
- `reduce` : use function f to process all value to build a return value in the dictionary.
- `empty` : clear all elements in the dictionary.
- `concat` : merge two dictionaries into one.

## Contribution

- Wu Bin -- all programming work.
- Li Jingwen -- writing README.md

## Changelog

- 29.03.2022 - 2
  - Add test coverage.
- 29.03.2022 - 1
  - Update README. Add formal sections.
- 29.03.2022 - 0
  - Initial

## Design notes

- The elements in the list converted by dictionary should be key value pairs.
- The key value pairs could be a list like [key,value] or tuple(key,value).
- The function to_list will return key value pairs as a tuple.
- The input of from_list should also be a list which elements are key value pairs.