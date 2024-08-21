import requests

class UserAPI:
    def __init__(self):
        self.api_url = "https://jsonplaceholder.typicode.com/users"

    def list_users(self):
        """Retrieve a list of users."""
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    
    def get_user(self, user_id):
        """Retrieve a single user by ID."""
        response = requests.get(f"{self.api_url}/{user_id}")
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
        else:
            response.raise_for_status()

    def delete_user(self, user_id):
        """Delete a user by ID."""
        response = requests.delete(f"{self.api_url}/{user_id}")
        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            return False
        else:
            response.raise_for_status()

    def create_user(self, user_data):
        """Create a new user."""
        response = requests.post(self.api_url, json=user_data)
        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()

    def update_user(self, user_id, user_data):
        """Update an existing user by ID."""
        response = requests.patch(f"{self.api_url}/{user_id}", json=user_data)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
        else:
            response.raise_for_status()
    