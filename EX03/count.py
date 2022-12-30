# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zmrabet <zmrabet>                          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/30 11:46:06 by zmrabet           #+#    #+#              #
#    Updated: 2022/12/30 11:46:06 by zmrabet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string 

def punc_c(string_c):
    count = 0
    for i in string_c :
        if (i in string.punctuation):
            count += 1
    return count

def text_analyzer(string_c) :
    upper = punc = lower = space = 0
    for i in string_c :
        if (i.isupper()):
            upper += 1
        elif (i.islower()):
            lower += 1
        elif (i.isspace()):
            space += 1
    punc = punc_c(string_c)
    print("- " + str(upper) + " upper letter(s)")
    print("- " + str(lower) + " lower letter(s)")
    print("- " + str(punc) + " punctuation mark(s)")
    print("- " + str(space) + " space(s)")
        
def main():
    if (len(sys.argv) == 2):
        text_analyzer(sys.argv[1])
    elif (len(sys.argv) > 2):
        print("AssertionError: more than one argument are provided")

if __name__ == "__main__" :
    main()