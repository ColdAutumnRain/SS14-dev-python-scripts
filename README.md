 
# SS14-dev-python-scripts
Some scripts for development of SS14

## Translation script

I created small python script for anyone that want to create transaltion for his natve language.

### How this works?
Script creates files that are needed for translation. All about, how files should looks like you can find here: https://hackmd.io/@ss14/localization#Localization

Here is example of one generated file:

```
- msgid: mini hoe
  msgstr: 

- msgid: It's used for removing weeds or scratching your back.
  msgstr: 

 ## 

- msgid: Plant-B-Gone
  msgstr: 

- msgid: Kills those pesky weeds!
  msgstr: 

 ## 

- msgid: weed spray
  msgstr: 

- msgid: It's a toxic mixture, in spray form, to kill small weeds.
  msgstr: 

```

Basicly script read all '.yml' files in space-station-14/Resources/Prototypes directory. Then it detect all occurences of parameter ```name``` and ```description``` and copy it to new file in space-station-14/Resources/Locale. Of coure it also create direcotry that will contain transaltion files.

Now all you need to do is to write a transation of names and description.


### How to use it?

You need is Python interpreter. Script works on bulidiin modules, so you dont have to install anything additional.

```
python create_pranslation.py 'path_to_a_project_folder' 'name_of_translation_folder'
```

Where:

 - *path to a project folder* - as name suggest it is path to your folder with SS14 project

 - *name of translation folder* - name where all your transation files will be stored, for example if you want to make French translation you should write something like this "fr-FR". More on Language localizotion names ypou can find here: https://en.wikipedia.org/wiki/Language_localisation#Language_tags_and_codes

Example of command:

```
python create_pranslation.py /home/HONK_LORD/Projects/space-station-14 fr-FR
```


Hope it helps! :)
