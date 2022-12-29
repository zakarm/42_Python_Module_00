import sys

def reverse_strings(string) :
    len_s = len(string)
    while (len_s >= 0):
        print(string[len_s])
        len_s = len_s - 1

def main() :
    reverse_strings(sys.argv[0])

if __name__ == "__main__":
    main()