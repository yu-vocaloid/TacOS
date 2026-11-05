#TacOStpkg install 1.0
#Signaturepublisher=TacOS
code = 'def main(code):\n    try:\n        exec(code)\n    except Exception as error:\n        print("Your Python has been crashed!")\n        print()\n        print(e)'
def INSTALLMAIN():
    print('==========Install==========')
    print('Installing Python...')
    print('Please refer to the license terms below:')
    print('(1) This is a voluntary install by the user (you), Any consequences arising thereform shell be borne by the user (you) themselves.')
    print('(2) The right of interpretation belongs to the author.')
    answer = input('\nDo you agree to this license terms? (y/n):')
    if answer == 'n':
        print('You must agree to the license terms before we can provide installation services.')
        return 0
    print('Installing Python.py (1/1)...')
    with open('TacSystem/Programs/Python.py','w') as f:
        f.write(code)
    print('Install success!')
