while True:
    raw_input = input("")
    type = input("what is this > ")
    print(raw_input)

    seperated_input = raw_input.split(" ")
    print(seperated_input)

    match = []
    match_number = []

    current_word = 0
    current_entity = 0

    while current_entity < len(seperated_input):
        dictionary = open("dictionary.txt", "r").read().split("\n")
        current_word = 0
        current_word_match = 0
        temp_match = "NA"
        while current_word < len(dictionary):
            if dictionary[current_word] == seperated_input[current_entity]:
                temp_match = current_word
            current_word = current_word + 1
        if temp_match == "NA":
            open("dictionary.txt", "a+").write(str(seperated_input[current_entity]) + "\n")
            temp_match = len(dictionary)
        match.append(temp_match)
        current_entity = current_entity + 1
    print(match)
    labels = []

    # open("model.txt", "a+").write(str(match) + ":" +  type + "\n")

    model = open("model.txt", "r").read().split("\n")
    for label in model :
        label_value = label.split(":")[0]
        value = 0
        for entity in match :
            if str(entity) in str(label_value) :
                value = value + 1
        labels.append(value)

    print(model[labels.index(max(labels))])
            
            



