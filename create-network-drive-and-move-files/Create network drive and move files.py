## This script runs on windows machine
## The script creates a network drive and moves files from the local directory to the network share - once done, the network drive will be deleted
import os
import subprocess

remote_server_ip = "1.1.1.1" # The server IP where the remote share was defined
remote_share_domain = "domain" # This should be the remote server domain name or server hostname
remote_share_username = "administrator" # Username that have permission on the share
remote_share_password = "1qaz@WSX#EDC" # User password
remote_share_folder = "sysmon_ready_files" # Share name
files_to_move_path = "C:\\sysmon_events\\sysmon_ready_files\\" # The folder on the local workstation that includes the files that should move to the share
remote_share_drive_letter = "L:" # Share drive letter that will be created on the local workstation

remote_share_is_ready = subprocess.call(r'ping ' + remote_server_ip , shell=True) #If ping was successfully answered shall be 0 while unsuccessful ping answer will be 1
#print(remote_share_is_ready)
files_exists = os.listdir(files_to_move_path)   # Checks if there are files in ready folder

if remote_share_is_ready == 1:
    print("Remote share is not available")
    exit()
else:
    if not files_exists: #Check if the files_exists array include files
        print("There are no files in folder")
        exit()
    else:
        drive_exists = os.path.exists(remote_share_drive_letter) #check if remote drive letter is mapped
        if drive_exists:
            print("Moving files to remote folder and disconnecting remote drive")
            subprocess.call(r'move ' + files_to_move_path + '* ' + remote_share_drive_letter + '\\', shell=True)
            subprocess.call(r'net use ' + remote_share_drive_letter + ' /delete /y', shell=True)
            exit()
        else:
            print("creating mount to a remote network , Moving files to remote folder and disconnecting remote drive")
            subprocess.call(r'net use' + ' ' + remote_share_drive_letter + ' \\\\' + remote_server_ip + '\\' + remote_share_folder + ' ' + remote_share_password + ' /user:' + remote_share_domain + '\\' + remote_share_username + ' /persistent:no',shell=True)
            subprocess.call(r'move ' + files_to_move_path + '* ' + remote_share_drive_letter + '\\', shell=True)
            subprocess.call(r'net use ' + remote_share_drive_letter + ' /delete /y', shell=True)
            exit()

