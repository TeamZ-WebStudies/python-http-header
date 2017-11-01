import sys
import requests


def print_header(headline):
    """
    print String into a # rectangle
    :param headline: String witch should be include into a # boarder
    """

    horizontal_line = ('{:#<{width}}'.format("", width='30'))
    print(horizontal_line)
    print('#{:^{width}}#'.format(headline, width='28'))
    print(horizontal_line)
    print()


def print_dict_as_table(dict, header_first="http header", header_second="value"):
    """
    print a dict as a table
    :param header_second: secound header text for the table
    :param header_first: first header text for the table
    :param dict: dict witch should be printed into a table
    """

    horizontal_line = ('+{:-<32}+{:-<122}+'.format("", ""))
    print(horizontal_line)

    print('| {:<30} | {:<120} |'.format(header_first, header_second))
    print(horizontal_line)

    for key, value in dict.items():
        print('| {:<30} | {:<120} |'.format(key, value))

    print(horizontal_line)
    print()


# print website url
print("Target Site: %s" % sys.argv[1])

if len(sys.argv) <= 2:
    # do http request
    current_request = requests.get(sys.argv[1])
else:
    # do http request with custom header
    headers = {sys.argv[2]: sys.argv[3]}
    current_request = requests.get(sys.argv[1], headers=headers)

# print http request
print_header("http request content")
print_dict_as_table(current_request.request.headers)

# print http headers
print_header("http headers content")
print_dict_as_table(current_request.headers)
