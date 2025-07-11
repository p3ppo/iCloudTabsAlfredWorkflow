# iCloudTabs AlfredWorkflow

This workflow retrieves iCloud tabs from the local `CloudTabs.db` database for all connected iCloud devices and exports them to a Markdown file on the Desktop. The file is named with a date and time stamp for easy identification.

Usage

1. After installing, configure `File Path` and `File Name` if needed. Defaults to `~/Desktop/` and `alltabs`. E.g file will be saved as `~/Desktop/alltabs_2025-07-11 15.12.10.md`.
1. Trigger the workflow by typing `tabs icloud dump` in Alfred.
1. The workflow will create a Markdown file containing the tabs from all devices.
