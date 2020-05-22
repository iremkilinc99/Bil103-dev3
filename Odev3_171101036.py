# coding=utf-8 
import crypt
import string
import itertools 
        
def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        if cryptWord == cryptPass:
            print('Found Password: '+word)
            return

def testPassTwo(cryptPass):
    attempts=0
    salt = cryptPass[0:2]
    chars=string.digits
 
    for password_length in range(7):
      for guess in itertools.product(chars,repeat=password_length):  
         attempts+=1 
         guess=''.join(guess)          
         cryptWord = crypt.crypt(guess,salt)
         if cryptWord == cryptPass:
             print(guess)
            # return 'password is {}.'.format(guess)    
        # print(cryptWord,attempts)
            



def testPassThree(cryptPass):
    attempts=0
    salt = cryptPass[0:2]
    chars=string.ascii_uppercase+string.ascii_lowercase+string.digits
   
    for password_length in range(4):
        for guess in itertools.product(chars,repeat=password_length):
            attempts+=1             
            guess=''.join(guess)
            cryptWord = crypt.crypt(guess,salt)
            if cryptWord == cryptPass:
              print(guess)
                # return 'password is {}.'.format(guess)    
            #print(cryptWordS,attempts)



def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip('\n')
            print("Cracking Password for: "+user)
            testPass(cryptPass)
            testPassTwo(cryptPass)
            testPassThree(cryptPass)
main()
