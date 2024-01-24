import argparse
import os
import shutil
import sys

#DBVUnrealSmartCleaner  was born because of the necessity of Unreal Developers who have many Unreal Engine projects in their computer that they don't want to remove from it but that have problems with the disc space. This tool will remove the generated directories that can be generated at any time but that take many gigabytes of the hard disc.

 #   Copyright (C) 2023  David Bueno Vallejo
#
 #   This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    The GNU General Public License can be found in <https://www.gnu.org/licenses/>.
# 

# Definir las cadenas de texto en inglés y español
STRINGS = {
    "es": {
        "confirm": "¿Estás seguro de que quieres {accion}? [y/n]: ",
        "ready_to_delete": "Preparado para eliminar: ",
        "deleted": "Eliminado: ",
        "skipped": "Se ha omitido: ",
        "remove_folder": "eliminar esta carpeta ",
        "usage_example": "\nEjemplo de uso: python DBVUnrealSmartCleaner.py -path c:/unrealproyect/ -protect project1 project3 -remove intermediate saved",
        "description": 'Reduce el tamaño de las carpetas de los proyectos de Unreal Engine.',
        "path_help": 'La carpeta de trabajo',
        "protect_help": 'Lista de carpetas a proteger',
        "remove_help": 'Lista de carpetas a eliminar',
        "verbose_help": 'Por defecto se confirma antes de eliminar cada carpeta, si se activa esta opcion no se realizan confirmaciones',
        "lang_help": 'Idioma del script (en o es)',
        "alert_noverbose": 'Atencion, has elegido el modo no interactivo. Todas las carpetas se eliminaran sin confirmacion. Si no esta seguro elimine el atributo -noverbose',
        "verbose_mode": 'Modo interactivo...',
        "continue": 'continuar',
        "params": 'Los parametros recibidos son los siguientes:'
    },
    "en": {
        "confirm": "Are you sure you want to {accion}? [y/n]: ",
        "ready_to_delete": "Ready to delete: ",
        "deleted": "Deleted: ",
        "skipped": "Skipped: ",
        "remove_folder": "remove this folder ",
        "usage_example": "\nUsage example: python DBVUnrealSmartCleaner.py -path c:/unrealproject/ -protect project1 project3 -remove intermediate saved",
        "description": 'Reduce the size of the folders of Unreal Engine projects.',
        "path_help": 'The working folder',
        "protect_help": 'List of folders to protect',
        "remove_help": 'List of folders to remove',
        "verbose_help": 'Confirm before deleting each folder',
        "lang_help": 'Script language (en or es)',
        "alert_noverbose": 'Warning you have choosen noverbose. All the files will be deleted without confirmation. If you are not sure remove the -noverbose attribute',
        "verbose_mode": 'Verbose mode...',
        "continue": 'continue',
        "params": 'The params received are:'
    }
}

def confirm(accion, lang):
    respuesta = input(STRINGS[lang]["confirm"].format(accion=accion))
    return respuesta.lower() == 'y' or respuesta.lower() == 's'

def remove_folders(path, protect, remove, verbose, lang):
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if name in remove and not any(p in root for p in protect):
                full_path = os.path.join(root, name)
                if verbose:
                    print(STRINGS[lang]["ready_to_delete"] + full_path)
                    if confirm(STRINGS[lang]["remove_folder"], lang):
                        shutil.rmtree(full_path)
                        print(STRINGS[lang]["deleted"] + full_path)
                    else:
                        print(STRINGS[lang]["skipped"] + full_path)
                else:
                    print ("silent mode...")
                    shutil.rmtree(full_path)
                    print(STRINGS[lang]["deleted"] + full_path)
                    

def main():
    verbose=True
    print("DBVUnrealSmartCleaner")
    print("by David Bueno Vallejo 2024")
    parser = argparse.ArgumentParser(description="DBVUnrealSmartCleaner")
    parser.add_argument('-lang', type=str, default='en', help="language/idioma")
    parser.add_argument('-path', type=str, help=STRINGS["en"]["path_help"])
    parser.add_argument('-protect', nargs='+', help=STRINGS["en"]["protect_help"])
    parser.add_argument('-remove', nargs='+', help=STRINGS["en"]["remove_help"])
    parser.add_argument('-noverbose', action='store_false', help=STRINGS["en"]["verbose_help"])
    
   
    args = parser.parse_args()
    print(STRINGS[args.lang]["params"])
    for arg in vars(args):
        print(f'{arg}: {getattr(args, arg)}')

    if len(sys.argv)==1 or args.path is None or args.remove is None:
        parser.print_help(sys.stderr)
        print(STRINGS[args.lang]["usage_example"])
        sys.exit(1)
    if args.noverbose:
        print(STRINGS[args.lang]["verbose_mode"])
    else: 
        print(STRINGS[args.lang]["alert_noverbose"])
        verbose=False
        if not confirm(STRINGS[args.lang]["continue"],args.lang):
            sys.exit(1)
    
    remove_folders(args.path, args.protect, args.remove, verbose, args.lang)

if __name__ == "__main__":
    main()
