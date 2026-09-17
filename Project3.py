# Project 3 - InstaGoose Profile System

# Profile Class

class Profile:
    def __init__(self, username, age, bio):
        # use to identify a specific user
        self.username = username
        
        # user chooses these properties
        self.age = age
        self.bio = bio
        
        # constant default (NOT chosen by user)
        self.followers = 0   # everyone starts with 0 followers

    # string method
    def __str__(self):
        return (
            "----- InstaGoose Profile -----\n" +
            "Username: " + self.username + "\n" +
            "Age: " + str(self.age) + "\n" +
            "Bio: " + self.bio + "\n" +
            "Followers: " + str(self.followers) + "\n" +
            "------------------------------"
        )

    # getters
    def get_username(self):
        return self.username

    def get_age(self):
        return self.age

    def get_bio(self):
        return self.bio

    def get_followers(self):
        return self.followers

    # setter ONLY for constant property
    def set_followers(self, new_count):
        self.followers = new_count



# findPerson Function

def findPerson(profileList, identifier):
    for profile in profileList:
        if profile.get_username() == identifier:
            return profile
    return None



# Main Function

def main():
    profiles = []  # list to store all profiles

    while True:
        print("Welcome to InstaGoose!")
        print("1. Add Profile")
        print("2. View Profile")
        print("3. Quit")

        choice = input("Enter choice (1, 2, or 3): ")

        # Add profile
        if choice == "1":
            username = input("Enter username: ")
            age = int(input("Enter age: "))
            bio = input("Enter bio: ")

            new_profile = Profile(username, age, bio)
            profiles.append(new_profile)

            print("Profile created successfully!")

        # View profile
        elif choice == "2":
            search_name = input("Enter username to search: ")
            result = findPerson(profiles, search_name)

            if result is not None:
                print(result)
            else:
                print("Profile not found.")

        # Quit
        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


# run program
main()