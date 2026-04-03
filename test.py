from deep_translator import GoogleTranslator
import builtins
import keyword


words = [
    "hello",
    "world",
    "keyboard",
    "monitor",
    "mouse",
    "car",
    "microwave",
    "cookies"
]


lang = input("What language would you like to use? ")
print(lang)


translator = GoogleTranslator(source="en", target="pt")
for word in words:
    result = translator.translate(word)
    print("{} -> {}".format(word, result))


all_builtins = [b for b in dir(builtins)]
all_keywords = keyword.kwlist


combined = all_builtins + all_keywords
print(combined)