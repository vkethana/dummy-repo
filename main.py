def add_two_numbers(a, b):
    ''' 
    Takes in two nums a and b and returns their sum 
    '''
    return a + b

def multiply_two_numbers(a, b):
    '''
    Takes in two nums a and b and returns their product 
    '''
    return a * b

def subtract_two_numbers(a, b):
    '''
    Takes in two nums a and b and returns their difference 
    '''
    return a - b

def decompose_sentence(sentence):
  '''
  Split a sentence into a list of words
  Input: sentence (str) - a sentence
  Output: words (list) - a list of words
  '''
  assert type(sentence) == str, "ERROR: sentence should be a string. What was passed in is: " + str(sentence) + 'of type ' + str(type(sentence))
  words = [i for i in sentence.split() if i.lower().islower()] # we check if every string, lowercased, contains at least one lowercase letter
  # this will remove words that are just punctuation or numbers
  return words
def clean_word(word):
  '''
  Take a given word and lower case it, remove all punctuation, and remove all accents
  Input: word (str) - a word
  Output: cleaned_word (str) - a cleaned word
  '''
  word = re.sub(r'[^\w\s]', '', word).lower() # strip all punctuation and lowercase the word
  return ''.join(c for c in unicodedata.normalize('NFD', word)
                  if unicodedata.category(c) != 'Mn')

if __name__ == '__main__':
    print(add_two_numbers(3, 4))
    print(multiply_two_numbers(3, 4))
    print(subtract_two_numbers(3, 4))
