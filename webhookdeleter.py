import requests

ascii_art = """
  _______ _    _ ______ ______ ________  __  ____   ____  _   _ 
 |__   __| |  | |  ____|  ____|___  /  \/  |/ __ \ / __ \| \ | |
    | |  | |__| | |__  | |__     / /| \  / | |  | | |  | |  \| |
    | |  |  __  |  __| |  __|   / / | |\/| | |  | | |  | | . ` |
    | |  | |  | | |____| |     / /__| |  | | |__| | |__| | |\  |
    |_|  |_|  |_|______|_|    /_____|_|  |_|\____/ \____/|_| \_|
                                                                
                                                                
"""

print(ascii_art)

webhook_url = input("Enter the webhook URL: ")

response = requests.delete(webhook_url)

if response.status_code == 204:
    print("Webhook deleted successfully.")
else:
    print(f"Failed to delete webhook. Status code: {response.status_code}")
