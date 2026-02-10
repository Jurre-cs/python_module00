# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jurres <jurres@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/10 17:30:02 by jurres            #+#    #+#              #
#    Updated: 2026/02/10 17:54:41 by jurres           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	x = input("Day 1 harvest: ")
	y = input("Day 2 harvest: ")
	z = input("Day 3 harvest: ")
	x = int(x)
	y = int(y)
	z = int(z)
	x = x + y + z
	print(f"total harvest: {x}")
ft_harvest_total()