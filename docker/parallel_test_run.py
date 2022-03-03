from subprocess import Popen


processes = []

for counter in range(10):
    chrome_cmd = 'set BROWSER=chrome && python test.py'
    firefox_cmd = 'set BROWSER=firefox && python test.py'
    processes.append(Popen(chrome_cmd, shell=True))
    processes.append(Popen(firefox_cmd, shell=True))

for counter in range(10):
    processes[counter].wait()