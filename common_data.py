from datetime import datetime
from os import getlogin, path

import manage_files as mf

class CommonData():
    #data de hoje
    today = datetime.today().strftime('%d-%m-%Y')

    #usuário do sistema
    user = getlogin()

    #caminho absoluto do arquivo
    dir_path = path.dirname(path.realpath(__file__))

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

