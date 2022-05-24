def return_binary_result(value_to_evaluate, value_true:str = "", value_false:str = "")->str:
    return value_true if value_to_evaluate else value_false