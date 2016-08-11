print('\n\n***BEFORE YOU RUN THIS CODE***\n\n')
print('Did you first run `pip freeze > pip_freeze.list` in your terminal *USING* your python2 pip bin??')

userInput =  input('Did you first run `pip freeze > pip2_freeze.list` in your terminal *USING* your python2 pip bin?? [y/n]')

if userInput.lower()[0] == 'y':
  continue
elif userInput.lower()[0] == 'n':
  print('You must first run `pip freeze > pip2_freeze.list` in *this* directory terminal before using this script')
  exit(-1)
else:
  print('You must confirm [y/n] that you first ran `pip freeze > pip2_freeze.list` in *this* directory terminal before using this script')
  exit(-2)

from pandas     import read_csv
from sys        import argv, exit
from subprocess import check_output, call

which_pip = check_output(['/usr/bin/which','pip'])

if which_pip[-1] == 10:
  # 10 corresponds to `'\n'`
  print(True)
  which_pip = which_pip[:-1]

if len(argv) == 1:
  print('Usage: python python2-to-python3_pip_installs.py list\n')
  print('Where you must first run `pip freeze > pip2_freeze.list` in *this* directory terminal before using this script\n')
  exit(-1)

pipfreezelist = read_csv(argv[1])

call([which_pip, 'install', '--upgrade', pipfreezelist2.columns[0].split('==')[0]])
print pipfreezelist2.columns[0].split('==')[0]

for pipnow in pipfreezelist.values:
    call([which_pip, 'install', '--upgrade', pipnow[0].split('==')[0]])
    print(pipnow[0].split('==')[0])
