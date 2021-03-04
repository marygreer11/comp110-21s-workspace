"""EX03 - prime functions."""

__author__: str = "730394883"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(31))
    print(list_primes(3,7))


def is_prime(x:int) -> bool:
    if x <= 1:
       return False
    else:
     if x % 2 or 3 == 0:
        return True
     else:
          if x % 2 or 3 != 0:
              return False


def list_primes(min: int, max: int) -> list[int]:
   final_list: list[int] = [0]
   for num in range(min, max):
     while num >= 1:
         if is_prime(num) == False:
             break
         else:
             if is_prime(num) == True:
                final_list.append(num)
         num += 1
         return final_list
   
        






if __name__ == "__main__":
    main()