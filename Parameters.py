def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'    
    elif lang == 'Fa':
        return 'salam'
    else:
        return 'Hello'

print(greet('en'),'Glenn')
print(greet('es'),'Sally')
print(greet('fr'),'Michael')
print(greet('Fa'),'sara')
