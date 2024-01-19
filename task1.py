import requests

# Function to fetch JSON data from a URL
def fetch_json_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Function to display data with Title, Price ordered by descending popularity
def display_data(data):
    if data is not None and 'products' in data:
        products = data['products']
        sorted_data = sorted(products.values(), key=lambda x: int(x.get('popularity', 0)), reverse=True)

        print(f"{'Title':<30}{'Price':<10}{'Popularity':<10}")
        print("-" * 50)

        for item in sorted_data:
            title = item.get('title', 'N/A')
            price = item.get('price', 'N/A')
            popularity = item.get('popularity', 'N/A')

            print(f"{title:<30}{price:<10}{popularity:<10}")

json_file_url = 'https://s3.amazonaws.com/open-to-cors/assignment.json'
data = fetch_json_data(json_file_url)

if data:
    display_data(data)
