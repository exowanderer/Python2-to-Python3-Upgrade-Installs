from sys        import argv, exit, version
from subprocess import check_output, call

print('\n** Works best with converting Anaconda2 to Anaconda3 **\n')

print('\n\n***BEFORE YOU RUN THIS CODE***\n\n')

userInput =  input('Did you first run `pip freeze > pip2_freeze.list` in your terminal *USING* your python2 pip bin?? [y/n]')

if userInput.lower()[0] == 'y':
  pass
elif userInput.lower()[0] == 'n':
  print('You must first run `pip freeze > pip2_freeze.list` in *this* directory terminal before using this script')
  exit(-1)
else:
  print('You must confirm [y/n] that you first ran `pip freeze > pip2_freeze.list` in *this* directory terminal before using this script')
  exit(-2)

if version[0] == '2':
  userInput =  input('Did you already upgrade to Python3 [y/n]')
  
  if userInput.lower()[0] == 'y':
    print('You probably need to add it to your path, because this instance is running in Python2')
    print('Specifically: ' + version)
    exit(-1)
  elif userInput.lower()[0] == 'n':
    print('You have to upgrade to Python3 or this script is will only upgrade your existing packages in Python2\n')
    exit(-1)
  else:
    print('You must confirm [y/n] already upgraded to Python3')
    exit(-2)

which_pip = check_output(['/usr/bin/which','pip'])

if which_pip[-1] == 10:
  # 10 corresponds to `'\n'`
  which_pip = which_pip[:-1]

try:
  from pandas import read_csv
except:
  print('Requires pandas; Script is now installing it\n')
  call([which_pip, 'install', '--upgrade', 'pandas'])

if len(argv) == 1:
  print('Usage: python python2-to-python3_pip_installs.py list\n')
  print('Where you must first run `pip freeze > pip2_freeze.list` in *this* directory terminal before using this script\n')
  exit(-1)

pipfreezelist = read_csv(argv[1])

call([which_pip, 'install', '--upgrade', pipfreezelist2.columns[0].split('==')[0]])
print(pipfreezelist2.columns[0].split('==')[0])

for pipnow in pipfreezelist.values:
    call([which_pip, 'install', '--upgrade', pipnow[0].split('==')[0]])
    print(pipnow[0].split('==')[0])
