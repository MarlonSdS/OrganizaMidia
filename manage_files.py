from os import listdir, replace
from shutil import make_archive

from common_data import CommonData as cd

#lista os arquivos de downloads
def list_files():
    files = listdir(f'/home/{cd.user}/Downloads/')
    return files

#SEPARAÇÃO DE ARQUIVOS POR TIPO
def separate_images(files):
    images = []
    for arq in files:
        for mime in cd.img_types:
            if mime in arq:
                images.append(arq)
    return images

def separate_documents(files):
    docs = []
    for arq in files:
        for mime in cd.doc_types:
            if mime in arq:
                docs.append(arq)
    return docs

def separate_videos(files):
    videos = []
    for arq in files:
        for mime in cd.vid_types:
            if mime in arq:
                videos.append(arq)
    return videos

def move_files(images, docs, videos):
    for img in images:
        print("Movendo "+ img + " para a pasta Imagens...")
        try:
            replace(f"/home/{cd.user}/Downloads/{img}", f"/home/{cd.user}/Imagens/{img}")
        except OSError:
            print("Infelizmente não foi possível")
        except FileNotFoundError:
            print("Infelizmente não foi possível")
        else:
            print("Feito!")

    for doc in docs:
        print("Movendo "+ doc + " para a pasta Documentos...")
        try:
            replace(f"/home/{cd.user}/Downloads/{doc}", f"/home/{cd.user}/Documentos/{doc}")
        except OSError:
            print("Infelizmente não foi possível")
        except FileNotFoundError:
            print("Infelizmente não foi possível")
        else:
            print("Feito!")
    for vid in videos:
        print("Movendo "+ vid +" para a pasta Vídeos...")
        try:
            replace(f"/home/{cd.user}/Downloads/{vid}", f"/home/{cd.user}/Vídeos/{vid}")
        except OSError:
            print("Infelizmente não foi possível")
        except FileNotFoundError:
            print("Infelizmente não foi possível")
        else:
            print("Feito!")

#faz os backups
def compress_files(filenames, sources):
    #contagem para o laço for
    itens = [0, 1, 2]

    for item in itens:
        make_archive(filenames[item], 'zip', sources[item])
        replace(f"{cd.dir_path}/{filenames[item]}.zip", f"/home/{cd.user}/Backups/{filenames[item]}.zip")
        