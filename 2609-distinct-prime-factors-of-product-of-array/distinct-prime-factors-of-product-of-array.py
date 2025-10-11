class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        array_product = 1

        for num in nums:
            array_product *= num
        
        def primeFactorization(n):
            factors = set()
            
            # Handle 2s
            while n % 2 == 0:
                factors.add(2)
                n //= 2
            
            # Handle odd factors from 3 onwards
            i = 3
            while i * i <= n:
                while n % i == 0:
                    factors.add(i)
                    n //= i
                i += 2
            
            # If n is a prime greater than 2
            if n > 2:
                factors.add(n)
            
            return factors

        return len(primeFactorization(array_product))