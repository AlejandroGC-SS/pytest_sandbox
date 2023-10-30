import requests
database = {
  1: "Alice",
  2: "Bob",
  3: "Charlie",
}
base_url = 'jsonplaceholder.typicode.com'

def get_user_by_id(user_id):
  return database.get(user_id)


def get_users():
  endpoint = base_url + '/users'
  response = requests.get(endpoint)
  if response.status_code == 200:
    return response.json()
  
  raise requests.HTTPError