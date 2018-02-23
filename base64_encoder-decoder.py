base64_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
base64_letters.split()
stroka = b"ABC"

def encode_base64(data):
  byte_string = ""
  bit_string = ""
  base64_string = ""
  byte6_string = []
  
  for element in data:
    byte_string += "{:08b}".format(element)
  
  for byte in range(0, len(byte_string), 6):
    byte6_string.append(byte_string[byte:byte+6])
  
  for base64_symbol in byte6_string:
    if len(base64_symbol) < 6:
      base64_symbol = base64_symbol + (6-len(base64_symbol))*"0"
    base64_string += base64_letters[int(base64_symbol, 2)]
    
  return base64_string

def decode_base64(data):
	byte_string = ""
	byte8_list = []
	result = ""
	
	for element in data:
		if element in base64_letters:
			byte_string += "{:06b}".format(base64_letters.index(element))
	
	for byte in range(0, len(byte_string), 8):
		byte8_list.append(byte_string[byte:byte+8])
	
	for symbol in byte8_list:
		result += chr(int(symbol, 2))
	
	return result		



		
