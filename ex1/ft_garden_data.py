# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abdnahal <abdnahal@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/18 16:35:50 by abdnahal          #+#    #+#              #
#    Updated: 2026/01/18 16:46:56 by abdnahal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant :
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

def main() :
    Jassmin = Plant("Jassmin", 190, 25)
    Corn = Plant("Corn", 90, 15)
    Sunflower = Plant("Sunflower", 250, 90)
    all = [Jassmin, Corn, Sunflower]
    print("=== Garden Plant Registry ===")
    for i in range(3):
        print(f"{all[i].name}: {all[i].height}cm, {all[i].age} days old")

if __name__ == "__main__":
    main()