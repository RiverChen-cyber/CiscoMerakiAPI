import requests
import meraki

#https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid

#obtained from Meraki dashboard
API_KEY = " "


dashboard = meraki.DashboardAPI(API_KEY)
# get organization_id and network_id
# response =  dashboard.organizations.getOrganizations()

# Input your organization_id and network_id to manipulate the network settings
organization_id = ''
network_id = ''

#Input the desired name and password for SSID
new_ssid_name = 'Change'
new_psk = 'changed'


# list all ssids
# response = dashboard.wireless.getNetworkWirelessSsids(
#     network_id
# )


# print(response)

#change psk for ssid 7 
number = '7'

#HTTP POST
#change SSID name and psk
response = dashboard.wireless.updateNetworkWirelessSsid(
   network_id, number,
   name=new_ssid_name,
   enabled=True,
   psk=new_psk
)


print(response)


