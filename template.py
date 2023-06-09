# imports

# Declare constants and global variables here. 
# Might want to declare a unique token to be used for output file names


# A good practice is to declare your endpoint elements if static, 
# or declare the variables to be populated from config files.
# - protocol: http || https
# - host: This is the domain name, like google.com
# - path: This is the url path that comes after the host, like /api/login
# - params: The parameters required by the endpoint, they can be query, header, formData types
# - body: If the endpoint required a request body, declare it. This is usually json format
# - verb: What kind of operation it is (get,post,put,delete,etc)


# Another good practice is to create a session connection that you will reuse for all subsequent requests

# Send the request and save the response value in a variable

# Verify the response code and handle success/failed requests

# Decide if you want to split the response content into relevant data subsets or keep as whole
# Format the response content and save to a file in an easy to read manner for later use

# Have a coffee, you are done


# Design:
#######################################################################################
#
# +========================+
# | Configure the endpoint | 
# +========================+
#             |
#             |
#    +==================+                _
#    | Send the request |                 |
#    +==================+                 |
#             |                           |
#    +==================+                 |
#    |   Process data   |                 | This can be looped over if you need 
#    +==================+                 | multiple requests for the same endpoint
#             |                           |
#    +==================+                 |
#    |    Save data     |                 |
#    +==================+                _
#
#######################################################################################