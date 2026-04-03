from deep_translator import GoogleTranslator as gtrans
import os
import json
import builtins
import keyword

def create_list():
    all_builtins = [b for b in dir(builtins)]
    all_keywords = keyword.kwlist
    combined = all_builtins + all_keywords
    return combined

def save_data():
    if not os.path.exists("lang_data.json"):
        with open("lang_data.json", "w") as json_file:
            json.dump(LANGUAGES, json_file, indent=2)

def search_lang(lang):
    with open("lang_data.json", "r") as json_file:
        lang_data = json.load(json_file)
    if lang in lang_data.values() or lang in lang_data.keys():
        return False
    else:
        print("There is not such language. Try typing again")
        return True

def translate(lang):
    with open("lang_data.json", "r") as json_file:
        lang_data = json.load(json_file)
    if lang in lang_data.keys():
        actual_lang = lang_data[lang]
    else:
        actual_lang = lang
    translator = gtrans(source="en", target=actual_lang)
    translated = []
    for word in WORDS_LIST:
        try:
            translated.append(translator.translate(word))
            print(translator.translate(word))
        except Exception:
            translated.append(word)
            print(translator.translate(word))
    with open("translated_data.json", "w", encoding="utf-8") as json_file:
        json.dump(translated, json_file, ensure_ascii=False, indent=2)
    return translated

LANGUAGES = gtrans().get_supported_languages(as_dict=True)
WORDS_LIST = create_list()

def main():
    save_data()
    lang = input("What language would you like to use? ")
    while search_lang(lang) == True:
        lang = input("What language would you like to use? ")
    translate(lang)

if __name__ == "__main__":
    main()