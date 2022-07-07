from translate import Translator

def translate_language_ru():
    lang_ru = Translator(to_lang='ru')
    user_input = input()
    rus_translate = lang_ru.translate(user_input)
    return rus_translate

print(translate_language_ru())