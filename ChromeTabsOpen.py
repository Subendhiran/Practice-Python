import os

def open_chrome_tabs(profile_name, num_tabs):
    url = "https://www.google.com"
    for i in range(num_tabs):
        os.system(f"start chrome --profile-directory=\"{profile_name}\" {url}")


open_chrome_tabs("Third", 10)