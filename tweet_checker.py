
max_tweets_chars = 140
print("**************************************************")
tweet = input("ENTER YOUR POTENTIAL TWEET BELOW:")
char_count = len(tweet)

if char_count < max_tweets_chars:
    print(f"That {char_count} character tweet will work")
else:
    print(f"That {char_count} character tweet is {char_count - max_tweets_chars} characters long. Therefore it will not work")

print("**************************************************")