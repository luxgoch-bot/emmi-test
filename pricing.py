def calculate_price(distance_km: float) -> dict:
    """
    Calculate the transfer price for a LuxGo ride based on driving distance.

    Args:
        distance_km (float): The driving distance in kilometers.

    Returns:
        dict: A dictionary containing:
            - distance_km (float): The input distance in kilometers.
            - base_rate (float): The fixed base rate in CHF.
            - per_km_rate (float): The rate per kilometer in CHF.
            - per_km_charge (float): The total charge for the distance in CHF.
            - total_chf (float): The total price in CHF, rounded to 2 decimal places.
    """
    base_rate = 50.0
    per_km_rate = 3.0
    per_km_charge = distance_km * per_km_rate
    total_chf = round(base_rate + per_km_charge, 2)

    return {
        "distance_km": distance_km,
        "base_rate": base_rate,
        "per_km_rate": per_km_rate,
        "per_km_charge": per_km_charge,
        "total_chf": total_chf,
    }


if __name__ == "__main__":
    examples = [10, 25, 50]
    for km in examples:
        result = calculate_price(km)
        print(f"{km} km → CHF {result['total_chf']:.2f}")
