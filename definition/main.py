from definition import definition
import time
import os

import argparse

def _say(sentence, sleepseconds=0.5):
    os.system("say '{0}'".format(sentence))
    time.sleep(sleepseconds)

def main():
    parser = argparse.ArgumentParser(description="Definitions")
    parser.add_argument("word", help="Word for definition", type=str)
    parser.add_argument("-f", "--force", action="store_true", help="Bypass cache")
    parser.add_argument("-mtc","--max-type-count", help="Max Type Count", default=2)
    parser.add_argument("-mdf","--max-def-count", help="Max Def Count", default=2)

    args = parser.parse_args()
    # print(args)

    return_text = definition(args.word,
                max_type_count = args.max_type_count,
                max_def_count = args.max_type_count, force=args.force)
    
    print(return_text)
    text = return_text.split("\n")
    for t in text:
        if len(t):
            _say(t)



if __name__ == "__main__":
    main()