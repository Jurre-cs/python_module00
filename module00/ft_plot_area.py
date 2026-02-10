# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jurres <jurres@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/10 17:18:07 by jurres            #+#    #+#              #
#    Updated: 2026/02/10 17:54:39 by jurres           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
	x = input("Enter length: ")
	y = input("Enter width: ")
	x = int(x)
	y = int(y)
	print(f"Plot area: {x * y}")
ft_plot_area()