# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jurres <jurres@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/10 17:55:29 by jurres            #+#    #+#              #
#    Updated: 2026/02/11 02:42:54 by jurres           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    Days = int(input("Days until harvest: "))
    i = 0
    for i in range(Days):
        i = i + 1
        print(f"Day {i}")
    print("Harvest time!")

ft_count_harvest_iterative()