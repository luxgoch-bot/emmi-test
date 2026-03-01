# Swiss VAT Calculator
# VAT Rate: 8.1% (standard Swiss VAT rate)

VAT_RATE = 0.081  # Swiss standard VAT rate


def calculate_vat(amount: float) -> dict:
    """
    Calculate Swiss VAT for a given net amount.

    Args:
        amount (float): The net amount in CHF.

    Returns:
        dict: A dictionary containing net, vat_rate, vat_amount, and gross.
    """
    vat_amount = amount * VAT_RATE
    gross = amount + vat_amount

    return {
        "net": round(amount, 2),
        "vat_rate": VAT_RATE,
        "vat_amount": round(vat_amount, 2),
        "gross": round(gross, 2),
    }


def add_vat(amount: float) -> float:
    """
    Add VAT to a given net amount and return the gross amount.

    Args:
        amount (float): The net amount in CHF.

    Returns:
        float: The gross amount including VAT.
    """
    return round(amount * (1 + VAT_RATE), 2)


def extract_vat(gross: float) -> float:
    """
    Extract the VAT component from a gross (VAT-inclusive) amount.

    Args:
        gross (float): The gross amount in CHF including VAT.

    Returns:
        float: The VAT amount extracted from the gross.
    """
    return round(gross - (gross / (1 + VAT_RATE)), 2)


if __name__ == "__main__":
    # Example 1: Full VAT breakdown for CHF 100 net
    net_amount = 100.00
    result = calculate_vat(net_amount)
    print(f"Net Amount:   CHF {result['net']:.2f}")
    print(f"VAT Rate:     {result['vat_rate'] * 100}%")
    print(f"VAT Amount:   CHF {result['vat_amount']:.2f}")
    print(f"Gross Amount: CHF {result['gross']:.2f}")

    # Example 2: Add VAT to CHF 200
    print(f"\nCHF 200.00 + VAT = CHF {add_vat(200.00):.2f}")

    # Example 3: Extract VAT from a gross amount
    print(f"VAT in CHF 108.10 gross = CHF {extract_vat(108.10):.2f}")
