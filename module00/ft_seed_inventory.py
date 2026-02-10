# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jurres <jurres@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/10 18:37:53 by jurres            #+#    #+#              #
#    Updated: 2026/02/10 18:47:37 by jurres           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(type, amount, what):
    if what == "packets":
        what = f"{amount} packets available"
    elif what == "grams":
        what = f"{amount} grams total"
    else:
        what = f"covers {amount} square meters"
    print(f"{type} seeds: {what}")
ft_seed_inventory("lettuce", 12, "grams")