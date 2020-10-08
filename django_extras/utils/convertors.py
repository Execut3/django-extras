def price_beautifier(amount):
    """ Will create comma separated values for better display
    of Price values.

    for example: price_beautifier(100000) will generate '100,000'
    """
    try:
        return "{:,}".format(int(amount))
    except:
        return amount
