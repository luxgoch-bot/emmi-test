import requests
from urllib.parse import quote_plus

def calculate_driving_distance(address1, address2):
    """
    Calculate driving distance between two addresses in Switzerland.
    
    Args:
        address1 (str): The starting address string.
        address2 (str): The ending address string.
        
    Returns:
        dict: A dictionary containing 'distance_km' and 'duration_min' keys.
              
    Raises:
        ValueError: If geocoding or routing fails.
    """
    
    def geo_code(address):
        """Geocode address using Nominatim API and return (lat, lon)."""
        # Added countrycodes=ch to restrict results to Switzerland, and limit=1 for top result
        url = f"https://nominatim.openstreetmap.org/search.php?q={quote_plus(address)}&format=json&countrycodes=ch&limit=1"
        headers = {"User-Agent": "LuxGo-Emmi/1.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        json_response = response.json()
        if not json_response:
            raise ValueError(f"Address not found: {address}")
        lat = float(json_response[0]["lat"])
        lon = float(json_response[0]["lon"])
        # Print resolved address and coordinates for verification
        print(f"Resolved '{address}' to: {json_response[0]['display_name']} ({lat}, {lon})")
        return (lat, lon)

    def get_route_distance(lat_lon1, lat_lon2):
        """Get driving distance and duration via OSRM."""
        url = (
            f"http://router.project-osrm.org/route/v1/driving/"
            f"{lat_lon1[1]},{lat_lon1[0]};{lat_lon2[1]},{lat_lon2[0]}"
            f"?overview=false"
        )
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        result_json = response.json()
        if result_json.get("code") != "Ok":
            raise ValueError(f"OSRM routing failed: {result_json.get('message', 'Unknown error')}")
        
        # Distance in meters → km; duration in seconds → minutes
        distance_km = round(result_json['routes'][0]['distance'] / 1000.0, 2)
        duration_min = round(result_json['routes'][0]['duration'] / 60.0, 2)
        return {'distance_km': distance_km, 'duration_min': duration_min}

    coords1 = geo_code(address1)
    coords2 = geo_code(address2)
    return get_route_distance(coords1, coords2)


# Example usage - Winterthur to Zürich should be ~30km
if __name__ == "__main__":
    result = calculate_driving_distance(
        "Bahnhofstrasse 1, Winterthur",
        "Birmensdorferstrasse 507, Zürich"
    )
    print(f"Distance: {result['distance_km']} km")
    print(f"Duration: {result['duration_min']} minutes")
