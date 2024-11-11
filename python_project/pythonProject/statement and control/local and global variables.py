age = 28 # global variable can be used anywhere the scopw of this VARIABLE IS IT CAN BE USED INSIDE AND OUTSIDE THE FUNCTION

def print_my_name():
    first_name = "abuzar" #local space the scope of this varj
    lastname = "khan"
    full_name = first_name + lastname
    print(f"my name is {full_name}and age is {age}")
print_my_name()
print(age)

def calculate_sq_list(list_nums):#[1,2,3,4] [1,4,9,16]
    sq_list = []
    for num in list_nums:
        sq_list.append(num ** 2)
    return sq_list #[1,4,9,16] #return in list value
def calculate_add_2(sq_list): #[1,4,9,16]
    added_list = []
    for num in sq_list:
        added_list.append(num + 2)
    print(added_list) #[3,6,11,18]

list_squared = calculate_sq_list([1,2,3,4]) #[1,4,9,16]
calculate_add_2(list_squared) #passed returned value to another function

def calculate_sq_num(a,b,c):
    sq_a = a ** 2
    sq_b = b ** 2
    sq_c = c ** 2
    return sq_a,sq_b,sq_c #return mutiple var/vslues from a function
sq_val_a, sq_val_b, sq_val_c = calculate_sq_num(1,2,3)
print(sq_val_a, sq_val_b, sq_val_c)

def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
bool_val = check_even(5)
print(bool_val)

#default parameters/arguments

def calculate_sum_numbers(a,b,c,d,e=0):
    return a + b + c + d + e
sum_vars = calculate_sum_numbers(2,3,4,5,10)
print(sum_vars)


def build_dictionary(dict = {}):
    dict['a'] = 1
    dict['b'] = 2
    dict['c'] = 3
    return dict

returnd_dict = build_dictionary({'d' : 4, 'e' :5})
print(returnd_dict)


#You have to write a function that takes a dictionary as an input parameter
#a new dictionary where the key is the key from given dictionary,
# the value is value if its a string, or if its int or float, the value is value + 2

{"a": 1, "b": 2, "c": 3.5, "d": "mateen"} #Given input dict
{"a": 3, "b": 4, "c": 5.5, "d": "mateen"} #outputdictionary


def modify_dict(input_dict):
    output_dict = {}

    for key, value in input_dict.items():
        if isinstance(value, (int, float)):
            # Increment numerical values by 2
            output_dict[key] = value + 2
        else:
            # Keep string values unchanged
            output_dict[key] = value

    return output_dict


# Example usage
input_dict = {"a": 1, "b": 2, "c": 3.5, "d": "mateen"}
output_dict = modify_dict(input_dict)
print(output_dict)
