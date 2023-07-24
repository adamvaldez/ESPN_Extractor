""" Handy reusable functions for project """


def format_data(datas, delimiter) -> str:
    """ Format data list into delimited string """
    output = ''
    # Build output
    for data in datas:
        output += f'{data}{delimiter}'
    # Removing trailing seperator
    return output[:-len(delimiter)]


def clean_name(name) -> str:
    """ Clean name string that comes from espn_api """
    return name.replace("'", "")
