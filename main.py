import googletrans as gtrans
import os
import json

LANGUAGES = gtrans.LANGUAGES
with open("lang_data.json", "w") as json_file:
    json.dump(LANGUAGES, json_file)
