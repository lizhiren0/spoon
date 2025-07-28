from sys import argv, stderr, exit

RED = r'\033[91m'
RESET = r'\033[0m'

with open(argv[1], 'r') as f:
    code = f.read()

if code == 'spoon':
    print('Hello, World!')
else:
    print(f'{RED}Unacceptable cutlery.{RESET}', file=stderr)
    exit(1)