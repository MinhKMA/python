import subprocess

def check_process(name_process):
    output = subprocess.check_output(['ps', '-A'])
    if name_process in str(output):
        result = "{0} is running!".format(name_process)
    else:
        result = "{0} is not running".format(name_process)
    return result

result = check_process(name_process='chrome')
print(result)
