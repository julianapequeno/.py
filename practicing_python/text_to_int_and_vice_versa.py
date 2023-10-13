#just for practicing python coding

##############ENCODING FROM TEXT TO INT (ASCII CODE)

frase_input = input()
encoding_by_ascii = list(map(ord,frase_input.upper()))

secret_number = ' '
for n in encoding_by_ascii:
    secret_number  = secret_number + str(n)

print(secret_number)


##########DECODING FROM INT TO TEXT (ASCII CODE)

initial_sequence = list(input())

sequence = list(filter(lambda x: x ,map(int,initial_sequence)))

init_list_seq = []

#sppliting into multiples partes
chunk_size = 2
while sequence:
    chunk, sequence = sequence[:chunk_size], sequence[chunk_size:]
    init_list_seq.append(tuple(chunk))
print(init_list_seq)


final_phrase = ''
for (first, sec) in init_list_seq:
    num = str(first).__add__(str(sec))
    charac = chr(int(num))
    if charac is not int:
        final_phrase += charac

print(final_phrase)