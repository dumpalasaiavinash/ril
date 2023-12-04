def get_next_words(text, pattern):
    import re
    return re.findall("%s\s+([a-zA-Z0-9_-]+)"%(pattern), text)




def find_most_similar_word(text):
    import difflib
    from domain_specific_words import wells
    wells = map(lambda x:x.lower(), wells)

    # Extract the word after "well" in the sample sentence
    # words_after_well = sample_sentence.split("well")[1].split()[0]
    words_after_well = get_next_words(text,'well')
    # print(words_after_well)

    # Find the most similar word from the list
    for i in words_after_well:
        # print(i)
        if i not in wells:
            most_similar_word = difflib.get_close_matches(i, wells, n=1, cutoff=0.7)
            # print(most_similar_word)
            if most_similar_word:
                text = text.replace(i,most_similar_word[0])
            else:
                text = text

    
    return(text)




# processed_text = "who is the age of the well KGD6Os in the well KGD6D26MA"
# # Find the most similar word
# result = find_most_similar_word(processed_text)

# # Print the result
# print("Most similar word:", result)

