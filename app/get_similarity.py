def get_next_words(text, pattern):
    import re
    return re.findall("%s\s+([a-zA-Z0-9_-]+)"%(pattern), text)




import difflib
from domain_specific_words import glossary,wells,terms,word,alphabets,numbers

def find_most_similar_word(text, word_list):

    # Extract the word after "well" in the sample sentence
    # words_after_well = sample_sentence.split("well")[1].split()[0]
    words_after_well = get_next_words(text,'well')
    print(words_after_well)

    # Find the most similar word from the list
    most_similar_word = difflib.get_close_matches(words_after_well, word_list, n=1, cutoff=0.7)

    return most_similar_word[0] if most_similar_word else None



# List of words
word_list = wells
processed_text = "who is the age of the well Ar1Devs in the well Ar-Dev1"
# Find the most similar word
result = find_most_similar_word(processed_text, word_list)

# Print the result
print("Most similar word:", result)

