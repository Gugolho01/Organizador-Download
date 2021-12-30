import os, shutil, pathlib, fnmatch

# Movendo pasta

def move_dir(src: str, dst: str, pattern: str = '*.'):
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
    newpath = r'..\..\Downloads\Imagens' 

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    destination = r'..\..\Downloads\Imagens'
    source = r'..\..\Downloads'

    oenu(source, destination, all)


# Adobe

def orgAdo(*all):
    # crinando pasta
    newpath = r'..\..\Adobe' 

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    # Destino
    destination = r'..\..\Downloads\Adobe'
    source = r'..\..\Downloads'

    # organizando
    oenu(source, destination, all)

# Arquivo

def orgArq(*all):
    
    # crinando pasta
    newpath = r'..\..\Downloads\Arquivos' 

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    destination = r'..\..\Downloads\Arquivos'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# Áudio 

def orgAud(*all):
    # crinando pasta
    newpath = r'..\..\Áudio' 

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    destination = r'..\..\Downloads\Áudio'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# Vídeo

def orgVid(*all):
    # crinando pasta
    newpath = r'..\..\Downloads\Vídeos' 

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    destination = r'..\..\Downloads\Vídeos'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# WinRaR

def orgRaR(*all):
    # crinando pasta
    newpath = r'..\..\Downloads\Arquivos WinRaR' 

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    destination = r'..\..\Downloads\Arquivos WinRaR'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# Torrent

def orgTor(*all):
    # crinando pasta
    newpath = r'..\..\Downloads\Torrent' 

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    destination = r'..\..\Downloads\Torrent'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# Aplicativos

def orgApp(*all):
    # crinando pasta
    newpath = r'..\..\Downloads\Aplicativos' 

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    destination = r'..\..\Downloads\Aplicativos'
    source = r'..\..\Downloads'

    oenu(source, destination, all)

# Code

def orgCod(*all):
    # crinando pasta
    newpath = r'..\..\Downloads\Code' 

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    destination = r'..\..\Downloads\Code'
    source = r'..\..\Downloads'

    oenu(source, destination, all)
