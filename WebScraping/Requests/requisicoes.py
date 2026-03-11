import requests

response = requests.get('https://automatetheboringstuff.com/3e/chapter13.html')

print(f"Status code: {response.status_code}")
print(" Header ")
print(response.headers)

print("\n Content ")
print(response.content)









