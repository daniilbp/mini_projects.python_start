def cipher_cezar(secret):
    decoding_1 = ''.join(
        [
            alphabet[alphabet.find(secret[i_letter]) - 3]
            if secret[i_letter] in alphabet
            else secret[i_letter]
            for i_letter in range(len(secret))
        ]
    ).split(' ')
    return decoding_1

def shift(secret_2):
    decoding_2 = ''
    num = 3
    for word in secret_2:
        new_word = [lt for lt in word]
        new_new_word = ''.join(
            [new_word[(i_num + len(new_word) - num) % len(new_word)] for i_num in range(len(new_word))])
        decoding_2 += new_new_word + ' '
        if '/' in word:
            num += 1
    return decoding_2

input_text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
alphabet = 'Aa?Bb?Cc?Dd?Ee?Ff?Gg?Hh?Ii?Jj?Kk?Ll?Mm?Nn?Oo?Pp?Qq!Rr"Ss*Tt+Uu-Vv.Ww,Xx-Yy`Zz('

cipher = cipher_cezar(input_text)
output_text = shift(cipher)

output_text = output_text.replace('/ ', '.\n')
print(output_text)
