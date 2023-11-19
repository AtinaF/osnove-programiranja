input_file = open("neformatiraniTekst.txt", 'r')
output_file = open("formatiranTekst.txt", 'w')

counter = 0
for line in input_file.readlines():
    if len(line) > 1:
        formated_line = " ".join(line.split())
        if counter == 0:
            formated_title = formated_line.lower().title()
            centered_title = formated_title.center(100)
            output_file.write(centered_title)
            output_file.write("\n\n")
            counter += 1
            continue
        formated_paragraph = "     {}".format(formated_line)
        sentences = formated_paragraph.split('. ')
        index = 0
        for sentence in sentences:
            # print(sentence)
            sentence =  "{}{}".format(sentence[0].upper(), sentence[1:])
            sentences[index] = sentence
            index += 1
            # print(sentence)
        formated_paragraph = ". ".join(sentences)
        output_file.write(formated_paragraph)
        output_file.write("\n")
        counter += 1
    else:
        break
input_file.close()
output_file.close()