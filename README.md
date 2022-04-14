# SA Spade A - lab 1 - variant 6

## laboratory work description

* `Dictionary based on binary-tree`
  + You need to check that your implementation correctly works with None value
  + You need to implement functions/methods for getting/setting value by key.
  
## Project structure

* `Dictionary.py` -- implementation of `Dictionary` class with `set` , `get` , `remove` , `to_list` , `size` , `filter` , `member` ,`map` and `reduce` features.
* `mutable_test.py` -- unit tests for `Dictionary`.

## Features

* `set` : put V<key,value> to dictionary.
* `get` : get value by key.
* `remove` : remove V by key from dictionary
* `from_list` and `to_list` : store all the values in the dictionary in the linked list.
* `size` : get list's length.
* `filter` : filter the diction by judge function.
* `member` : query whether the key exists in the dictionary.
* `map` : use function f to process all value in the dictionary.
* `reduce` : use function f to process all value in the dictionary.

## Contribution

* Wu Bin -- all programming work.
* Li Jingwen -- writing README.md

## Changelog
* 29.03.2022 - 2 
  + Add test coverage.
* 29.03.2022 - 1
  + Update README. Add formal sections.
* 29.03.2022 - 0
  + Initial

## Design notes
* The key will be stored as a string in the dictionary.
* The input key will also be converted into a string during query.
