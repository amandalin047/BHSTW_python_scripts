def enc(letter, key):
    return chr((ord(letter) + ord(key)) % 1114112)

def dec(letter, key):
    return chr((ord(letter) - ord(key)) % 1114112)

def process(message, key, encrypt):
    if message != None and key != None:
        if encrypt == True:
            answer_message = [enc(x, key[i%len(key)]) for i, x in enumerate(message)]
        elif encrypt == False:
            answer_message = [dec(x, key[i%len(key)]) for i, x in enumerate(message)]
        else: answer_message = None
    else: answer_message=None
    
    return ''.join(answer_message)

def instructions(show):
    if show == 'yes':
        print('cypher_script.py is a script for encrypting/decrupting messages...')
        print('But only when it is run as a script, not imported as a module...')