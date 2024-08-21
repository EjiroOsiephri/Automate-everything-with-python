from googletrans import Translator

def translate(text, target_language):
    return Translator().translate(text, dest=target_language).text

text = input('Enter text to translate: ')
target_language = input('Enter target language: ')

print(translate(text, target_language))