def pig_latin(sentence):
    words = sentence.split( )
    mylist= []
    for word in words:
        letter=word[0]
    
        if letter.lower() in 'aeiou':
            pig_word = word + 'ay'
            mylist.append(pig_word)
        else:
            pig_word = word[1:] + letter + 'ay'
            mylist.append(pig_word)
    return mylist
            
