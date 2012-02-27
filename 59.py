import string, sys

s = open('files/cipher1.txt','r').read()

chars           = [int(c) for c in string.split(s.rstrip(),',')]
decrypted_chars = [None]*len(chars)

low_case_range=range(ord('a'),ord('z')+1)

for i in low_case_range:
    for j in low_case_range:
        for k in low_case_range:
            decrypted_chars[::3] =[chr(c^i) for c in chars[::3]]
            decrypted_chars[1::3]=[chr(c^j) for c in chars[1::3]]
            decrypted_chars[2::3]=[chr(c^k) for c in chars[2::3]]
            
            s_decrypted=string.join(decrypted_chars,'')

            if string.find(s_decrypted, "and")  >= 0 and \
               string.find(s_decrypted, "the")  >= 0 and \
               string.find(s_decrypted, "is")   >= 0 and \
               string.find(s_decrypted, "that") >=0:
                print sum([ord(c) for c in s_decrypted])
                sys.exit()
