def getFile():
    file = input("File Name: ")
    file = file.lower()
    return file

def checkFileType(file):
    fileTypeIndex = file.find(".")
    if fileTypeIndex != -1:
        fileType = file[fileTypeIndex + 1: ] 
        return fileType
    else:
        return fileTypeIndex

def main():
    file = getFile()
    fileType = checkFileType(file)
    if fileType == "zip":
        print(f"file/{fileType}")
    elif fileType == "gif" or fileType == "png" or fileType == "jpg" or fileType == "jpeg":
        print(f"image/{fileType}")
    elif fileType == "pdf" or fileType == "txt":
        print(f"document/{fileType}")
    else:
        print("application/octet-stream")


main()