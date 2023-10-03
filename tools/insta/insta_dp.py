import instaloader

try:
    ig = instaloader.Instaloader()
    dp = input("Enter instagram username: ")
    ig.download_profile(dp,profile_pic_only=True)
    print("profile pic of {} is downloaded successfully".format(dp))

except instaloader.exceptions.ProfileNotExistsException:
    print(f"Profile {dp} does not exist.")
except instaloader.exceptions.QueryReturnedNotFoundException:
    print(f"No user with username {dp}.")
except instaloader.exceptions.LoginRequiredException:
    print("Authentication required. Please provide login credentials.")
except instaloader.exceptions.TooManyRequestsException:
    print("Too many requests. Please wait before trying again.")
except Exception as e:
    print(f"An error occurred: {e}")