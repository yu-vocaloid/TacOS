import os
import shutil
import urllib.request
def main(path,operation,version='lastest'):
    if operation == 'makeImage':
        def getfile(rootfiles='.'):
            filedict = {}
            for items in os.listdir(rootfiles):
                newpath = f'{rootfiles}/{items}'
                print(f'Extracting {newpath}...')
                try:
                    content = os.listdir(newpath)
                    filedict[items] = [getfile(newpath),'dir']
                except:
                    with open(newpath) as c:
                        content = c.read()
                    filedict[items] = [content,'file']
                print('Successful.')
            return filedict
        print('System files are being extracted...')
        data = getfile()
        def write_image(image,data,spacenum=0):
            spaces = '    ' * spacenum
            for items in data.items():
                if items[1][1] == 'file':
                    if items[0] != 'TacOSRun.py':
                        image.write(f'{spaces}FILE&{items[0]}:\n')
                        image.write(f'{spaces}{items[1][0]}\n')
                elif items[1][1] == 'dir':
                    image.write(f'{spaces}DIR&{items[0]}:\n')
                    write_image(image,items[1][0],spacenum + 1)
        if os.path.exists(f'./{path}.tac'):
            print('Path already exists.')
        else:
            print('Making Image...')
            image = open(f'./{path}.txt','w')
            image.write('MAIN:\n')
            image.write(data['TacOSRun.py'][0])
            image.write('\nFILES:\n')
            write_image(image,data)
            image.close()
    elif operation == 'getImage':
        if version == 'lastest':
            version = urllib.request.urlopen('https://raw.githubusercontent.com/yu-vocaloid/TacOS/main/TacOSImage/latestVer.txt').read().strip()
        image = urllib.request.urlopen(f'https://raw.githubusercontent.com/yu-vocaloid/TacOS/main/TacOSImage/{version}.tac').read()
        print(f'Getting image version {version.strip()}...')
        if os.path.exists(f'./{path}.tac'):
            print('Path already exists.')
        else:
            print('Making Image...')
            with open(f'./{path}.txt','w') as f:
                f.write(image)
    print('Successful.')
    print('Renameing...')
    shutil.move(f'./{path}.txt',f'./{path}.tac')
    print('Successful.')
    print()
    print('Done.')
