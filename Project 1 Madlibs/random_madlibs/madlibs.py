# String Concatenation -> putting different strings together
# To start off with we want to make a variable that allows a person to subscribe to your youtube channel

# youtuber = 'Joseph Adusei'  # this is the random string to start off with

# There are a number of different ways to do this
#print('Subscribe to ' + youtuber)
# print('Subscribe to {}'.format(youtuber))  # This is done using f-strings
# print(f'Subscribe to {youtuber}')  # This is done using f-strings
def madlibs():
    adj = input('Adjective =')
    verb1 = input('Verb =')
    verb2 = input('Verb =')
    famous_person = input('Celebrity =')

    madlibs = f'Computer programming is so {adj}. I makes my so happy because I love to {verb1}. \
Keep motivated, stay hydrated and {verb2} because you look like {famous_person}'

    print(madlibs)
