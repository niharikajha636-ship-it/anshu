import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x skb')
    os.system('./skb')
elif bit == '32bit':
    os.system('chmod +x skb32')
    os.system('./skb32')
else:
    print('device not supported')
