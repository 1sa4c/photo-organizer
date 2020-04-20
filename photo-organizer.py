from PIL import Image
from datetime import datetime
import os
import shutil


class PhotoOrganizer:
    extensions = ['jpg', 'jpeg', 'gif', 'png', 'mp4', 'mov', 'wmv', 'mpeg', 'mkv', 'avi' 'JPG', 'JPEG', 'GIF', 'PNG', 'MP4', 'MOV', 'WMV', 'MPEG', 'MKV', 'AVI']

    def photo_date(self, arq):
        try:
            img = Image.open(arq)
            info = img._getexif()
            if 36867 in info:
                date = info[36867]
                date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
            else:
                date = datetime.fromtimestamp(os.path.getmtime(arq))
        except:
            img = open(arq)
            date = datetime.fromtimestamp(os.path.getmtime(arq))
            img.close()
        return date


    def folder_name_aammdd(self, arq):
        date = self.photo_date(arq)
        return date.strftime('%Y') + '/' + date.strftime('%m') + '/' + date.strftime('%d')


    def move_photo(self, arq):
        n_folder = self.folder_name_aammdd(arq)
        if not os.path.exists(n_folder):
            os.makedirs(n_folder)
        shutil.move(arq, n_folder + '/' + arq)


    def organize(self):
        for arq in os.listdir('.'):
            if any(arq.endswith(ext) for ext in self.extensions):
                self.move_photo(arq)


POrg = PhotoOrganizer()
POrg.organize()