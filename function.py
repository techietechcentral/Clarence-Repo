import re
name = "H@ns"
spec_xter = re.compile('!@£$%^&*()')
if spec_xter.search(name) == None:
    print(f'{name} does not contain special characters')
else:
    print(f'{name} contains special characters')