import os
from datetime import datetime

class File:
    def __init__(self, file_path:str):
        self.file_path = file_path

    def find_datetime_create(self):
        datetime_create_UNIX = os.stat(self.file_path).st_ctime #return sec
        return datetime.fromtimestamp(int(datetime_create_UNIX))

    def find_datetime_change(self):
        datetime_create_UNIX = os.stat(self.file_path).st_mtime #return sec
        return datetime.fromtimestamp(int(datetime_create_UNIX))


class Directory:
    def __init__(self, path:str):
        self.path = path

    def find_files(self):
        files_names = os.listdir(self.path)
        return list(map(lambda file: {'file_name' : file, 'file_object': File(os.path.join(self.path, file)),} , files_names))