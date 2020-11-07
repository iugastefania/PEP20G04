#1
def build(a, b, c):
    def response(x):
        return a * (x ** 2) + b * x + c
    return response

functie = build(2, 4, 6)
print(functie(4))

#2
list_of_functions = []

for a, b, c in ((1, -2, 2), (2, -4, 4), (3, -6, 6)):
    list_of_functions.append(build(a, b, c))

print(list_of_functions)

#3
dict_of_results = {}

for function in list_of_functions:
    list_of_results = [function(x) for x in range(-10, 10)]
    dict_of_results.update({function : list_of_results})

print(dict_of_results)

#4
function_with_smallest_result = None
smallest_value = None
contor = 9999999

for function, values in dict_of_results.items():

    for i in values:

        if i < contor:
            contor = i
            smallest_value = i
            function_with_smallest_result = function

print(function_with_smallest_result, smallest_value)
#5
print(function_with_smallest_result(0))



