def readDictionary(filename, separator=":"):
    """Creates a dictionary by reading key-value pairs
    from the specified file in which the division between
    the key and the values is marked by specified separator,
    which defaults to a colon. The function discards any leading
    and trailing whitespaces from both the key and the value

    Args:
        filename ([file]): [file containing the key-value pairs]
        separator (str, optional): [what separtes the key from values]. Defaults to ":".
    """

    # Create empty dictionary
    my_dictionary = {}
    with open(filename) as f:
        for line in f:
            index = f.find(separator)
            key = line[:index].strip()
            value = line[index + len(separator):].strip()
            my_dictionary[key] = value
        return my_dictionary

        