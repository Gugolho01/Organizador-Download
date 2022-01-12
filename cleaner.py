import os, shutil, pathlib, fnmatch
from pathlib import Path

# find the path Download
def get_downloads_path():
    return '%s\Downloads' % (str(Path.home()))

# find the path startup
def get_startup_path():
    return '%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % (str(Path.home()))

def startupFind():
    if not os.path.exists('Organizador_Download - Atalho.lnk'):
        shutil.copyfile('Organizador_Download.exe', 'Organizador_Download - Atalho.lnk')
    os.rename('Organizador_Download - Atalho.lnk', get_startup_path() + '/Organizador_Download - Atalho.lnk')
    
FILE_PATH = get_downloads_path()
source = FILE_PATH

# Movendo pasta e cria a pasta
def move_dir(src: str, dst: str, pattern: str = '*'):
        pattern = '*.' + pattern
        if not os.path.isdir(dst):
            pathlib.Path(dst).mkdir(parents=True, exist_ok=True)
        for f in fnmatch.filter(os.listdir(src), pattern):
            shutil.move(os.path.join(src, f), os.path.join(dst, f))

#enumerar

def organize(*enumerate):
    tam = len(enumerate)
    for i in range(0, tam):
        return i

# o = enumerate funcinar

def oenu(source, destination, all):
    o = organize(all)
    while o < len(all):
        move_dir(source, destination, all[o])
        o = o + 1

# Img

def orgImg(*all):
    # crinando pasta
    destination = FILE_PATH + '\Imagens'

    oenu(source, destination, all)

# Text

def orgTxt(*all):
    # crinando pasta
    destination = FILE_PATH + '\Text'

    oenu(source, destination, all)

# Adobe

def orgAdo(*all):
    # crinando pasta
    destination = FILE_PATH + '\Adobe'

    # organizando
    oenu(source, destination, all)

# Arquivo

def orgArq(*all):
    
    # crinando pasta
    destination = FILE_PATH + '\Arquivos'

    oenu(source, destination, all)

# Áudio 

def orgAud(*all):
    # crinando pasta
    destination = FILE_PATH + '\Áudio'

    oenu(source, destination, all)

# Vídeo

def orgVid(*all):
    # crinando pasta
    destination = FILE_PATH + '\Vídeos'

    oenu(source, destination, all)

# WinRaR

def orgRaR(*all):
    # crinando pasta
    destination = FILE_PATH + '\Arquivos WinRaR'

    oenu(source, destination, all)

# Torrent

def orgTor(*all):
    # crinando pasta
    destination = FILE_PATH + '\Torrent'

    oenu(source, destination, all)

# Aplicativos

def orgApp(*all):
    # crinando pasta
    destination = FILE_PATH + '\Aplicativos'

    oenu(source, destination, all)

# Code

def orgCod(*all):
    # crinando pasta
    destination = FILE_PATH + '\Code'

    oenu(source, destination, all)

# Pdf

def orgPdf(*all):
    # crinando pasta
    destination = FILE_PATH + '\Pdf'

    oenu(source, destination, all)

# Document

def orgDoc(*all):
    # crinando pasta
    destination = FILE_PATH + '\Word'

    oenu(source, destination, all)

# planilha

def orgSpr(*all):
    # crinando pasta
    destination = FILE_PATH + '\Planilhas'

    oenu(source, destination, all)
