import argparse

from stegger.steg import convert_to_steg
from stegger.decode import steg_to_message

def main():
    args = get_parse()
    if args.messagepath:
        convert_to_steg(args.messagepath)

    if args.stegpath:
        steg_to_message(args.stegpath)

def get_parse():
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument(
        "-e",
        "--messagepath",
        help = "Convert message to steg"
    )

    ap.add_argument(
        "-d",
        "--stegpath",
        help = "Convert steg to message"
    )
    return ap.parse_args()
