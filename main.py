import googletrans as gtrans
import os
import json

LANGUAGES = gtrans.LANGUAGES


def save_data():
    if not os.path.exists("lang_data.json"):
        with open("lang_data.json", "w") as json_file:
            json.dump(LANGUAGES, json_file)


def search_lang(lang):
    with open("lang_data.json", "r") as json_file:
        lang_data = json.load(json_file)
    if lang in lang_data.values():
        return False
    else:
        print("There is not such language. Try typing again")
        return True


def get_language(get_lang):
    if get_lang == False:
        print("works")
        return


def main():
    save_data()
    lang = input("What language would you like to use? ")
    while search_lang(lang) == True:
        lang = input("What language would you like to use? ")
    get_lang = search_lang(lang)
    print(lang)
    search_lang(lang)
    get_language(get_lang)


if __name__ == "__main__":
    main()
