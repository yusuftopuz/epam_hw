def check_power_of_2(a: int) -> bool:
    """Check if a is power of 2"""
    if a == 0:
        return False
    return not (bool(a & (a - 1)))


if __name__ == "__main__":
    print(check_power_of_2(0))
