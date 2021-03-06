def read_list():
    list = []
    vector = input("Dati lista: ")
    numere = vector.split(" ")
    for x in numere:
        list.append(int(x))
    return list


def list_is_even(l):
    """Functia verifica daca toate numerele dintr-o lista sunt pare

    Args:
        l (list[int]): o lista de numere intregi

    Returns:
          True: cand o lista are toate numerele pare
          False: cand o lista are cel putin un numar impar
    """
    for x in l:
        if x % 2 == 1:
            return False
    return True

def get_longest_all_even(l):
    """Returneaza cea mai mare subsecventa de numere pare a unui sir

    Args:
        l (list[int]): [o lista de numare intregi]

    Returns:
        subsecventa_max (list[int]): [cea mai lunga subsecventa de numere pare]
    """
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if list_is_even(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i:j + 1]
    return subsecventa_max

def test_get_longest_all_even():
    assert get_longest_all_even([2, 2, 2, 3, 4, 7, 7]) == [2, 2, 2]
    assert get_longest_all_even([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]

def one_in_binary_of_a_list(lst: list[int]) -> bool:
    cnt = 0
    while lst[0] != 0:
        if lst[0] % 2 == 1:
            cnt += 1
        lst[0] //= 2

    cnt_1 = 0
    for i in range(1, len(lst)):
        while lst[i] != 0:
            if lst[i] % 2 == 1:
                cnt_1 += 1
            lst[i] //= 2
        if cnt_1 != cnt:
            return False
        cnt_1 = 0

    return True


def get_longest_same_bit_counts(lst: list[int]) -> list[int]:
    """Returneaza cea mai mare subsecventa care au acelasi numar de 1 in scrierea binara

    Args:
        lst (list[int]): [o lista de numare intregi]

    Returns:
        subsecventa_max (list[int]): [cea mai lunga subsecventa are au acelasi numar de 1 in scrierea binara]
    """  
    
    subsecventa_max = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if one_in_binary_of_a_list(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = lst[i:j + 1]

    return subsecventa_max


def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([5, 8, 5, 3, 1, 3, 5, 10, 2, 12]) == [3, 5, 10]
    assert get_longest_same_bit_counts([1]) == [1]
    assert get_longest_same_bit_counts([]) == []


def is_prime(x):
    """ 
    Verifica daca un numar este prim
    """

    if x < 2:
        return False
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    return True


def if_digits_is_prime(x):
    """ 
    Verifica daca un numar ar toate cifrele prime
    """

    while x != 0:
        if not is_prime(x%10):
            return False
        x //= 10
    return True

def list_with_prime_digits(lst):
    """ 
    Verifica daca o lista are toate numerele de cifre prime
    """

    for x in lst:
        if not if_digits_is_prime(x):
            return False
    return True        

def get_longest_prime_digits(lst: list[int]) -> list[int]:
    """Functia returneaza cea mai lunga secventa a caror numere sunt formate doar din cifre prime

    Args:
        lst (list[int]): [o lista de numere intregi]

    Returns:
        list[int]: [returneaza cea mai lunga subsecventa a sirului avand numere de cifre prime]
    """
    subsecventa_max = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if list_with_prime_digits(lst[i:j + 1]) and len(lst[i:j + 1]) >= len(subsecventa_max):
                subsecventa_max = lst[i:j + 1]
    return subsecventa_max


def test_get_logest_prime_digits():
    assert get_longest_prime_digits([1, 2, 3, 4, 5, 6]) == [2, 3]
    assert get_longest_prime_digits([2, 3, 25, 75, 5]) == [2, 3, 25, 75, 5]
    assert get_longest_prime_digits([]) == []
    assert get_longest_prime_digits([1, 6, 8, 4, 6]) == []


def printMenu():
    print("1.Citire date ")
    print("2.Determina cea mai lunga secventa in care numerele au acelasi numar de 1 in scrierea binara ")
    print("3.Determina cea mai lunga secventa in care numerele sunt pare ")
    print("4.Determina cea mai lunga secventa de numere cu cifre prime ")
    print("5.Iesi")


def main():
    test_get_longest_all_even()
    test_get_longest_same_bit_counts()
    test_get_logest_prime_digits()
    list = []
    while True:
        printMenu()
        optiune = input("Alegeti o optiune: ")
        if optiune == "1":
            list = read_list()
        elif optiune == "2":
            print(get_longest_same_bit_counts(list))
        elif optiune == "3":
            print(get_longest_all_even(list))
        elif optiune == "4":
            print(get_longest_prime_digits(list))
        elif optiune == "5":
            break
        else:
            print("Optiune invalida! Reincercati ")


if __name__ == "__main__":
    main()