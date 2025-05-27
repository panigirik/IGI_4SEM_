def Task4():
    """
    Analyzes the given text.

    Operations:
    a) Counts words shorter than 5 characters.
    b) Finds the shortest word ending with 'd'.
    c) Displays all words sorted in descending order by length.
    """

    text = ("So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy "
            "and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and "
            "picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.")

    # Remove punctuation and split text into words
    words = text.replace(',', '').replace('.', '').split()

    # Convert all words to lowercase
    words = [word.lower() for word in words]

    # a) Count words with length < 5 characters
    short_word_count = sum(1 for word in words if len(word) < 5)
    print("Номер слова короче 5 символов:", short_word_count)

    # b) Find the shortest word ending with 'd'
    words_ending_with_d = [word for word in words if word.endswith('d')]
    shortest_word_with_d = min(words_ending_with_d, key=len, default=None)
    print("Кратчайшее слово на 'd':", shortest_word_with_d if shortest_word_with_d else "Not found")

    # c) Sort and display words by length in descending order
    sorted_words = sorted(words, key=len, reverse=True)
    print("Слова отсортированные под длине в порядке убывания:")
    print(", ".join(sorted_words))

if __name__ == "__main__":
    Task4()
