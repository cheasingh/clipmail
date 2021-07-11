import pyperclip
import re

raw_email = pyperclip.paste()
reg_email = re.compile(r'''
    \w*[._-]?\w* # suffix can include . - _
    @+\w* # domain
    .*\w # suffix ''',
                       re.VERBOSE)

result = reg_email.findall(raw_email)

if len(result) == 0:
    pyperclip.copy('No email found!')
    exit()

pyperclip.copy('\n'.join(result))
