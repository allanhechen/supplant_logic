# this file is used for constants values
import pygsheets

# variables for where to split text into phrases
split = [", ", ". ", " and ", " but "]

# import glossary from excel sheet
# TODO: somehow get the file directive after "service_file" to this current opened file
sheets = pygsheets.authorize(service_file="glossary_key.json").open_by_key("1hsG7UiSjyaIEWVHGd2dHRJIkSrRBeO4IDpQGqp19D9o")

# test
sheets[0].update_value("test")
