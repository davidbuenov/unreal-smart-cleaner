# unreal-smart-cleaner
DBV Unreal Smart Cleaner was born because of the necessity of Unreal Developers who have many Unreal Engine projects in their computer that they don't want to remove from it but that have problems with the disc space. This tool will remove the generated directories that can be generated at any time but that take many gigabytes of the hard disc.

# how to use it
The application is a python script, so you need to have installed python. It can be called from the console. With these options:
```python
  -h, --help            show this help message and exit
  -lang LANG            language/idioma
  -path PATH            The working folder
  -protect PROTECT [PROTECT ...]
                        List of folders to protect
  -remove REMOVE [REMOVE ...]
                        List of folders to remove
  -noverbose            Confirm before deleting each folder

Usage example: python DBVUnrealSmartCleaner.py -path c:/unrealproject/ -protect project1 project3 -remove intermediate saved
```
Basically in the 
-path attributes we will put the folder that is on top of the proyects in this folder we use to have all our Unreal Engine 5 projects. The will be some of them that we are using frequently and we don't want to generate all the information for them. This means that there will be some projects that we want to protect. In the example above, the projects 1 and 3 will not find there folders modified. For the rest, the intermediate and saved folder will be removed. This keeps the consistency of the project and reduces the space in this, the only thing to know is that in the future we will have to wait until the content is generated. with the -remove keyword we can add all the folders that we don't want to have in our hard disk.

-remove there are different folders that are generated automatically and that coud be included in this list. Some of them are: Saved, Intermediate, Binaries, DerivedDataCache

All the information about the folders in the [Unreal Engine 5 Documentation](https://docs.unrealengine.com/5.0/en-US/unreal-engine-directory-structure/)

We can select if we want the language in Spanish -lang es or in English by default -lang en
By default before removing any folder the user is asked for confirmation. We can avoid these questions if we select the param -noverbose.

## batch files
There are two example batch (.bat) files that can be modified to call easily to the main application

## test folders
In the code you will find some test folder to practise before using it with your real files.

# videos
Soon we will have some videos showing how to use it. But don't forget to suscribe to my [Youtube channel](https://www.youtube.com/@davidbuenov)  with many [Unreal Engine tutorials and demos](https://www.youtube.com/playlist?list=PLnNbmcjjevxvP97mRrjDHxHW1g6o9ZesL) 
