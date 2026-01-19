# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: abdnahal <abdnahal@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/18 16:48:52 by abdnahal          #+#    #+#              #
#    Updated: 2026/01/18 17:41:34 by abdnahal         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant :
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def age(self) :
        self.age += 1
    def grow(self) :
        self.height += 1
    def get_info(self) :
        print(f"{self.name}: {self.height}cm, {self.age} days old")

def main() :
    Sunflower = Plant("Sunflower", 250, 90)
    print("=== Day 1 ===")
    Sunflower.get_info()
    k = 0
    for i in range(1, 7) :
        Sunflower.age()
        Sunflower.grow()
    print("=== Day 7 ===")
    Sunflower.get_info()
    print(f"Growth this week: +{i}cm")
        
if __name__ == "__main__":
    main()