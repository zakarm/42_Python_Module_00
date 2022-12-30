# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zmrabet <zmrabet>                          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/29 19:17:39 by zmrabet           #+#    #+#              #
#    Updated: 2022/12/29 19:17:39 by zmrabet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def swap_case(string):
    swapped_string = ""
    for ch in string:
        if ch.isupper():
            swapped_string += ch.lower()
        elif ch.islower():
            swapped_string += ch.upper()
        else:
            swapped_string += ch
    return swapped_string

def reverse_strings(string) :
    data = ""
    for i in range(len(string) - 1, -1, -1):
        data += string[i]
    print(swap_case(data))

def main() :
    if len(sys.argv) >= 2:
        concat = " ".join(sys.argv[1:])
        reverse_strings(concat)

if __name__ == "__main__":
    main()