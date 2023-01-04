# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zmrabet <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/01/04 16:00:44 by zmrabet           #+#    #+#              #
#    Updated: 2023/01/04 16:32:13 by zmrabet          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import datetime

def main():
    kata = (2019, 9, 25, 3, 30)
    time = datetime.datetime(kata[0], kata[1], kata[2], kata[3], kata[4])
    print(time.strftime("%m/%d/%Y %H:%M"))

if __name__ == "__main__":
    main()