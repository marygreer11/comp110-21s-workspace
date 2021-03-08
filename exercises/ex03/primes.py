"""EX03 - prime functions."""

__author__: str = "730394883"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(31))
    print(list_primes(3, 7))


def is_prime(x: int) -> bool:
    """Identifying prime numbers."""
    prime = False
    if x < 2:
        return False
    else:
        for num in range(2, x):
            if x % num == 0:
                prime = True
                break
            if prime == True:
                return False
            return True


def list_primes(x: int, y: int) -> list[int]:
    """Making a list of primes."""
    final_list = []
    for num in range(x, y):
        if is_prime(num) is False:
            break
        else:
            if is_prime(num) is True:
                final_list.append(num)
    return final_list
   
        
if __name__ == "__main__":
    main()