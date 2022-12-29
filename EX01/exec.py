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

def reverse_strings(string) :
    data = ""
    len_s = len(string)
    while (len_s > 0):
        data += string[len_s - 1]
        len_s = len_s - 1
    print(data)

def main() :
    i = 1
    concat = ""
    if (len(sys.argv) >= 2) :
        while (i < len(sys.argv)):
            concat += sys.argv[i]
            concat +=  " "
            i = i + 1;
        reverse_strings(concat)

if __name__ == "__main__":
    main()