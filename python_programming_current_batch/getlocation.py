import requests

def get_location_using_locationiq():
    # Your LocationIQ API key
    api_key = 'AIzaSyD8xOstoZNWl9wfZ-eWF-7mGx5EzdKLseY'
    
    # Get current IP-based location
    url = f"https://us1.locationiq.com/v1/ip?token={api_key}"
    
    response = requests.get(url)
    location_data = response.json()

    return location_data

location_info = get_location_using_locationiq()
print(location_info)
