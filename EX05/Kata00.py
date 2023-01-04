# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zmrabet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/30 11:59:37 by zmrabet           #+#    #+#              #
#    Updated: 2023/01/04 15:54:49 by zmrabet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
    k = 0
    kata = (19,42,21)
    len_t = len(kata);
    data = ""
    sys.stdout.write("The " + str(len_t) + " numbers are: ")
    for i in kata :
        data += str(i)
        if (k != len_t - 1):
            data += ","
        k += 1
    print("".join(str(data)));

if __name__ == "__main__":
    main()
