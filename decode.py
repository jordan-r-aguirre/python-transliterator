# This is a transliterator, i.e. it takes written text and transliterates
# it into 26-letter latin alphabet text (lowercase only).
#
# It functions as a rudimentary (and incomplete)
# equivalent to the "unidecode" module:
# https://stackoverflow.com/a/2633310
# https://pypi.org/project/Unidecode/
#
# This script lets you decide which dictionary to use:
# 1. Use a default dictionary ("homoglyphs_bank.json")
# 2. Specify a dictionary (must be .json, in same directory)
# (see homoglyphs_bank.json for syntax and formatting)
#
# The script also lets you decide where the text-to-be-decoded comes from:
# A. From a file in the same directory as the script
# B. As input from the user
#
#
# Credits for the various bits of script are listed below:
# https://www.geeksforgeeks.org/convert-json-to-dictionary-in-python/
# https://www.geeksforgeeks.org/python-replace-words-from-dictionary/~/python3/0015_read_files_1.py
# https://stackoverflow.com/a/69270773
# https://stackoverflow.com/a/68822930
# https://stackoverflow.com/a/8305541
# https://stackoverflow.com/a/13675403
# https://stackabuse.com/converting-json-to-a-dictionary-in-python/
# https://stackoverflow.com/a/66140403
# https://stackoverflow.com/a/55695264
# https://stackoverflow.com/a/4004439
# https://stackoverflow.com/a/45790606


# The script assumes that a json dictionary will be used
import json


# This is the prompt for user input, it is newline, 3 arrows, and a space
# (it sort of looks like a fish: ⮞⮞⮞ )
fish = "\n" + 3*"\u2b9e" + " "


# This is a brief description of what the script does
def description():
    print("""\n
        \r|===\ ABOUT \========================================================|
        \r|--------------------------------------------------------------------|
        \r|                                                                    |
        \r| This is a transliterator script, it transliterates symbols into    |
        \r| latin letters resembling the symbols. Example - it takes the text: |
        \r|                                                                    |
        \r|        νeạʝ ánėnò զàҳ                                              |
        \r|                                                                    |
        \r| And it transliterates it to:                                       |
        \r|                                                                    |
        \r|        veai aneno qax                                              |
        \r|                                                                    |
        \r| NOTE: If you want a more robust transliterator, consider using the |
        \r|       "Unidecode" module, found at:                                |
        \r|                                                                    |
        \r|       https://pypi.org/project/Unidecode/                          |
        \r|                                                                    |
        \r|____________________________________________________________________|
        \n""")


# This opens, reads, byte-encodes, unicode-decodes, json-loads the dictionary.
# Why?
# JSON does not like 32-bit unicode, i.e. \U12345678,
# so these interim variables take the original file,
# open it, read it, then convert it to bytes,
# and finally decode the bytes as proper unicode characters.
def dictionary():
    # a = open the file named "filename"
    a = open(filename)
    # b = read the file named "filename"
    b = a.read()
    # c = convert the contents of filename into ascii characters
    c = bytes(b, 'ascii')
    # d = decode these ascii characters as unicode escape characters;
    # for example, the key-value pair:
    # "\U00001D83" : "g"
    # becomes:
    # "ᶃ" : "g"
    d = c.decode('unicode-escape')
    # e = we need the loaded dictionary to be useable in other bits
    # of the script, so we're setting the fifth variable, "e",
    # as a variable summonable by its parent function name;
    # its job is to load the dictionary
    dictionary.e = json.loads(d)


# The initial prompt to get things started
prompt = input(f"""\nTo decode, select one of the following:
    [1] Use the default dictionary (\"homoglyphs_bank.json\")
    [2] Select another dictionary (must be in same directory)
    [a] Learn more about this script{fish}""")

# If-statements for option 1:
# Summons the custom dictionary() function,
# which reads and loads the default .json dictionary
if prompt == "1":
    filename = "homoglyphs_bank.json"

    # Ask the user to provide a filename containing text to be decoded
    # (must be in same directory as this script)
    prompt_1 = input(f"""\nLoaded \"{filename}\"
    \rPlease select input source that is to be decoded:
    [a] From a file (must be in this directory)
    [b] As input typed by user in terminal{fish}""")

    # If-statements for option 1, sub-option a
    if prompt_1 == "a":
        prompt_1_a = input(f"\nPlease input filename{fish}")
        # Summon the custom dictionary() function
        dictionary()
        # Open the contents of the user-defined file "prompt_1_a",
        # read the contents, make substitutions of non-latin characters
        f = open(prompt_1_a)
        g = f.read()
        for new, old in dictionary.e.items():
            g = g.replace(new, str(old))
        # Print the converted content to the screen
        print("\nHere is the cleaned up string:\n")
        print(g)

    # If-statements for option 1, sub-option b
    if prompt_1 == "b":
        prompt_1_b = input(f"\nPlease input text to be decoded{fish}")
        g = prompt_1_b
        # Summon the custom dictionary() function
        dictionary()
        # Take the user input from the terminal,
        # use the dictionary to substitute any non-latin characters
        for new, old in dictionary.e.items():
            g = g.replace(new, str(old))
        # Print the converted content to the screen
        print("\nHere is the cleaned up string:\n")
        print(g)

    # If-statement that accommodates fat finger syndrome
    if prompt_1 != "a" and prompt_1 != "b":
        print("That input does not make sense.")


# If-statements for option 2:
# Summons the custom dictionary() function,
# which reads and loads the user-defined .json dictionary
if prompt == "2":
    filename = input(f"""\nPlease input the filename of the desired dictionary
    \r(must be in same directory as script){fish}""")
    prompt_2 = input(f"""\nLoaded \"{filename}\"
    \rPlease select input source that is to be decoded:
    [a] From a file (must be in this directory)
    [b] As input typed by user in terminal{fish}""")

    # If-statements for option 2, sub-option a
    if prompt_2 == "a":
        prompt_2_a = input(f"\nPlease input filename{fish}")
        # Summon the custom dictionary() function
        dictionary()
        # Open the contents of the user-defined file "prompt_2_a",
        # read the contents, make substitutions of non-latin characters
        f = open(prompt_2_a)
        g = f.read()
        for new, old in dictionary.e.items():
            g = g.replace(new, str(old))
        # Print the converted content to the screen
        print("\nHere is the cleaned up string:\n")
        print(g)

    # If-statements for option 2, sub-option b
    if prompt_2 == "b":
        prompt_2_b = input(f"\nPlease input text to be decoded{fish}")
        g = prompt_2_b
        # Summon the custom dictionary() function
        dictionary()
        # Take the user input from the terminal,
        # use the dictionary to substitute any non-latin characters
        for new, old in dictionary.e.items():
            g = g.replace(new, str(old))
        # Print the converted content to the screen
        print("\nHere is the cleaned up string:\n")
        print(g)


    # If-statement that accommodates fat finger syndrome
    if prompt_2 != "a" and prompt_2 != "b":
        print("That input does not make sense.")


# If-statement for option a, prints "about" information
if prompt == "a":
    description()


# If-statement that accommodates fat finger syndrome
if prompt != "1" and prompt != "2" and prompt != "a":
    print("\nThat input does not make sense.")
