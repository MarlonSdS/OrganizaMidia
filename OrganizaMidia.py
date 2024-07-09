from shutil import make_archive
from datetime import datetime
from os import getlogin

#data de hoje
today = datetime.today().strftime('%d-%m-%Y')

#usuário do sistema
user = getlogin()

#nomes dos arquivos de cada backup
filenames = ["ImagensBackup-"+today,
             "DocumentosBackup-"+today,
             "VideosBackup-"+today]

#cada pasta a ser backupada
sources = [f'/home/{user}/Imagens',
           f'/home/{user}/Documentos',
           f'/home/{user}/Vídeos']

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