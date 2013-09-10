import os
print os.popen('cd ../lcmd && git pull origin master').read()