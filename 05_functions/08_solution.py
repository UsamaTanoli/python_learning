def kw_argument(**kwargs):
    result_string = ""
    for key, value in kwargs.items():
        result_string += f"{key} : {value}\n"
    return result_string

    


result = kw_argument(name="Super Man", power="Laser")
print(result)

result2 = kw_argument(name="Usama Abbasi", power="Good IQ", do_use= "Some Time")
print(result2)