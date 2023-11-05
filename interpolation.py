def find_location(
    number: float, temperature_conversion_curve: list[list[int]]
) -> tuple[int, int] | int:
    """finds the location of a number in temperature_conversion_curve.
    For more information, read the documentation for interpolation

    :param number: the value, for which the location should be determent
    :param temperature_conversion_curve: array of arrays with the voltage to degrees curve
    :return: a tuple of the indexes from the number below and above the input, or one number if there's an exact match
    """
    for idx, val in enumerate(temperature_conversion_curve):
        if val[0] == number:
            return idx
        a = val[0] - number
        if a > 0:
            return idx - 1, idx
    raise ValueError(f"number {number} not in temperature_conversion_curve")


def get_temperature(voltage: float, temperature_conversion_curve: list[list[int]]):
    """calculates the temperature for a given voltage.
    For more information, read the documentation for interpolation

    :param voltage: the voltage for which the temperature should be calculated in V
    :param temperature_conversion_curve: array of arrays with the voltage to degrees curve
    :return: the temperature in °C
    """
    location = find_location(voltage, temperature_conversion_curve)
    if isinstance(location, int):
        # If there's an exact match in the curve, we already found the temperature, or there was an error
        return temperature_conversion_curve[location][1]

    prv, nxt = location
    prv = temperature_conversion_curve[prv]
    nxt = temperature_conversion_curve[nxt]

    x1 = prv[0]
    x = voltage
    x2 = nxt[0]
    y1 = prv[1]
    y2 = nxt[1]

    y = (x - x1) / (x2 - x1) * (y2 - y1) + y1

    return y
