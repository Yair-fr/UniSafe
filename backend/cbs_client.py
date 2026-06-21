import requests

def get_latest_cpi_multiplier() -> float:
    """
    Queries the official Israel Central Bureau of Statistics API for the latest
    Consumer Price Index (מדד מחירים לצרכן) relative to our baseline index year (2024).
    """
    # Official Israel Gov Data Portal / CBS API Endpoint
    url = "https://api.cbs.gov.il/index/data/price/cpi?format=json" 
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            # Extract the latest index value
            # API structure: data['index_values'][0]['value']
            latest_value = float(data["index_values"][0]["value"])
            baseline_2024_value = 100.0 # Baseline normalization index
            
            multiplier = latest_value / baseline_2024_value
            return round(multiplier, 2)
        else:
            print(f"CBS API returned status code {response.status_code}. Using fallback multiplier.")
            return 1.05
    except Exception as e:
        print(f"CBS API connection failed: {e}. Using fallback multiplier.")
        return 1.05

if __name__ == "__main__":
    print(f"Testing CBS CPI Client. Multiplier: {get_latest_cpi_multiplier()}")
