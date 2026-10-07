#1
'''A security script requires text clean-up before processing
credentials. Write a function named
validate_access_code(raw_code) that accepts a single string
argument. Inside the function:
• Remove all accidental spaces from the beginning and end of the
string using a string method.
• Convert the entire code into absolute lowercase characters.
• Check the cleaned text string against two rules:
o It must strictly start with the prefix "admin".
o It must strictly end with the suffix "2026".
• If both rules are met, return True. Otherwise, return False.
• Prompt the user to enter a raw code string using input().
• Call validate_access_code(raw_code).
• Print a success message if it returns True, or an access denied
message if it returns False'''
def validate_access_code(raw_code):
    cleaned_code = raw_code.strip().lower()
    if cleaned_code.startswith("admin") and cleaned_code.endswith("2026"):
        return True
    else:
        return False
raw_code = input("Enter the raw code string: ")
if validate_access_code(raw_code):
    print("Access granted. Welcome!")
else:
    print("Access denied. Invalid code.")
#2
'''Write a function named audit_text_stream(flagged_word) that
accepts a single string parameter. Inside the function:
a. Initialize an occurrence_total counter variable at 0.
b. Implement a while True loop that repeatedly prompts the
user to enter a sentence via input().
c. If the user enters the word "exit" (in any casing
configuration, like "EXIT" or "Exit"), the loop must break
immediately.
d. For every other sentence entered, clean the input by making it
entirely lowercase, and use the string .count() method to see
how many times the flagged_word appears in it.Accumulate these counts into your occurrence_total.
• The function must return the total number of flagged words
counted across the entire session'''
def audit_text_stream(flagged_word):
    occurrence_total = 0
    while True:
        sentence = input("Enter a sentence (or type 'exit' to quit): ")
        if sentence == "exit" or sentence == "Exit" or sentence == "EXIT":
            break
        cleaned_sentence = sentence.lower()
        occurrence_total += cleaned_sentence.count(flagged_word)
    return occurrence_total
'''Write a validation function named
verify_file_record(line_content) that accepts a single string
representing one raw row of text from a file.'''\
#3
