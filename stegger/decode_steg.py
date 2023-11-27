def get_steg(filepath):
    f = open(filepath, "r").read().split("\n\n")
    return [len(l) for l in f]

def steg_to_bins(nums):
    bins = []
    for n in nums:
        if n >= 1025:
            n -= 1025
        bins.append(bin(n)[2:].zfill(10))
    return bins

def get_bin_str(bins):
    return "".join(bins)

def split_bin_str(bin_str, base):
    bins = []
    for i in range(0, len(bin_str), base):
        if i + base > len(bin_str):
            base = len(bin_str) - i
        bins.append(bin_str[i:i+base])
    return bins

def remove_separator(bin_str, last_char):
    chunk = ""
    base = len(last_char)
    for i in range(len(bin_str)-1, -1, -1):
        if len(chunk) < len(last_char):
            chunk = bin_str[i] + chunk
        else:
            chunk = bin_str[i] + chunk[:-1]
            if chunk == last_char:
                break
            bin_str = bin_str[:-1]
    return bin_str

def get_message(bins):
    chars = []
    for b in bins:
        char = chr(int(b,2))
        chars.append(char)
    with open("message.py", "w") as f:
        f.write("".join(chars))

def steg_to_message(filepath):
    steg = get_steg(filepath)
    bins = steg_to_bins(steg)
    bin_str = get_bin_str(bins)
    bin_str = remove_separator(bin_str, bin(ord("#"))[2:])
    bins = split_bin_str(bin_str, 7)
    get_message(bins)
