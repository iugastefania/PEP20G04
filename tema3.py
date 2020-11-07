#1
def ordered_ints(list_of_objects: list):
    newlist = []

    for i in range(0, len(list_of_objects)):
        if type(list_of_objects[i]) == int:
            newlist.append(list_of_objects[i])

        elif type(list_of_objects[i]) == str:
            newlist.append(int(list_of_objects[i]))

        elif list_of_objects[i] == True:
            newlist.append(1)

        else: # SAU elif list_of_objects[i] == False or list_of_objects[i] == () or list_of_objects[i] == []:
            newlist.append(0)
    return sorted(newlist, reverse=True)

l = [1, True, '123', False, 6, ()]
print(ordered_ints(l))

#2
def sum_of_square(n: int):
    if n >= 1:

        if n == 1:
            return 1
        return n ** 2 + sum_of_square(n-1)

    else:
        return 'n prea mic'

print(sum_of_square(10))

#3
def factorial_of_squares(n: int):
    if n >= 1:

        if n == 1:
            return 1
        return (n ** 2) * factorial_of_squares(n-1)

    else:
        return 'n prea mic'

print(factorial_of_squares(5))

#4
def process_text(text: str):
    m=len(text)
    text2 = ''

    for i in range(0,m):

        if text[i] == ' ':
            k = i
            break

    text1 = text[0:k].upper()

    for i in range(k+1, m):

        if text[i].islower():
            text2 = text2 + text[i]

        else:
            text2 = text2 + '_'

    return (text1, text2)

print(process_text('1234567a Text to te5t'))

