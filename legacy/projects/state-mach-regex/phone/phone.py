import re  # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# TODO Define your regex
regex = '\+?([\d]{0,3})[-\s]?\(?(\d{3})\)?\s?\-?(\d{3})\s?\-?(\d{4})'

''' 
\+ --> Looks for the + character
? --> Makes the preceding regex optional
([\d]{0,3}) --> Matches between 0 and 3 digits (country code)
[-\s] --> Matches the - character and any whitespace
? --> Makes the preceding regex optional
\( --> Escapes the (
? --> Makes the preceding regex optional
(\d{3}) --> Matches 3 digits
\) --> Escapes the )
? --> Makes the preceding regex optional
\s --> Matches any whitespace
? --> Makes the preceding regex optional
\- --> Matches the - character
? --> Makes the preceding regex optional
(\d{3}) --> Matches 3 digits
\s --> Matches any whitespace
? --> Makes the preceding regex optional
\- --> Matches the - character
? --> Makes the preceding regex optional
(\d{4}) --> Matches 4 digits
'''

while line != "exit":
    # TODO Find matches
    matches = re.search(regex, line)

    # TODO If no match found, print that no number was found
    if not matches:
        print('❗ This is not a valid phone number.')

    # TODO Else, break number up into area code, prefix, and suffic
    else:
        print('Country code: %s \nArea code: %s \nPrefix: %s \nSuffix: %s' %
              (matches[1], matches[2], matches[3], matches[4]))

    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!

    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")
