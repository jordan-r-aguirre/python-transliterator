================================================================================
=== What the script does =======================================================
================================================================================

This is a transliterator, i.e. it takes written text and transliterates
it into 26-letter latin alphabet text (lowercase only).

It functions as a rudimentary (and incomplete) equivalent to the
"unidecode" module:
https://stackoverflow.com/a/2633310
https://pypi.org/project/Unidecode/

This script lets you decide which dictionary to use:
1. Use a default dictionary ("homoglyphs_bank.json")
2. Specify a dictionary (must be .json, in same directory)
(see homoglyphs_bank.json for syntax and formatting)

The script also lets you decide where the text-to-be-decoded comes from:
A. From a file in the same directory as the script
B. As input from the user



================================================================================
=== Dependencies ===============================================================
================================================================================

Python 3.10
JSON module



================================================================================
=== Usage ======================================================================
================================================================================

python3 000_transliterator.py
[inputs are solicited from within the running script]
