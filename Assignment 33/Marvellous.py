import os
import hashlib

def CalculateChecksum(Path):

    fobj = open(Path, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):

        hobj.update(Buffer)

        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


def FindDuplicates(DirName):

    Data = {}

    for Folder, SubFolder, Files in os.walk(DirName):

        for Name in Files:

            Path = os.path.join(Folder, Name)

            Value = CalculateChecksum(Path)

            if Value in Data:
                Data[Value].append(Path)
            else:
                Data[Value] = [Path]

    return Data