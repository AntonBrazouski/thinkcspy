# Aliasing and Copying

opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
acopy = opposites.copy()

print(acopy is opposites)

acopy['right'] = 'left'
print(opposites['right'])
