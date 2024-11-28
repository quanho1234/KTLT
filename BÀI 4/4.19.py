print("Sinh vien: Ho Anh Quan")
print("Ma so SV : 235752021610088")
print("#######################################")
################################################
limit = 1000000
is_prime = [True] * limit
is_prime[0], is_prime[1] = False, False
for i in range(2, int(limit ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, limit, i):
            is_prime[j] = False
primes = [i for i in range(limit) if is_prime[i]]
P = tuple(primes)
print(f"Total primes found: {len(P)}")
