import os, shutil, pathlib, fnmatch

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
    
    destination = r'..\..\Downloads\Imagens'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# Text

def orgTxt(*all):
    # crinando pasta

    destination = r'..\..\Downloads\Text'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# Adobe

def orgAdo(*all):
    # crinando pasta
    # Destino
    destination = r'..\..\Downloads\Adobe'
    source = r'..\..\Downloads'

    # organizando
    oenu(source, destination, all)

# Arquivo

def orgArq(*all):
    
    # crinando pasta
    destination = r'..\..\Downloads\Files'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# Áudio 

def orgAud(*all):
    # crinando pasta
    destination = r'..\..\Downloads\Áudio'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# Vídeo

def orgVid(*all):
    # crinando pasta
    destination = r'..\..\Downloads\Vídeos'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# WinRaR

def orgRaR(*all):
    # crinando pasta
    destination = r'..\..\Downloads\Files WinRaR'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# Torrent

def orgTor(*all):
    # crinando pasta
    destination = r'..\..\Downloads\Torrent'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# Aplicativos

def orgApp(*all):
    # crinando pasta
    destination = r'..\..\Downloads\Application'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# Code

def orgCod(*all):
    # crinando pasta
    destination = r'..\..\Downloads\Code'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# Pdf

def orgPdf(*all):
    # crinando pasta
    destination = r'..\..\Downloads\Pdf'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# Document

def orgDoc(*all):
    # crinando pasta
    destination = r'..\..\Downloads\Word'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# planilha

def orgSpr(*all):
    # crinando pasta
    destination = r'..\..\Downloads\Spreadsheet'
    source = r'..\..\Downloads'

    oenu(source, destination, all)
