import base64
class decoded_char:
    
    def decode_chars():
        b64_decoded_codes = []
        decoded_codes = []
        decoded_character = []
        
        def get_codes():
            global encoded_codes
            file = open("codes.txt", "r")
            encoded_codes = file.readlines()
            file.close()
            decode_codes()
    
        def decode_codes():
            for j in range(len(encoded_codes)):
                decoded_code = base64.b64decode(encoded_codes[j])
                b64_decoded_codes.append(decoded_code)
                #print(b64_decoded_codes)
            get_nums_from_codes()
        
        def get_nums_from_codes():
            for k in range(len(b64_decoded_codes)):
                ascii_decode = b64_decoded_codes[k].decode("ascii")
                decoded_codes.append(int(ascii_decode))
            #print(decoded_codes)
            assign_characters()
        
        def assign_characters():
            for l in range(len(decoded_codes)):
                decoded_num = int(decoded_codes[l] / 16384)
                decoded_char = chr(decoded_num)
                decoded_character.append(decoded_char)
            #print(decoded_character)
            get_full_text()
        
        def get_full_text():
            full_str = "".join(decoded_character)
            print(f"Entschlüsselter Text: {full_str}\nDieses Programm zu erstellen, hat mir einige Nerven gekostet :D")
            erase_data()
            input("\nDrücke Enter, um das Programm zu schließen")
        
        def erase_data():
            encoded_codes.clear()
            b64_decoded_codes.clear()
            decoded_codes.clear()
            decoded_character.clear()
            return
        
        get_codes()

decoded_char.decode_chars()