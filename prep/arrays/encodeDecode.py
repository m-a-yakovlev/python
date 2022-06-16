'''
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.
'''

def encode(strs: 'list[str]') -> str:
    result = ''
    for s in strs:
        result += str(len(s)) + '#' + s
    return result


def decode(str) -> 'list[str]':
    result, i = [], 0 # i -> index of the array(str)

    while i < len(str):
        j = i
        while str[j] != '#':
            j += 1
        length = int(str[i:j])
        result.append(str[j+1 : j+1+length])
        i = j + 1 + length
    
    return result


strs = ["we", "say", "#", "yes"]

print(encode(strs))
print(decode('2#we3#say1##3#yes'))
