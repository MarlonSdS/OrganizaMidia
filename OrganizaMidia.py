from shutil import make_archive
from datetime import datetime

import manage_files as mf
from common_data import CommonData as cd

#checa se já é hora de fazer o backup
def check_time():
    time = datetime.today().strftime("%H")
    return int(time)

#listas com os arquivos separados por tipo
images = mf.separate_images(mf.list_files())
docs = mf.separate_documents(mf.list_files())
videos = mf.separate_videos(mf.list_files())

mf.move_files(images, docs, videos)

time = check_time()

#o backup só será feito a noite
if time > 17:
    mf.compress_files(cd.filenames, cd.sources)
else:
    print("Ainda não é hora do backup, encerrando execução")