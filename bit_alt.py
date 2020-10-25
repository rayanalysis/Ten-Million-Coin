# Copyright (C) 2020 Logan Bier
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# project details
# a time-bound distributed currency
# that replace blockchain exponential energy usage
# with a finite energy distributed ledger
# made up of a randomly generated set of values
# in a range of natural numbers

import random

class main():
    def __init__(self):
        ledger = int(310783912)
        print(ledger)

        self.secret_registry = []
        self.max_coin_length = 10000000  # ten million
        self.random_number_max = 10000000  # ten million (to save memory)
        # ten million * ten million requires ~500 megabytes to store
        # these values fully express "Ten Million Coin"

        for x in range(0, self.max_coin_length):
            self.secret_registry.append(random.randint(1, self.random_number_max))

        self.party = []
        self.value = []
        self.ledger = []

main()
