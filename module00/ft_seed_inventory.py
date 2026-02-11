# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jurres <jurres@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/10 18:37:53 by jurres            #+#    #+#              #
#    Updated: 2026/02/11 02:55:47 by jurres           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(type, amount, what):
    if what == "packets":
        what = f"{amount} packets available"
    elif what == "grams":
        what = f"{amount} grams total"
    elif what == "area":
        what = f"covers {amount} square meters"
    else:
        what = "ERROR"
    if what == "ERROR":
        print(f"{what}")
    else:
        print(f"{type} seeds: {what}")
ft_seed_inventory("lettuce", 12, "grams")