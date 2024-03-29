import random
import os
import base64
class encrypted_char:
    def __init__(self, _id, enc, I_NUMB) -> None:
        self.identification = _id
        self.encoded = enc
        self.real_id = ord(_id)
        self.enc_identification_number = I_NUMB
    
    def encode_characters():
        for i in range(len(chars)):
            chars[i].enc_identification_number = random.randint(0,16384)
            chars[i].encoded = chr(chars[i].enc_identification_number)
        
        encrypted_char.encode()
    
    def encode():
        os.system("cls")
        print("Schreibe hier die Nachricht, die verschlüsselt werden soll\n")
        msg_str = str(input("> "))
        encoded_list = []
        encoded_codes = []
        for char in str(msg_str):
            for i in range(len(chars)):
                if char.lower() == chars[i].identification:
                    encoded_list.append(chars[i].encoded)
                    encoded_codes.append(chars[i].real_id)
        global encoded_str
        encoded_str = "".join(encoded_list)

        def b64_encode_codes():
            global b64_codes
            b64_codes = []
            for i in range(len(encoded_codes)):
                sample_string = str(encoded_codes[i] * 16384)
                sample_string_bytes = sample_string.encode("ascii")
                base64_bytes = base64.b64encode(sample_string_bytes)
                base64_str = base64_bytes.decode("ascii")
                b64_codes.append(base64_str)
            return
        
        b64_encode_codes()
        encrypted_char.decode(encoded_str)

    
    def decode(encoded_str):
        os.system("cls")
        decoded_list = []
        for char in str(encoded_str):
            for i in range(len(chars)):
                if char == chars[i].encoded:
                    decoded_list.append(chars[i].identification)
        global decoded_str
        decoded_str = "".join(decoded_list)
        encrypted_char.show_all()
    
    def show_all():
        print(f"Verschlüsselte Nachricht: {encoded_str}\nEntschlüsselte Nachricht: {decoded_str}\n")

        input("Drücke Enter, um alle Buchstaben zu sehen\n")
        os.system("cls")
        print(f"Alle Buchstaben:")
        for i in range(len(chars)):
            print(f"{chars[i].identification}: {chars[i].encoded}")
        
        with open("codes.txt", "w") as file:
            for i in range(len(encoded_str)):
                file.write(f"{b64_codes[i]}\n")
        
        input("Drücke Enter, um das Programm zu schließen\n")
        os.system("cls")

a = encrypted_char("a", 0, 0,)
b = encrypted_char("b", 0, 0,)
c = encrypted_char("c", 0, 0,)
d = encrypted_char("d", 0, 0,)
e = encrypted_char("e", 0, 0,)
f = encrypted_char("f", 0, 0,)
g = encrypted_char("g", 0, 0,)
h = encrypted_char("h", 0, 0,)
i = encrypted_char("i", 0, 0,)
j = encrypted_char("j", 0, 0,)
k = encrypted_char("k", 0, 0,)
l = encrypted_char("l", 0, 0,)
m = encrypted_char("m", 0, 0,)
n = encrypted_char("n", 0, 0,)
o = encrypted_char("o", 0, 0,)
p = encrypted_char("p", 0, 0,)
q = encrypted_char("q", 0, 0,)
r = encrypted_char("r", 0, 0,)
s = encrypted_char("s", 0, 0,)
t = encrypted_char("t", 0, 0,)
u = encrypted_char("u", 0, 0,)
v = encrypted_char("v", 0, 0,)
w = encrypted_char("w", 0, 0,)
x = encrypted_char("x", 0, 0,)
y = encrypted_char("y", 0, 0,)
z = encrypted_char("z", 0, 0,)
spacebar = encrypted_char(" ", 0, 0)
chars = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,spacebar]
x = ord(" ")
print(x)
encrypted_char.encode_characters()