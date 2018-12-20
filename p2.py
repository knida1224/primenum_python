#Part A
#Prime generator up to a given value n
class PrimeSeq(object):

    #initialization
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.last = 1

    def __iter__(self):
        return self

    #Function for prime check
    def is_prime(self, n):

        if n >= 2:
            for m in range(2, n):
                if not (n%m):
                    return False

        else:
            return False

        return True

    #Finds prime number, 
    #checks with is_prime 
    #and returns if prime
    def next_prime(self):

        n = self.last + 1

        #iterator
        while not self.is_prime(n):
            n = n + 1

        self.last = n
        self.count = self.count + 1

        return n

    #__next__() returns either the
    #next prime or raises StopInteration
    #error if desired number of primes
    #have already been generated, as instructed
    def __next__(self):
        if self.count == self.n:
            raise StopIteration
        else:
            return self.next_prime()

#Part B
def prime_gen(n):

    prime_lst  = [] #list of n primes
    test = 2 #number being tested starting at 2

    #length of list must be less than n
    #while loop keeps that constraint and
    #checks if the number is prime or not 
    #and adds it to the list, increase test
    while len(prime_lst) < n:

        #checks if remainder is zero (prime)
        list_check = [test for i in prime_lst if test%i == 0]

        #adds to list if list_check is true
        prime_lst += [] if list_check else [test]
        test += 1

    #returns list of primes
    return prime_lst

def main():
    #Test given by assignment
    print("--Part A--")
    primeseq = PrimeSeq(25)

    for p in primeseq:
        print(p)

    primes_lst = [p for p in PrimeSeq(25)]

    print(primes_lst)
    print()

    #Test given by assignment 
    print("--Part B--")
    print("First 10 prime numbers are: ")
    for p in prime_gen(10):
        print(p)

if __name__ == '__main__':
    main()
