import os
import shutil

imgPath = "C:/Users/bacht/Desktop"
projectPath = "D:/02.code/05.flutter/sixmar"
name = ""


def GetAndroidSize():
    yield "48x48"
    yield "72x72"
    yield "96x96"
    yield "144x144"
    yield "192x192"


def GetInfo():
    global imgPath, projectPath, name
    imgPath = imgPath if imgPath else input('Enter Image Parent Folder Path: ')
    projectPath = projectPath if projectPath else input('Enter Project Folder Path: ')
    name = name if name else input('Enter Name File: ')
    return imgPath, projectPath, name


def MoveToImageFolder():
    imgPath, projectPath, name = GetInfo()
    for idx, oldName in enumerate(GetAndroidSize()):
        src = os.path.join(imgPath, "Android Icons", "{}.png".format(oldName))
        destFolder = os.path.join(projectPath, "assets/images", "{}x".format(idx+1)) if idx != 0 else os.path.join(projectPath, "assets/images")
        dest = os.path.join(destFolder, "{}.png".format(name))
        
        if not os.path.exists(destFolder):
            os.makedirs(destFolder)
        if os.path.isfile(src):
            shutil.move(src, dest)


if __name__ == "__main__":
    try:
        MoveToImageFolder()
    except Exception as err:
        print(err)
