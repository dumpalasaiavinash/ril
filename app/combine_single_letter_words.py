def combine_single_letter_words(raw_speech):
    from configparser import ConfigParser 
    configuration = ConfigParser() 
    configuration.read('config.ini')
    well_types = configuration.get('well_types','wells')
    well_types = (well_types.split(','))
    
    words = raw_speech.split()
    # well_types = ['well','wellbore','wellname']
    index_well = words.index('well')
    well_indexes_list = []
    character_end_indexes_list = []
    # getting the indexes of words in the well types list 
    for well_type in well_types:
        for i in range(len(words)):
            if words[i] == well_type:
                
                well_indexes_list.append(i)


    for well_index in well_indexes_list:
        for i in range(well_index+1,len(words)):
            # print(well_index)
            if len(words[i]) > 1:
                character_end_indexes_list.append(i)
                break


    # sorting lists
    well_indexes_list.sort()
    character_end_indexes_list.sort()
    # print(well_indexes_list)
    # print(character_end_indexes_list)
    if len(character_end_indexes_list) == 0:
        character_end_indexes_list.append(len(words))

    # print(well_indexes_list)
    # print(character_end_indexes_list)
    if len(character_end_indexes_list) < len(well_indexes_list):
        # well_indexes_list.pop()
        character_end_indexes_list.append(len(words))
    
    merge_list = list(zip(well_indexes_list, character_end_indexes_list))
    result = []
    index = 0
    # print(merge_list)
    for start, end in merge_list:
        result += words[index:start+1]
        # print(result)
        result.append("".join(words[start+1:end]))
        index = end
    result.append(" ".join(words[end:]))
    return(' '.join(result))
# print(combine_single_letter_words("who is the age of the well kgd6 in the well k g d 675"))