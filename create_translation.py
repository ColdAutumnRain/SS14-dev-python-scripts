#!/usr/bin/env python3
import re
import os
import ntpath  # For Windows users
import sys


def get_file_paths(directory) -> str:
    """
    :param directory:
    :return: file_path

    This will move throught all directiories strting from one specified in "directory" parameter. Next it will search for files
    with ".yml" extension and create a string containing path to that file.
    """

    for path, subdirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".yml"):
                file_path = os.path.join(path, file)

                yield file_path  # instead od yeals, return


def create_translation_file(soure_file_path, dest_file_path):
    """
    :param file_path:
    :return:

    This will open yml file, then it will search yml file for all occurences of "name" and "description" lines.
    Next is going to modify this lines and put them to newly created file.
    """
    new_file_name = ntpath.basename(soure_file_path)

    # New transalation path with file name
    tmp = os.path.join(dest_file_path, new_file_name)

    with open(soure_file_path, 'r') as fd:

        new_file = open(tmp, "w")

        # lines = []

        lines = fd.readlines()

        for line in lines:
            # New line for "name"
            if re.search(r" name:", line):
                text = ""

                line_id = line.lstrip()

                new_string_id = line_id.replace('name:', '- msgid:')

                text = f"{new_string_id} " \
                       f" msgstr: \n\n"

                new_file.write(text)

            if re.search(r"description:", line) is not None:
                text = ""

                line_desc = line.lstrip()

                new_string_desc = line_desc.replace('description:', '- msgid:')

                text = f"{new_string_desc} " \
                       f" msgstr: \n\n" \
                       f" ## \n\n"

                new_file.write(text)

        new_file.close()


def main():
    # Checking number of arguments
    if len(sys.argv) < 3:
        print("Error. Specify project directory and translation")
        sys.exit(1)

    # Taking project directory
    project_dir = sys.argv[1]

    files_location = os.path.join(project_dir, "Resources/Prototypes/Entities")

    translation_dir = os.path.join(project_dir, "Resources/Locale")

    # Get into folder "Locale"
    os.chdir(translation_dir)

    # Name of a translation ex. fr-FR
    translation_name = sys.argv[2]

    # Create new directory
    os.makedirs(translation_name)

    # Move to new directory
    new_tralsation_dir = os.path.join(translation_dir, translation_name)

    os.chdir(new_tralsation_dir)

    # computed_dir = os.path.join(project_dir, "Resources/Prototypes")

    # Create translation files
    for path in get_file_paths(files_location):
        create_translation_file(path, new_tralsation_dir)

    print("OK")
    # print(f"There is {counter} file")


if __name__ == "__main__":
    main()
