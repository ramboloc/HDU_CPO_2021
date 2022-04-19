# SA Spade A - lab 1 - variant 6

## Laboratory work description

- `Dictionary based on binary-tree`
  - You need to check that your implementation correctly works with Nonevalue.
  - You need to implement functions/methods for getting/setting value by key.

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
- unit tests:
  - advantages -- Unit Tests help you really understand the design of the code you are working on. 
  Instead of writing code to do something, 
  you are starting by outlining all the conditions 
  you are subjecting the code to and what outputs you'd expect from that.
  - disadvantages -- For data structures and black box algorithms unit tests would be perfect,
   but for algorithms that tend to be changed, 
   tweaked or fine tuned, 
   this can cause a big time investment that 
   one might claim is not justified. 
   So use it when you think it actually fits the system and 
   don't force the design to fit to TDD.
- PBT tests:
  - advantages -- PBT can significantly improve test coverage.
  - disadvantages -- It is not a replacement for unit tests at all because Property-based testing is not enough.
