import datetime
import requests


def get_weather(location: str):
    print(f"🌤 Calling Free Open-Meteo Weather API for {location}...")
    try:
        # 1. Geocoding
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1"
        res = requests.get(geo_url).json()
        
        if not res.get('results'):
             return {"error": "Location not found, fallback to default", "forecast": "Sunny"}

        lat = res['results'][0]['latitude']
        lon = res['results'][0]['longitude']
        
        # 2. Weather fetching
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        w_res = requests.get(weather_url).json()

        current = w_res.get('current_weather', {})
        return {
            "location": res['results'][0]['name'],
            "temperature": f"{current.get('temperature', 'Unknown')}°C",
            "windspeed": f"{current.get('windspeed', 'Unknown')} km/h",
            "source": "Open-Meteo Free API"
        }
    except Exception as e:
        print(f"[ERROR] Failed to fetch weather: {e}")
        return {"error": "Weather fetch failed", "fallback": "Sunny, 25°C"}

def get_crop_price(crop: str, region: str) -> dict:
    """Returns the market price (in INR) and trend of a specific crop in a specified region."""
    print(f"📊 Fetching Crop Price Data for {crop} in {region}...")

    # Dictionary acting as a mock API database
    prices = {
        "wheat": {"current_price": 2200, "last_week_price": 2150, "trend": "Increasing", "percentage_change": "2.3%"},
        "rice": {"current_price": 3100, "last_week_price": 3150, "trend": "Decreasing", "percentage_change": "-1.5%"},
        "corn": {"current_price": 1850, "last_week_price": 1850, "trend": "Stable", "percentage_change": "0.0%"},
        "sugarcane": {"current_price": 340, "last_week_price": 330, "trend": "Increasing", "percentage_change": "3.0%"}
    }
    
    crop_key = crop.lower()
    if crop_key not in prices:
        # Fallback dynamic calculation for unsupported crops
        base = len(crop) * 200
        return {
             "crop": crop, "region": region, "current_price": base, "last_week_price": base - 50, 
             "trend": "Increasing", "percentage_change": "+2%"
        }

    data = prices[crop_key]
    data["crop"] = crop
    data["region"] = region
    return data

def get_schemes(crop: str) -> dict:
    """Returns the government scheme data including Minimum Support Price (MSP) for a given crop."""
    print(f"🏛 Checking Government Schemes for {crop}...")

    schemes = {
        "wheat": {"minimum_support_price": 2275, "storage_subsidy": "20% subsidy for 30 days", "eligibility": "Small and marginal farmers"},
        "rice": {"minimum_support_price": 2183, "storage_subsidy": "10% subsidy for 60 days", "eligibility": "All farmers in registered areas"},
        "corn": {"minimum_support_price": 2090, "storage_subsidy": "None", "eligibility": "Drought-prone area farmers"},
        "sugarcane": {"minimum_support_price": 315, "storage_subsidy": "Transport subsidy available", "eligibility": "Cooperative members"}
    }
    
    crop_key = crop.lower()
    return schemes.get(crop_key, {
        "minimum_support_price": "Not officially set",
        "storage_subsidy": "General godown access",
        "eligibility": "Anyone with farmer ID"
    })


if __name__ == "__main__":
    print(get_weather("Delhi"))
    print()
    print(get_crop_price("Wheat", "Punjab"))
    print()
    print(get_schemes("Rice"))
