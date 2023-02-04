# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name: Jennifer kim

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    #returns input text with each word in list
    return input_text.split()


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    dictionary = {}
    # loops through each letter or each word in list
    for i in input_iterable:
        # checks if letter or word is in dictionary yet
        if i in dictionary.keys():
            # adds to frequency
            dictionary[i] = dictionary.get(i) + 1
        else:
            # adds letter/word to dictionary
            dictionary[i] = 1
    return dictionary


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    # uses the above function for frequency of letter in string
    return get_frequencies(word)


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    unique = []
    # finds unique letters or words in first dict
    # goes through all lettters/words in first dictionary
    for i in freq_dict1:
        if i not in unique:
            unique.append(i)
    # finds unique letters or words in second dict
    # goes through all letters/words in second dictionary
    for j in freq_dict2:
        if j not in unique:
            unique.append(j)
    freq_diff = 0
    freq_totals = 0
    # goes through whole unique list
    for num in range(len(unique)):
        # frequency to 0 if not in first dictionary
        if freq_dict1.get(unique[num]) == None:
            first_freq=0
        # gets frequency of letter/word
        else:
            first_freq=freq_dict1.get(unique[num])
        # frequency to 0 if not in second dictionary
        if freq_dict2.get(unique[num]) == None:
            sec_freq=0
        # gets frequency of letter/word
        else:
            sec_freq=freq_dict2.get(unique[num])
        # adds first minus second frequencies (absolute value) to total differences
        freq_diff += abs(first_freq-sec_freq)
        # adds first plus second frequencies to total differences
        freq_totals += first_freq+sec_freq
    # gets similarity score and rounds to 2 decimals
    return round(1 - (freq_diff/freq_totals),2)

### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    max_words=[]
    # gets most frequent value of 1st dicitonary
    max1 = max(freq_dict1.values())
    # gets most frequent value of 2nd dictionary
    max2 = max(freq_dict2.values())
    # set max comparing the max of 1st and 2nd dictionary
    if max1 > max2:
        max_freq = max1
    else:
        max_freq = max2
    # loops through 1st dictionary
    for i in freq_dict1.keys():
        # adds word to max_words list if it has the max frequency
        if freq_dict1.get(i) == max_freq:
            max_words.append(i)
    # loops through 2nd dictionary
    for i in freq_dict2.keys():
        # adds word to max_words list if it has the max frequency
        if freq_dict2.get(i) == max_freq:
            max_words.append(i)
    # sorts list alphabetically
    max_words.sort()
    return max_words

### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    # get words in file
    file = load_file(file_path)
    # make words into list
    file_words = text_to_list(file)
    num_words = len(file_words)
    # get freqencies of each word
    frequencies = get_frequencies(file_words)
    tfs = {}
    # loops through all words
    for i in frequencies.keys():
        # adds tf to tfs list
        tfs[i] = frequencies.get(i)/num_words
    # return tfs
    return tfs

def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    file = ""
    words_in_files = []
    file_words = []
    # loops through all files
    for i in file_paths:
        # get words in file
        file = load_file(i)
        words_in_current_file = text_to_list(file)
        # add list of words to another list called words_in_files
        words_in_files.append(words_in_current_file)
        # go through words in current file
        for j in words_in_current_file:
            # if word isn't in the overall list of words, add
            if j not in file_words:
                file_words.append(j)
    total_num_docs = len(file_paths)
    idfs = {}
    #iterates each unique word in files and maps it to idf
    for i in file_words:
        num_docs = 0
        #iterates each list of words in each file
        for j in words_in_files:
            # if curent word is present in file, add 1
            if i in j:
                num_docs += 1
        # calculates idf by # of files with word over # of files
        idf = math.log10(total_num_docs/num_docs)
        # adds idf to list of idfs
        idfs[i] = idf
    return idfs

def get_tfidf(tf_file_path, idf_file_paths):
    """
        Args:
            tf_file_path: name of file in the form of a string (used to calculate TF)
            idf_file_paths: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
        """
    # get the tfs
    tf_values = get_tf(tf_file_path)
    # gets the idfs
    idf_values = get_idf(idf_file_paths)
    tfidf = {}
    # goes through all the words in tf_file_path
    for i in tf_values.keys():
        # adds tfidf to dictionary mapping word to tfidf
        tfidf.update({i:tf_values.get(i) * idf_values.get(i)})
    # sort tfidf by alphabetical order first
    sorted_alpha = sorted(tfidf.items(), key = lambda kv: kv[0])
    # sort tfidf by value next
    # words with same tfidf already in alphabetical order
    sorted_age = sorted(sorted_alpha, key = lambda kv: kv[1])
    return sorted_age


if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    ## Tests Problem 0: Prep Data
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    # print(world)      # should print ['hello', 'world', 'hello']
    # print(friend)     # should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    # print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    # print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    ## Tests Problem 2: Get Letter Frequencies
    freq1 = get_letter_frequencies('hello')
    freq2 = get_letter_frequencies('that')
    # print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    word1_freq = get_letter_frequencies('toes')
    word2_freq = get_letter_frequencies('that')
    word3_freq = get_frequencies('nah')
    word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    # print(word_similarity1)       # should print 1.0
    # print(word_similarity2)       # should print 0.25
    # print(word_similarity3)       # should print 0.0
    # rint(word_similarity4)       # should print 0.4

    ## Tests Problem 4: Most Frequent Word(s)
    freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    # print(most_frequent)      # should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    tf_text_file = 'tests/student_tests/hello_world.txt'
    idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    tf = get_tf(tf_text_file)
    idf = get_idf(idf_text_files)
    tf_idf = get_tfidf(tf_text_file, idf_text_files)
    # print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]
