class TestData(object):
    msg_input_required_empty = "Field can't be empty."
    msg_input_over_limit = "You can't be so rich."
    valid_price = "250"
    max_valid_characters_price = "1234567891011" #should allow 13 characters
    over_limit_characters_price = "12345678912345" #should not allow more than 13 characters
    invalid_price_with_letter = "123abc"
    invalid_category_with_number = "123"
    valid_title = "Test_Title"
    valid_category = "Test_Category"
    title_edited = "Test_Title_Edited"
    total_after_delete = "+ 0 NON"