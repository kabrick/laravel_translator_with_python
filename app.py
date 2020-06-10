import os
import short_codes
import json
from googletrans import Translator

print("""
##############################################
# Welcome to Laravel Application Translation #
#          Created by Douglas Hozea          #
##############################################
""")

translator = Translator()

while True:
    directory_location = input("Please enter location of lang folder in your project e.g "
                               "/var/www/html/project/resources/lang: \n")

    if not os.path.isdir(directory_location + "/en"):
        print("Wrong directory entered")
        break

    translate_to = input("Please enter the language short code to translate to: \n")

    if not short_codes.is_short_code_valid(translate_to):
        print("Language short code specified does not exist")
        break

    file_to_translate = input("Please enter the name of the file you wish to translate e.g file.php: \n")

    if not os.path.isfile(directory_location + "/en/" + file_to_translate):
        print("File name not found")
        break

    dict_from_en_file = json.loads(os.popen("php -r \"echo json_encode(include '" +
                                            directory_location + "/en/" + file_to_translate +
                                            "');\"").read())

    number_of_translation_keys = len(dict_from_en_file)
    current_key_being_translated = 1

    if not os.path.isdir(directory_location + "/" + translate_to):
        os.mkdir(directory_location + "/" + translate_to)

    f = open(directory_location + "/" + translate_to + "/" + file_to_translate, "w+")
    f.write("<?php \n\n")
    f.write("return [\n")

    for key, value in dict_from_en_file.items():
        print(current_key_being_translated, "/", number_of_translation_keys)

        translated_value = translator.translate(value, dest=translate_to, src='en').text

        # check if translated value is still destination lang and use lower case
        if translator.detect(translated_value).lang == 'en':
            translated_value = translator.translate(value.lower(), dest=translate_to, src='en').text

        print(key, "=>", translated_value)
        print("")

        f.write("    \"" + key + "\" => \"" + translated_value + "\", \n")

        current_key_being_translated += 1

    f.write("];")
    f.close()

    break
