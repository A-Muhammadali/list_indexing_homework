def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    k=[]
    a=[True]
    b=[False]
    if list1[0]==1:
        k=k+a
    else:
        k=k+b
    if list1[1]==1:
        k=k+a
    else:
        k=k+b
    if list1[2]==1:
        k=k+a
    else:
        k=k+b 
    if list1[3]==1:
        k=k+a
    else:
        k=k+b 
    if list1[4]==1:
        k=k+a
    else:
        k=k+b 
    
    return k
print(main([1,0,0,0,0]))