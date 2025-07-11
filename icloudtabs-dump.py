#!/usr/bin/env python3
#
# Alfred workflow for listing iCloud tabs
#

import os
import subprocess
import shutil
from datetime import datetime
import urllib.request
import re
import getpass
import sqlite3


local_user = getpass.getuser()
cloudtabs_db = f'/Users/{local_user}/Library/Containers/com.apple.Safari/Data/Library/Safari/CloudTabs.db'

conn = sqlite3.connect(cloudtabs_db)
cursor = conn.cursor()

cursor.execute("SELECT device_uuid, device_name FROM cloud_tab_devices")
cloud_tab_devices = cursor.fetchall()

cloud_tab_devices_lookup = {
	device_uuid: device_name for device_uuid, device_name in cloud_tab_devices
}

cloud_tab_devices_uuid_list = [device_uuid for device_uuid, _ in cloud_tab_devices]

cursor.execute("SELECT device_uuid, title, url FROM cloud_tabs")
cloud_tabs = cursor.fetchall()

conn.close()

all_device_tabs = []

for device_uuid in cloud_tab_devices_uuid_list:
	lookup_name = cloud_tab_devices_lookup[device_uuid]
	device_tabs = []
	for tab in cloud_tabs:
		if tab[0] == device_uuid:
			tabinfo = {'Title': tab[1], 'URL': tab[2]}
			device_tabs.append(tabinfo)
	all_device_tabs.append([lookup_name, device_tabs])

# Output path with safe filename format
outfile = os.path.expanduser(
	f'~/Desktop/alltabs_{datetime.now().strftime("%Y-%m-%d %H.%M.%S")}.md'
)

outtext = f'''
## iCloud Tab Listing - {datetime.now().isoformat()[:19]}

Links from all devices:

'''

for device in all_device_tabs:
	outtext += f'### {device[0]}\n\n'
	for tab in device[1]:
		title = tab['Title'].replace("[", "/[").replace("]", "/]")
		url = tab['URL']
		outtext += f'* [{title}]({url})\n'
	outtext += '\n'

# Write UTF-8 encoded text
with open(outfile, 'w', encoding='utf-8') as f:
	f.write(outtext)

# Optional: open in Marked 2
# os.system(f'open -a "Marked 2" "{outfile}"')
