
def min_int(a: int, b: int):
    if a > b: return b
    else: return a

class Fraction:
    def __init__(self, num: int = 1, den: int = 1) -> None:
        self.num = num
        self.den = den
    
    def __add__(self, other: object):
        if isinstance(other, Fraction):
            return self.add_fraction(other)
    
        elif isinstance(other, int):
            return self.add_int(other)
        
        elif isinstance(other, float):
            print("Float value will be rounded to int when added to fraction.")
            return self.add_int(round(other, 0))
        
        else:
            raise TypeError("Idk how to deal with this type.")
    
    def __iadd__(self, other: object):
        if isinstance(other, Fraction):
            return self.iadd_fraction(other)
    
        elif isinstance(other, int):
            return self.iadd_int(other)
        
        elif isinstance(other, float):
            print("Float value will be rounded to int when added to fraction.")
            return self.iadd_int(round(other, 0))
        
        else:
            raise TypeError("Idk how to deal with this type.")

    def add_fraction(self, other: object):
        if self.den == other.den:
            return Fraction(self.num + other.num, self.den).shorten()

        ex0 = self.num * other.den
        ex1 = other.num * self.den

        return Fraction(ex0 + ex1, self.den * other.den).shorten()

    def iadd_fraction(self, other: object):
        if self.den == other.den:
            self.num += other.num
            self.shorten()
            return self
        
        prev_den = self.den
        self.iexpand(int(other.den))
        self.num += other.num * prev_den
        self.shorten()
        return self

    def add_int(self, other: int):
        return Fraction(self.num + other * self.den, self.den).shorten()

    def iadd_int(self, other: int):
        self.num += other * self.den
        self.shorten()
        return self

    def __mul__(self, other: float):
        if isinstance(other, Fraction):
            return self.mul_fraction(other)
    
        elif isinstance(other, int):
            return self.mul_int(other)
        
        elif isinstance(other, float):
            print("Float value will be rounded to int when added to fraction.")
            return self.mul_int(round(other, 0))
        
        else:
            raise TypeError("Idk how to deal with this type.")
    
    def __imul__(self, other: float):
        if isinstance(other, Fraction):
            return self.imul_fraction(other)
    
        elif isinstance(other, int):
            return self.imul_int(other)
        
        elif isinstance(other, float):
            print("Float value will be rounded to int when added to fraction.")
            return self.imul_int(round(other, 0))
        
        else:
            raise TypeError("Idk how to deal with this type.")
        
    def mul_fraction(self, other: object):
        return Fraction(self.num * other.num, self.den * other.den).shorten()

    def imul_fraction(self, other: object):
        self.num *= other.num
        self.den *= other.den

        self.shorten()
        return self

    def mul_int(self, other: int):
        return Fraction(self.num * other, self.den).shorten()
    
    def imul_int(self, other: int):
        self.num *= other
        self.shorten()
        return self

    def expand(self, other: int):
        if not isinstance(other, int):
            raise TypeError("Must be int??")
        
        return Fraction(self.num * other, self.den * other)

    def iexpand(self, other: int):
        if not isinstance(other, int):
            raise TypeError("Must be int??")

        self.num *= other
        self.den *= other
        return self

    def other_short(self):
        tmp = Fraction(self.num, self.den)

        while True:
            change = False

            for i in range(2, min_int(int(tmp.num), int(tmp.den)) + 1):
            #for i in prime:
                if (tmp.num % i == 0) and (tmp.den % i == 0):
                    tmp.num /= i
                    tmp.den /= i

                    change = True
                    break
            
            if not change: break
        
        return tmp

    def shorten(self):
        while True:
            change = False
            if (self.num % 2 == 0) and (self.den % 2 == 0):
                self.num /= 2
                self.den /= 2
                continue
            
            for i in range(3, min_int(int(self.num), int(self.den)) + 1, 2):
                if (self.num % i == 0) and (self.den % i == 0):
                    self.num /= i
                    self.den /= i

                    change = True
                    break
            
            if not change: break
        
        return self

    def value_aprox(self):
        return self.num / self.den

    def __str__(self) -> str:
        return f"{self.num}/{self.den}"
    
    def __repr__(self) -> str:
        return self.__str__()

def SieveOfEratosthenes(num):
    global prime
    
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1

def main():
    from random import randint
    from time import perf_counter
    SieveOfEratosthenes(100_000)
    #print("Done with sieve.")
    
    MIN_SIZE = 1_000
    MAX_SIZE = 1_000_000
    number = 1000
    
    rand_num = [randint(MIN_SIZE, MAX_SIZE) for _ in range(number)]
    rand_den = [randint(MIN_SIZE, MAX_SIZE) for _ in range(number)]
    rand_fracs = [Fraction(num, den) for (num, den) in zip(rand_num, rand_den)]

    t0 = perf_counter()
    for frac in rand_fracs:
        
        #tmp = frac.other_short()
        frac.shorten()

        #if (frac.num != tmp.num) or (frac.den != tmp.den): print("Uh oh!")

    t1 = perf_counter()
  
    print(f"Shortened {number} fractions between {MIN_SIZE} and {MAX_SIZE} in {t1-t0} seconds.")

if __name__ == "__main__":
    main()