def morse(text):
    d_morse = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
         'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
         'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
         'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
         'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
         'Z':'--..', ' ':'.....'}
    
    decode = ''

    if text.startswith('.') or text.startswith('-'):
        dict_encrypt = dict([(value,key) for key,value in d_morse.items()])
        text = text.split(' ')
        for x in text:
            decode += dict_encrypt.get(x)
    else:
        text = text.upper() 
        for x in text:
            decode += d_morse.get(x) + ' '
    return decode.strip()
    
print(morse("Major League Hacking"))
print(morse('-- .- .--- --- .-. ..... .-.. . .- --. ..- . ..... .... .- -.-. -.- .. -. --.'))
