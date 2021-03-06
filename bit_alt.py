# Copyright (C) 2020 Logan Bier. All rights reserved.

# project details
# a time-bound distributed currency
# that replaces chain exponential energy usage
# with a finite energy distributed ledger
# made up of a randomly generated set of values
# in a range of natural numbers

# conceptually, energy is conserved by awarding the
# winning guess the Nth "coin" in a stepwise registry
# of the vector of secret randomly generated values
# with the Unix Time as a standard of linear computation

# given a finite cycle time to guess the registry value,
# the winning computer is the first one which guesses 
# correctly in a normalized time range across wallets

import random
import time

class main():
    def __init__(self):
        # 10_25_20 the following is a prototype for a much larger system
        self.secret_registry = []
        self.max_coin_length = 10000000  # ten million
        self.random_number_max = 10000000  # ten million
        self.time_amount = 0.001  # 1 millisecond compute slice
        # ten million * ten million requires ~500 megabytes to store
        # these values fully express "Ten Million Coin"

        for x in range(0, self.max_coin_length):
            self.secret_registry.append(random.randint(1, self.random_number_max))

        self.ledger = []
        
        def get_ledger_current_size(input_ledger):
            return len(self.ledger)
        
        # spawn a number of simulated Ten Million Coin "miners"
        def gen_miner_1():
            # take the current length of the distributed ledger 
            # as input on the secret registry to determine the
            # current target value of the process
            # get a unique miner ID
            unique_miner_id = 29304234
            var_1 = get_ledger_current_size(self.ledger)
            guess_this_now = self.secret_registry[var_1]
            current_guess_var = random.randint(1, self.random_number_max)
            print('Miner 1 Current Guess: ' + str(current_guess_var))
            
            if current_guess_var == guess_this_now:
                winning_information = [time.time(), unique_miner_id, var_1, guess_this_now]
                self.ledger.append(winning_information)
                file_1 = open('ten_million_ledger.txt', 'w')
                file_1.write(str(self.ledger))
                file_1.close()
                
        def gen_miner_2():
            # take the current length of the distributed ledger 
            # as input on the secret registry to determine the
            # current target value of the process
            # get a unique miner ID
            unique_miner_id = 12954231
            var_1 = get_ledger_current_size(self.ledger)
            guess_this_now = self.secret_registry[var_1]      
            current_guess_var = random.randint(1, self.random_number_max)
            print('Miner 2 Current Guess: ' + str(current_guess_var))
            
            if current_guess_var == guess_this_now:
                winning_information = [time.time(), unique_miner_id, var_1, guess_this_now]
                self.ledger.append(winning_information)
                file_1 = open('ten_million_ledger.txt', 'w')
                file_1.write(str(self.ledger))
                file_1.close()
                
        while len(self.ledger) < self.max_coin_length:
            time.sleep(self.time_amount)
            print(time.time())
            gen_miner_1()
            gen_miner_2()
            print('Current Length of Ledger: ' + str(len(self.ledger)))
            print('Current Distributed Ledger: ' + str(self.ledger))

main()
