import requests


def get_weather(city):
    try:
        url = f'https://wttr.in/{city}?F2'
        response = requests.get(url)
        # Print the weather information
        if response.status_code == 200:
            print(response.text)
        else:
            print(f"Unable to retrieve weather information for {city}.")
    except Exception as e:
        print(f"Error", e)


# Example: Get weather for New York
data = input("Please enter location: ")
get_weather(data)
