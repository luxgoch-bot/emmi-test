def chf_to_eur(chf: float) -> float:
    """
    Convert CHF to EUR using a fixed rate of 1.05.

    Args:
        chf (float): Amount in Swiss Francs

    Returns:
        float: Amount in Euros

    Example:
        >>> chf_to_eur(100)
        95.23809523809523
    """
    return chf / 1.05


# Test cases
assert abs(chf_to_eur(100) - 95.23809523809523) < 0.001
assert abs(chf_to_eur(0) - 0.0) < 0.001
assert abs(chf_to_eur(50) - 47.61904761904762) < 0.001
