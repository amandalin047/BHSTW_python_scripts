import useful_functions as use  
import os
import argparse

def cypher_main(msgfile, key, mode):
    try: 
        ftitle=os.path.basename(msgfile)[:-4]  
        m = open(msgfile, encoding='utf-8')
        text = m.read()
        m.close
    except (FileNotFoundError, TypeError): print('\nYou have entered None type or invalid objects')
    else:
        if mode == 'enc':
            ans = use.process(text, key, True)
            f = open(ftitle + '_encrypted.txt', 'w')  
            f.write(ans)
            f.close()
            print('\nEncrypted file saved as ' + ftitle + '_encrypted.txt !')
        elif mode == 'dec':
            ans = use.process(text, key, False)
            f = open(ftitle + '_decrypted.txt', 'w')
            f.write(ans)
            f.close()
            print('\nDecrypted file saved as ' + ftitle + '_decrypted.txt !')
        else: print('\nYou have entered None type or invalid objects')
    finally: pass

def sort_names(namesfile, mode):
    try:
        n = open(namesfile)
        text = n.read().split()
        n.close()
        text.sort(key=len)
        if mode == 'ascend': print('\n', text)
        elif mode == 'descend': print('\n', [text[-i] for i in range(1, len(text)+1)])
        else: print('\nYou have entered None type or invalid objects')

    except (FileNotFoundError, TypeError): print('\nYou have entered None type or invalid objects')

def argparse_func():
    parse = argparse.ArgumentParser()
    parse.add_argument('--show', dest='show',
                       help='whether to show instructions',
                       choices=['yes', 'no'],
                       required=True)
    parse.add_argument('--message', dest='msg',
                       help='the path to a text files containing the message',
                       required=False)
    
    parse.add_argument('--key', dest='key',
                       help='a string directly containing the key',
                       required=False)
    parse.add_argument('--mode', dest='mode',
                       help='a string that can take the value enc or dec',
                       choices=['enc', 'dec', 'ascend', 'descend'],  
                       required=False)
    args=parse.parse_args()
    return args

args = argparse_func()
use.instructions(show=args.show)

  
if __name__=="__main__":
    cypher_main(args.msg, args.key, args.mode)