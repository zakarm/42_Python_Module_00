# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zmrabet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/04 15:36:18 by zmrabet           #+#    #+#              #
#    Updated: 2023/01/04 15:59:14 by zmrabet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys 

def main():
    kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }
    for name, author in kata.items() :
        print(name + " was created by " + author)

if __name__ == "__main__" :
    main()