import argparse
import os, fnmatch
import shutil
import ntpath

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getFiles(directory, images, limit):
    listOfFiles = os.listdir(directory)  
    pattern = "*.JPG"
    excludedDirectories = ".*"

    for entry in listOfFiles:
        path_entry = directory + '/' + entry
        # TODO METTRE UNE LIMITE SUR LE NOMBRE POSSIBLE DE SELECTION
        if (len(images) > limit):
            return 
        if (os.path.isdir(path_entry)):
            if (fnmatch.fnmatch(excludedDirectories, pattern) == False):
                getFiles(path_entry,images,limit)
        else:
            # TODO METTRE PLUSIEURS PATTERNS
            if fnmatch.fnmatch(entry, pattern):
                # TODO METTRE DU RANDOM DANS LA SELECTION DES IMAGES
                print (bcolors.WARNING + "1 images" + bcolors.ENDC)
                images.append(path_entry)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir')
    parser.add_argument('-o', '--output')
    parser.add_argument('-v', dest='verbose', action='store_true')
    args = parser.parse_args()


    images = []
    limit = 30

    getFiles(args.dir, images, limit)

    print (bcolors.WARNING + "Coping " + str(len(images)) + 'files' + bcolors.ENDC)
    # TODO GENERATION DES FICHIERS DANS UN REPERTOIRE
    for image in images:
        shutil.copyfile(image, args.output + '/' + ntpath.basename(image))
