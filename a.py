import os

# check every folder of the cic folder
for folder in os.listdir('cic'):
  # check every file of the folder if it has a file named en_US.html, if not, copy the pt_BR.html file to en_US.html
  if not os.path.exists('cic/' + folder + '/en_US.html'):
    print('cic/' + folder + '/en_US.html')
    os.system('cp cic/' + folder + '/pt_BR.html cic/' + folder + '/en_US.html')

