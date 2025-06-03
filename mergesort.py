import matplotlib.pyplot as plt

def assignment(new_list, new_pointer, old_list, old_pointer):
    new_list[new_pointer] = old_list[old_pointer]

def merge_sort(unsorted_list):
    if len(unsorted_list) > 1:
        middle = len(unsorted_list) // 2
        left_list = unsorted_list[:middle]
        right_list = unsorted_list[middle:]

        merge_sort(left_list)
        merge_sort(right_list)

        merge(unsorted_list, left_list, right_list)

def merge(output_list, left_list, right_list):
    left_pointer = 0
    right_pointer = 0
    target_pointer = 0

    # Solange beide Listen Elemente haben, vergleiche und füge das jeweils kleinere ein
    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] <= right_list[right_pointer]:
            assignment(new_list=output_list,
                       new_pointer=target_pointer,
                       old_list=left_list,
                       old_pointer=left_pointer)
            left_pointer += 1
        else:
            assignment(new_list=output_list,
                       new_pointer=target_pointer,
                       old_list=right_list,
                       old_pointer=right_pointer)
            right_pointer += 1

        target_pointer += 1

    # Füge verbleibende Elemente aus left_list ein
    while left_pointer < len(left_list):
        assignment(new_list=output_list,
                   new_pointer=target_pointer,
                   old_list=left_list,
                   old_pointer=left_pointer)
        left_pointer += 1
        target_pointer += 1

    # Füge verbleibende Elemente aus right_list ein
    while right_pointer < len(right_list):
        assignment(new_list=output_list,
                   new_pointer=target_pointer,
                   old_list=right_list,
                   old_pointer=right_pointer)
        right_pointer += 1
        target_pointer += 1

def plot_list(input_list):
    x = range(len(input_list))
    fig, ax = plt.subplots(figsize=(5,5))
    ax.bar(x, input_list)
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    plt.show()
    

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
plot_list(my_list)
mergeSort(my_list)
plot_list(my_list)
