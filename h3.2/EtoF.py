EtoF = {'bread': 'du pain', 'wine': 'du vin',\
       'eats': 'mange', 'drinks': 'bois',\
       'likes': 'aime', 1: 'un',\
       '6.00':'6.00'}
# print(EtoF)
# print(list(EtoF.keys()))
# print(EtoF.keys)
# del EtoF[1]
# print(EtoF)

# D = {1: 'one', 'deux': 'two', 'pi': 3.14159}
# D1 = D
# print(D1)
# D[1] = 'uno'
# print(D1)
# for k in list(D1.keys()):
#    print(k, '=', D1[k])

def translateWord(word, dictionary):
   if word in dictionary:
       return dictionary[word]
   else:
       return word
    
def translate(sentence):
   translation = ''
   word = ''
   for c in sentence:
       if c != ' ':
           word = word + c
       else:
           translation = translation + ' '\
                         + translateWord(word, EtoF)
           word = ''
   return translation[1:] + ' ' + translateWord(word, EtoF)

def list_dict(dict):
   for key, value in dict.items():
       print("{} => {}".format(key, value))

print(translate('John eats bread'))
print(translate('Steve drinks wine'))
print(translate('John likes 6.00'))
print()
list_dict(EtoF)