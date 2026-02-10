# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jurres <jurres@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/10 17:55:29 by jurres            #+#    #+#              #
#    Updated: 2026/02/10 18:28:27 by jurres           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    Days = int(input("Days until harvest: "))
    i = 0
    for i in range(Days):
        i = i + 1
        print(f"Day {i}")
    print("Harvest time!")

def ft_count_harvest_recursive(Days = None, i = 0):
    if Days is None:
        Days = int(input("Days until harvest: "))
    if i == Days:
        print("Harvest time!")
        return
    print(f"Day {i + 1}")
    ft_count_harvest_recursive(Days, i + 1)

ft_count_harvest_recursive()