def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    a=len(list1)
    a=int(a)
    if sum(list1)==(list1[0])*a :
        return True
    else:
        return False
print(main([1,0,0,0,0]))