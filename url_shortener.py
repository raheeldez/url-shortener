import pyshorteners

# Function to shorten the URL
def shorten_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

# Get input from the user
if __name__ == "__main__":
    long_url = input("Enter the URL to shorten: ")
    short_url = shorten_url(long_url)
    print(f"Shortened URL: {short_url}")
