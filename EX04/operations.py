# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zmrabet <zmrabet>                          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/30 11:46:01 by zmrabet           #+#    #+#              #
#    Updated: 2022/12/30 11:46:01 by zmrabet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
    if (len(sys.argv) == 3):
        if (not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric()) :
            print("AssertionError: argument is not an integer")
            exit()
        print("Sum:        "+ str(int(sys.argv[1]) + int(sys.argv[2])))
        print("Difference: "+ str(int(sys.argv[1]) - int(sys.argv[2])))
        print("Product:    "+ str(int(sys.argv[1]) * int(sys.argv[2])))
        if (int(sys.argv[2]) == 0) :
            print("Quotient:   ERROR (division by zero)")
            print("Remainder:  ERROR (modulo by zero)")
        else :
            print("Quotient:   "+ str(int(sys.argv[1]) / int(sys.argv[2])))
            print("Remainder:  "+ str(int(sys.argv[1]) % int(sys.argv[2])))
    elif (len(sys.argv) > 3):
        print("AssertionError: more than one argument are provided")
    elif (len(sys.argv) == 2):
        print("AssertionError: less than two argument are provided")

if __name__ == "__main__" :
    main()