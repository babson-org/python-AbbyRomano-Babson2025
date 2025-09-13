 # TODO: Get user input
    text = input("Enter some text: ")

    # TODO: Count letters
    letters = 0
    for char in text: 
        if char.isalpha():
            count += 1
    print('Number of letters:', count)

    # TODO: Count words
    words = text.split()
    num_words = len(words)
    print(f"Words: {num_words}")

    # TODO: Count sentences
    sentence_count = 0
    for char in text:
         if char in ".?!":
            sentence_count += 1
    print(f"Sentences: {sentence_count}")
    
    # TODO: Print the results
    print(f"Letters: {letters}")
    print(f"Words: {num_words}")        
    print(f"Sentences: {sentence_count}")   