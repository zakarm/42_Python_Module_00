# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zmrabet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/05 14:30:46 by zmrabet           #+#    #+#              #
#    Updated: 2023/01/05 14:43:38 by zmrabet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
    if len(sys.argv) == 3 and not sys.argv[1].isnumeric():
        data = []
        data = sys.argv[1].split()
        print(data)
    else :
        print("ERROR")

if __name__ == "__main__" :
    main()