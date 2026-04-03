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
            json.dump(LANGUAGES, json_file)


def search_lang(lang):
    with open("lang_data.json", "r") as json_file:
        lang_data = json.load(json_file)
    if lang in lang_data.values() or lang_data.keys():
        return False
    else:
        print("There is not such language. Try typing again")
        return True


def get_language(get_lang):
    if get_lang == False:
        print("works")
        return


LANGUAGES = gtrans().get_supported_languages(as_dict=True)
WORDS_LIST = create_list()


def main():
    save_data()
    lang = input("What language would you like to use? ")
    while search_lang(lang) == True:
        lang = input("What language would you like to use? ")
    get_lang = search_lang(lang)
    print(lang)
    search_lang(lang)
    get_language(get_lang)
    print(WORDS_LIST)


if __name__ == "__main__":
    main()