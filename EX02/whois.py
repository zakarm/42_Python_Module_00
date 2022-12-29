# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zmrabet <zmrabet>                          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/29 20:05:19 by zmrabet           #+#    #+#              #
#    Updated: 2022/12/29 20:05:19 by zmrabet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
    if (len(sys.argv) == 2):
        
        if (not sys.argv[1].isnumeric()) :
            print("AssertionError: argument is not an integer")
            exit()
        number = int(sys.argv[1])
        if (number == 0) :
            print("I'm Zero.")
        elif (number % 2 == 0):
            print("I'm Even.")
        elif (number % 1 == 0) :
             print("I'm Odd.")
    elif (len(sys.argv) > 2) :
        print("AssertionError: more than one argument are provided")

if __name__ == "__main__":
    main()