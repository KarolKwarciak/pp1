
facebook = input("Do you have a Facebook account? (True/False): ").lower() == 'true'
twitter = input("Do you have a Twitter account? (True/False): ").lower() == 'true'
instagram = input("Do you have an Instagram account? (True/False): ").lower() == 'true'

if facebook + twitter + instagram >= 2:
    print("A person can be a good influencer!")
else:
    print("A person cannot be a good influencer.")
