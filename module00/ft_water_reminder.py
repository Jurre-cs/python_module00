# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jurres <jurres@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/10 17:50:31 by jurres            #+#    #+#              #
#    Updated: 2026/02/10 18:07:53 by jurres           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    days = input("Days since last watering: ")
    days = int(days)
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
ft_water_reminder()