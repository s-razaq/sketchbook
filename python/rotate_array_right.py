__author__ = 'Saqib Razaq'


'''
Given an array of n elements, write an algorithm to rotate it right by k
element without using any other array.
'''


def rotate_right(my_list, k=1):
    reverse(my_list, 0, len(my_list)-1)
    reverse(my_list,0, k-1)
    reverse(my_list, k, len(my_list)-1)


def reverse(my_list, begin, end):
    while begin < end:
        swap(my_list, begin, end)
        begin += 1
        end -= 1


def swap(my_list, pos1, pos2):
    my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1]


'''
Given an array of n elements, write an algorithm to rotate it right by k
element using temp array.
'''


def rotate(my_list, k=1):
    rotated_list = list()
    length = len(my_list)
    for i in xrange(length-k,length):
        rotated_list.append(my_list[i])
    for i in xrange(length-k):
        rotated_list.append(my_list[i])
    return rotated_list


def main():
    my_array = [1,2,3,4,5,6,7,8,9,10]
    rotate_right(my_array, 3)
    print my_array
    my_array = [1,2,3,4,5,6,7,8,9,10]
    my_array = rotate(my_array, 3)
    print my_array


if __name__ == '__main__':
    main()