class TestData(object):
    
    ########## STATIC TEST DATA ################################################

    valid_name = "budget_test"
    valid_value = "1000"
    valid_max_name = "Qwertyuiopasdfghjklçzxcvbnmqwe" # max 30 characters
    valid_max_value = "1000000000" # max 10 characters

    toast_value_empty= "Budget value is empty"
    toast_name_empty = "Budget type is empty"

    invalid_name_number = "123 456" #name with number and space must be recused
    invalid_value_letter = "abc" #string with letters must be recused
    invalid_name_over_limit = "Qwertyuiopasdfghjklçzxcvbnmqwet" #Should not allow insert more than 30 characters
    invalid_value_over_limit = "12345678910" #Should not allow insert more than 10 characters

    edit_value = int(valid_value) + 100
    edit_name = f"{valid_name}_edited"


    ########## MODELS TO USING DATA FOR TEST ##################################

    valid_data_list =[
        valid_name,
        valid_value,
        valid_max_name,
        valid_max_value
    ]
    
    toast_data_list=[
        toast_name_empty,
        toast_value_empty
    ]

    invalid_data_list=[
        invalid_name_number,
        invalid_value_letter,
        invalid_name_over_limit,
        invalid_value_over_limit
    ]

    edit_date_list=[
        edit_name,
        edit_value
    ]