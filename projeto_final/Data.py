class TestData(object):
    msg_input_required_empty = "Field can't be empty."
    valid_price = "250"
    max_valid_characters_price = "1234567891011" #should allow 13 characters
    over_limit_characters_price = "12345678910111" #should not allow 14 characters
    invalid_price_with_letter = "123abc"

    valid_title = "Test_Title"
    valid_category = "Test_Category"