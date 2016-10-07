
"""
Birthday paradox sample test
By: Sandra Escandor-O'Keefe

This program demonstrates finding the threshold number that guarantees
that no two people will have the same birthday
"""

from random import randint


class Possible_choices():

    def __init__(self, size):
        self.choices = [0] * size 
        self.size = size

    def choose(self):
        
        choice = randint(0, self.size-1)

        #print "Choice:" + str(choice)

        if 0 == self.choices[choice]:
            self.choices[choice] = 1
            return True
        else:
            return False

def test():
    size = 365
    count = 0
    set_of_choices = Possible_choices(size)

    for i in range(0, size):
        if set_of_choices.choose():
            count = count + 1
        else:
            break
    
    #print "Number of choices before collision:" + str(count)

    return count


def main():

    iterations = 1000
    count = 0

    for x in range(0, iterations):
        count = count + test()
    
    avg_count = count/iterations

    print "With 365 day (assuming even distribution of birthdays), the \
    possible number of people in a room that will ensure that NO two people \
    have the same birthday tends to:" + str(avg_count)

if __name__ == '__main__':
    main()
