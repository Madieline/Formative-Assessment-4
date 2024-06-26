def bin_to_dec(binary_string):
    disected_list = list(binary_string)
    number_list = [int(item) for item in disected_list]

    binary_calculation = 0
    for i in range(len(number_list)):
        binary_calculation += number_list[i] * (2  ** (len(number_list) - 1 - i))
    
    return int(binary_calculation)

def dec_to_bin(number):
    binary = [number]
    while number > 1:
        number //= 2
        binary.append(number)

    arranged_list = binary[::-1]
    
    final_list = []
    counter = 0

    while counter < len(arranged_list):
        if arranged_list[counter] % 2 == 0:
            final_list.append("0")
            counter += 1
        else:
            final_list.append("1")
            counter += 1
    
    return "".join(final_list)

def telephone_cipher(message):
    encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }

    encoded = ""
    disected_list = list(message)
    i = 0 
    while i < len(disected_list):
        value = encoder_dict.get(disected_list[i], "")
        encoded += value 
        if i + 1 < len(disected_list):
            if encoder_dict.get(disected_list[i], "") in encoder_dict.get(disected_list[i + 1], ""):
                encoded += "_"
            elif encoder_dict.get(disected_list[i + 1], "") in encoder_dict.get(disected_list[i], ""):
                encoded += "_"
        i += 1

    return encoded

def telephone_decipher(telephone_string): 
    decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }
    start = 0
    end = 0
    disected_list = []
    
    while end < len(telephone_string):
        if telephone_string[start] == telephone_string[end]:
            end += 1 
            if end == len(telephone_string):
                sublist = telephone_string[start:end]
                disected_list.append(sublist)
                break
        else:
            sublist = telephone_string[start:end]
            disected_list.append(sublist)
            start = end 

    deciphered_message = []
    for item in disected_list:
        if item == "_":
            deciphered_message.append("")
        else: 
            corresponding_letter = decipher_dict[item] 
            deciphered_message.append(corresponding_letter)

    return "".join(deciphered_message)

