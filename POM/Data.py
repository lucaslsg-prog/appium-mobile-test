class TestData(object):
    budget_type = "supermarket"
    budget_value = "600"
    new_budget_value = "800"
    fieldEmpty = ""
    msg_budget_value_empty= "Budget value is empty"
    msg_budget_type_empty = "Budget type is empty"
    budget_empty_list = "You don't have any budgets at the moment. Click the + (plus) button up top "
    date_result = '2/2/22 ~ '
    value_with_letter = "abcd"
    name_with_number = 1000
    invalid_name_over_limit = "Qwertyuiopasdfghjklçzxcvbnmqwet" #Should not allow insert more than 30 characters
    invalid_value_over_limit = "12345678910" #Should not allow insert more than 10 characters
    valid_max_name = "Qwertyuiopasdfghjklçzxcvbnmqwe" # max 30 characters
    valid_max_value = "1000000000" # max 10 characters


