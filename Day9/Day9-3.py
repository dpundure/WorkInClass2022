import alphabet

def is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz'):
    return set(text.lower()) >= set(alphabet)

print(is_pangram("The quick brown fox jumps over a lazy dog"))

a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
print(is_pangram("Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!", alphabet=a_lv))
