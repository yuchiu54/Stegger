import random
import secrets
import string

def convert_bin_str(message):
    result = []
    for char in message:
        result.append(f"{ord(char):07b}")
    return "".join(result)
    
def adjust_sub_bin(sub_bin):    
    # number aren't necessary to be under 64 but must larger than 0
    if int(sub_bin, 2) == 0:
        sub_bin = bin(1025)[2:]
#    if int(sub_bin, 2) <= 64:    
#        sub_bin = bin(int(sub_bin, 2) + 1025)[2:]    
    return sub_bin    
    
def split_bin(bin_str, base=10):    
    sub_bins = []    
    for i in range(0, len(bin_str), base):    
        chunk = bin_str[i:]    
        if len(chunk) > base:    
            chunk = chunk[0:base]    
        chunk = adjust_sub_bin(chunk)    
        sub_bins.append(chunk)    
    return sub_bins 

def gen_fake_data(length):    
    pool = string.ascii_letters + string.digits + string.punctuation + " "
    return "".join(random.choices(pool, k=length))

def gen_steg(sub_bins):
    output = []
    for b in sub_bins:
        data = gen_fake_data(int(b, 2)) + "\n\n"
        output.append(data)
    with open("output.txt", "w") as f:
        f.write("".join(output))

def convert_to_steg(filepath):
    # append # * 5 at the end of input to be separate line for decoding
    # I choose ")" as a mark for end of script. Combination of \n and space
    # in binary will misleading algorithm to stop at wrong index.
    f = open(filepath, "r").read()[:-1] + "#" * 5
    bin_str = convert_bin_str(f)
    sub_bins = split_bin(bin_str)
    gen_steg(sub_bins)
