def primes(limit):
    if limit < 2:
        return []
    
    unmarked = set(range(2, limit+1))
    prime = []
    
    for n in range(2, limit+1):
        if n in unmarked:
            prime.append(n)
            multiple = n * n
            while multiple <= limit:
                unmarked.discard(multiple)
                multiple += n
    return prime
