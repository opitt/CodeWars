from itertools import cycle

def encode_rail_fence_cipher(s, n):
    fence = cycle(list(range(n)) + list(range(n-2,0,-1)))
    result = [""] * n
    for c in s:
        f = next(fence)
        result[f] = result[f] + c
    return "".join(result)
    
def decode_rail_fence_cipher(s, n):
    fence = cycle(list(range(n)) + list(range(n-2,0,-1)))
    decoder_template = [[] for _ in range(n)]
    for pos,_ in enumerate(s):
        decoder_template[next(fence)].append(pos)
    
    decoder_input = []
    input_s = s[:]
    for t in decoder_template:
        decoder_input.append(input_s[:len(t)])
        input_s = input_s[len(t):]

    fence = cycle(list(range(n)) + list(range(n-2,0,-1)))
    result = ""
    for pos,_ in enumerate(s):
        f = next(fence)
        result += decoder_input[f][0]
        decoder_input[f] = decoder_input[f][1:]
    return result


s = "WEAREDISCOVEREDFLEEATONCE"
print(encode_rail_fence_cipher(s,3))
s = "WECRLTEERDSOEEFEAOCAIVDEN"
print(decode_rail_fence_cipher(s,3))

x='''
W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C  
    A       I       V       D       E       N    
'''
