import json

# Load slang-to-standard dictionary
def load_slang_dict():
    with open("slang.json", "r") as f:
        return json.load(f)

slang_dict = load_slang_dict()

# Translate slang into standard Swahili
def translate_to_standard(slang_phrase):
    return slang_dict.get(slang_phrase, slang_phrase)  # Return the slang if no match

# Optionally, you can have a function that works the other way around (standard -> slang)
def translate_to_slang(standard_phrase):
    for slang, standard in slang_dict.items():
        if standard == standard_phrase:
            return slang
    return standard_phrase  # Return the standard phrase if no slang match found
