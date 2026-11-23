MAIN:
# = Init = #
 # = Import = #
import sys
import os
import urllib.request
 # ========== #
now_path = './'
sizedict = {'B':1024,'KB':1024**2,'MB':1024**3,'GB':1024**4,'TB':1024**5,'PB':1024**6,'EB':1024**7,'ZB':1024**8,'YB':1024**9}
try:
    with open('TacSystem/version/Ver.version') as ver:
        systemVerInfo = {}
        for i in ver.read().split(',',1):
            kv = []
            for t in i.split('=',1):
                kv.append(t)
            systemVerInfo[kv[0]] = kv[1]
    namespace = {}
    exec(open('TacSystem/functionInfo.py').read(),namespace)
    info = namespace.get('info')
except Exception as e:
    pass
    print('='*35)
    print('Running over !')
    print('Sorry !Your TacOS has some problem ,let\'s fix them !')
    print('='*35)
    sys.exit()
print('''ooooooooooooo                       .oooooo.    .oooooo..o 
8'   888   `8                      d8P'  `Y8b  d8P'    `Y8 
     888       .oooo.    .ooooo.  888      888 Y88bo.      
     888      `P  )88b  d88' `"Y8 888      888  `"Y8888o.  
     888       .oP"888  888       888      888      `"Y88b 
     888      d8(  888  888   .o8 `88b    d88' oo     .d8P 
    o888o     `Y888""8o `Y8bod8P'  `Y8bood8P'  8""88888P'  
                                                           
                                                           
                                                           ''')

print(f'{systemVerInfo["system"]} Version :{systemVerInfo["ver"]}, copyright ©Jaden 2026')
# = Def function = #
def off():
    print('Shutting down ...')
    global running
    running = False
def istmgr(operation,name,version):
    if operation == 'getpackage':
        data = urllib.request.urlopen(f'https://raw.githubusercontent.com/yu-vocaloid/TacOS/main/{name}/{name}{version}.py').read()
        if data == '404: Not Found':
            print('Package not found')
        else:
            if not os.path.exists(f'TacSystem/Package/{name}_install.py'):
                print(f'Getting package "{name}" in https://raw.githubusercontent.com/yu-vocaloid/TacOS/main/ ...')
                with open(f'TacSystem/Package/{name}{version}_install.py','w') as f:
                    f.write(data)
                print(f'Get successfully {len(data)}B')
            else:
                print('Packge already exists')
    if operation == 'installpackage':
        with open(f'TacSystem/Package/{name}{version}_install.py')  as f:
            data = f.read()
        lines = data.split('\n')
        if not lines[0] == '#TacOStpkg install 1.0':
            print('Package has been damaged')
        else:
            if lines[1][:20] != '#Signaturepublisher=':
                answer = input('This package has not been signed for security, are you sure you want to continue installing it? (y/n):')
                if answer == 'n':
                    return 0
            else:
                print(f'Publisher: {lines[1].split("=")[1]}')
            print('Running package...')
            exec(f'{data}\nINSTALLMAIN()')
def echo(content):
    print(content)
def listfile(path=None):
    if not path:
        path = now_path
    if os.path.exists(path):
        files = os.listdir(path)
        print(f'Files in "{path}":')
        for f in files:
            try:
                os.listdir(f'{path}/{f}')
                print(f'    {f.ljust(20)}DIR')
            except:
                suffix = f.rsplit('.',1)[-1]
                size = len(open(f'{path}/{f}').read())
                for name,maxsize in sizedict.items():
                    if int(size) < maxsize:
                        size = f'{round(size / (maxsize / 1024),2)}{name}'
                        break
                print(f'    {f.split(".")[0].ljust(20)}.{suffix.ljust(10)}{size}')
    else:
        print('No such file of directory')
def todir(to_dir):
    global now_path
    if not to_dir.endswith('/'):
        to_dir = to_dir + '/'
    if to_dir == './':
        now_path = now_path.rsplit('/',1)[0] + '/'
    elif to_dir == '../':
        now_path = now_path.rsplit('/')[0] + '/'
    else:
        if os.path.exists(to_dir):
            now_path = now_path + to_dir
        else:
            print('Path not found')
def runapp(args):
    appname = args.split(' ')[0]
    args = args.split(' ',1)[1].split(',') if ',' in args else [args.split(' ',1)[1]]
    if not os.path.exists(f'TacSystem/Programs/{appname}.py'):
        print('App not found')
    else:
        with open(f'TacSystem/Programs/{appname}.py') as f:
            code = f.read()
        namespace = {}
        exec(code,namespace)
        if not namespace.get('main') or not callable(namespace['main']):
            print('App has damaged')
        else:
            namespace['main'](*args)
# = Run = #
running = True
while running:
    com = input(f'{now_path} >>> ').strip()
    if not com:
        continue
    funn = com.split(' ')[0]
    if funn == 'runapp':
        arg = com.split(' ',1)[1:]
    else:
        arg = com.split(' ')[1:]
    # = analysis = #
    if funn in globals() and callable(globals()[funn]):
        needarg = info.get(funn).get('needArg')
        default = info.get(funn).get('default')
        if default == False:
            if len(arg) != needarg:
                print(f'function "{funn}" needs {needarg} arg ,{len(arg)} given')
                continue
        else:
            if funn != 'runapp':
                if len(arg) > needarg:
                    print(f'function "{funn}" at most {needarg} arg ,{len(arg)} given')
                    continue
        globals()[funn](*arg)
    else:
        print('Bad command or file')
FILES:
DIR&TacSystem:
    DIR&Debug:
        FILE&compileVer.py:
        import shutil
        with open('../version/Ver.version') as f:
            v = f.read()
        print(f'System: {v.split(",")[0].split("=")[1]}')
        print(f'Now version: {v.split(",")[1].split("=")[1]}')
        compile_ver = input('New version: ')
        shutil.move('../version/Ver.version','../version/Ver.txt')
        with open('../version/Ver.txt','w') as f:
            f.write(f'system={v.split(",")[0].split("=")[1]},ver={compile_ver}')
        shutil.move('../version/Ver.txt','../version/Ver.version')
    DIR&version:
        FILE&Ver.version:
        system=TacOS,ver=1.2.4
    FILE&functionInfo.py:
    info = {
        'echo':{'needArg':1,'default':False},
        'listfile':{'needArg':1,'default':True},
        'off':{'needArg':0,'default':False},
        'todir':{'needArg':1,'default':False},
        'istmgr':{'needArg':3,'default':False},
        'runapp':{'needArg':2,'default':True}
    }
