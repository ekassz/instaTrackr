from bs4 import BeautifulSoup

# load followers
with open('followers_and_following/followers_1.html', 'r', encoding='utf-8') as f:
    followers_data = f.read()
parse_followers = BeautifulSoup(followers_data, 'html.parser')

# load who I'm following
with open("followers_and_following/following.html", 'r', encoding='utf-8') as f:
    following_data = f.read()
parse_following = BeautifulSoup(following_data, 'html.parser')

#Extract usernames from both lists
followers = set([tag.text for tag in parse_followers.find_all('a')])
following = set([tag.text for tag in parse_following.find_all('a')])

#Calculate people who don't follow back
non_followers = following - followers

#Print list
print("People who don't follow you: ")
for user in non_followers:
    print(user)