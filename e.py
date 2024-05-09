from psnawp_api import PSNAWP

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
