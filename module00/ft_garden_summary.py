# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jurres <jurres@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/10 18:29:25 by jurres            #+#    #+#              #
#    Updated: 2026/02/10 18:37:21 by jurres           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
    name = input("Enter garden name: ")
    plant_count = input("Enter number of plants: ")
    print(f"Garden: {name}")
    print(f"Plants: {plant_count}")
    print("Status: Growing well!")
ft_garden_summary()