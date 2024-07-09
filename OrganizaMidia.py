from shutil import make_archive
from datetime import datetime
from os import getlogin, listdir

#data de hoje
today = datetime.today().strftime('%d-%m-%Y')

#usuário do sistema
user = getlogin()

#LISTAS
#nomes dos arquivos de cada backup
filenames = ["ImagensBackup-"+today,
             "DocumentosBackup-"+today,
             "VideosBackup-"+today]

#cada pasta a ser backupada
sources = [f'/home/{user}/Imagens',
           f'/home/{user}/Documentos',
           f'/home/{user}/Vídeos']

#lista de tipos de arquivos de imagens
img_types = ['.jpeg', '.jpg', '.png', '.svg', '.gif']
doc_types = ['.txt', '.odt', '.docx', 'pdf', '.epub', '.html', '.rtf']
vid_types = ['.mp4', '.mkv', '.mov', '.avi']

#lista os arquivos de downloads
def list_files():
    files = listdir(f'/home/{user}/Downloads/')
    return files

#SEPARAÇÃO DE ARQUIVOS POR TIPO
def separate_images(files):
    images = []
    for arq in files:
        for mime in img_types:
            if mime in arq:
                images.append(arq)
    return images

def separate_documents(files):
    docs = []
    for arq in files:
        for mime in doc_types:
            if mime in arq:
                docs.append(arq)
    return docs

def separate_videos(files):
    videos = []
    for arq in files:
        for mime in vid_types:
            if mime in arq:
                videos.append(arq)
    return videos

#checa se já é hora de fazer o backup
def check_time():
    time = datetime.today().strftime("%H")
    return int(time)

#cria os arquivos zip das pastas em sources
def compress_files(filenames, sources):
    #contagem para o laço for
    itens = [0, 1, 2]

    for item in itens:
        make_archive(filenames[item], 'zip', sources[item])

time = check_time()

#o backup só será feito a noite
if time > 17:
    compress_files(filenames, sources)
else:
    print("Ainda não é hora do backup, encerrando execução")