def average_lists(list1, list2):
    """
    This function takes two lists and returns the average of them.
    :param list1: a list
    :param list2: a list
    :return: the average
    """
    for num in list2:
        list1.append(num)
    sum = 0
    amount = 0
    for number in list1:
        sum += number
        amount += 1
        average = sum / amount
    print("the average is " + str(average))

def main():
    list1 = [1, 5, 8]
    list2 = [7, 9 ,4]
    average_lists(list1, list2)

if __name__ == "__main__":
    main()
    