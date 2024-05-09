from psnawp_api import PSNAWP

## lvgD0cduLkvGFeXUa5BgvuB3NYovnFPm2QwB6JD7sV28C87D4CZowOFVNv1bUShy

psnawp = PSNAWP(input("ID: "))


# This is you
client = psnawp.me()
print(client.online_id)
print(client.account_id)
print(client.get_account_devices())
print(client.get_profile_legacy())
print(client.friends_list())
print(client.blocked_list())
print(client.available_to_play())
groups = client.get_groups()
print(groups)