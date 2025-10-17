# wrote by my self
import requests



def fetching_user_data():
    url = "https://randomuser.me/api"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching user data: ", response.status_code)
# fetching_user_data()

def print_user_data(user_data):
    if user_data:
        user_data = user_data['results'][0]
        username = user_data['name']
        # print(f"Name of user is {user_data['name']['first']} {user_data['name']['last']}.")
        print(f"Name of user is {username['first']} {username['last']}.")
        print(f"ID of user is {user_data['id']['name']}")
        print(f"Date of birth of user is '{user_data['dob']['date']}'.")
        print(f"Email of user is {user_data['email']}")
    else:
        print("Failed to retrieve data.")

def main():
    print("Fetching user data.....")
    random_user = fetching_user_data()
    print_user_data(random_user)
    


if __name__ == "__main__":
    main()




# Wrote by gemini

# import requests
# from datetime import datetime

# def fetch_random_user():
#     url = "https://randomuser.me/api"
#     response = requests.get(url)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception(f"Error fetching user data: Status code {response.status_code} - {response.text}")


# def print_user_data(user_data):
#     if user_data:
#         user_data = user_data["results"][0]

#         username = f"{user_data['name']['title']} {user_data['name']['first']} {user_data['name']['last']}"
#         user_id = user_data["id"]["name"]

#         try:
#             dob = datetime.strptime(user_data["dob"]["date"], "%Y-%m-%dT%H:%M:%S.%fZ")
#             dob_formatted = dob.strftime("%B %d, %Y")
#         except ValueError:
#             dob_formatted = "Not available"

#         email = user_data["email"]

#         print(f"Name of user is: {username}")
#         print(f"ID of user is: {user_id}")
#         print(f"Date of birth of user is: {dob_formatted}")
#         print(f"Email of user is: {email}")
#     else:
#         print("Failed to retrieve data.")


# def main():
#     print("Fetching user data...")
#     random_user = fetch_random_user()
#     print_user_data(random_user)


# if __name__ == "__main__":
#     main()




# Added some variations

# import requests


# def fetching_user_data():
#     url = "https://randomuser.me/api"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception(f"Error fetching user data: {response.status_code}")


# def print_user_data(user_data, count):
#     if user_data:
#         user_data = user_data['results'][0]
#         username = user_data['name']
        
#         # Print user information
#         print(f"\nUser {count}:")
#         print(f"Name of user: {username['first']} {username['last']}")
#         print(f"ID of user: {user_data['id']['name']}")
#         print(f"Date of Birth: {user_data['dob']['date']}")
#         print(f"Email of user: {user_data['email']}")
#     else:
#         print("Failed to retrieve data.")


# def main():
#     try:
#         user_count = int(input("Enter the number of users you want to fetch: "))
        
#         for i in range(1, user_count + 1):
#             print(f"\nFetching user data for user {i}...")
#             random_user = fetching_user_data()
#             print_user_data(random_user, i)
    
#     except ValueError:
#         print("Please enter a valid number.")
#     except Exception as e:
#         print(e)


# if __name__ == "__main__":
#     main()
