## This script runs on windows machine
## The script creates a network drive and moves files from the local directory to the network share - once done, the network drive will be deleted
import logging
from logging.handlers import RotatingFileHandler

## Log parameters##
logFile = 'C:\\sysmon_events\\sysmon-python-log.log'
log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024,backupCount=2, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)
app_log = logging.getLogger('root')
app_log.setLevel(logging.INFO)
app_log.addHandler(my_handler)

remote_server_ip = "1.1.1.1" # The server IP where the remote share was defined
remote_share_domain = "domain" # This should be the remote server domain name or server hostname
remote_share_username = "administrator" # Username that have permission on the share
remote_share_password = "1qaz@WSX#EDC" # User password
remote_share_folder = "sysmon_ready_files" # Share name
files_to_move_path = "C:\\sysmon_events\\sysmon_ready_files\\" # The folder on the local workstation that includes the files that should move to the share
remote_share_drive_letter = "L:" # Share drive letter that will be created on the local workstation

app_log.info("Script is starting")
remote_share_is_ready = subprocess.call(r'ping ' + remote_server_ip , shell=True) #If ping was successfully answered shall be 0 while unsuccessful ping answer will be 1
#print(remote_share_is_ready)
files = os.listdir(files_to_move_path)   # Checks if there are files in ready folder

if remote_share_is_ready == 1:
    app_log.error("Remote share is not available - Script will exit")
    exit()
else:
    if not files: #Check if the files_exists array include files
        #print("There are no files in folder")
        app_log.info("There are no files in ready folder - Script will exit")
        exit()
    else:
        drive_exists = os.path.exists(remote_share_drive_letter) #check if remote drive letter is mapped
        if not drive_exists:
            network_drive_creation_status = subprocess.call(r'net use' + ' ' + remote_share_drive_letter + ' \\\\' + remote_share_ip + '\\' + remote_share_folder + ' ' + remote_share_password + ' /user:' + remote_share_domain + '\\' + remote_share_username + ' /persistent:no',shell=True)
            if network_drive_creation_status == 0:
                app_log.info("Network drive was created successfully")
            else:
                app_log.info("Failed to create Network drive ; check connectivity - Process will abort")
                exit()
        app_log.info("Start moving files")
        for file in files:
            subprocess.call(r'move ' + files_to_move_path + file + ' ' + remote_share_drive_letter + '\\', shell=True)
            app_log.info("Moving file: " + file)
        network_drive_deletion_status = subprocess.call(r'net use ' + remote_share_drive_letter + ' /delete /y', shell=True)
        if network_drive_deletion_status == 0:
            app_log.info("Network drive was delete successfully")
        else:
            app_log.info("Failed to delete Network drive ; Process will abort")
            exit()
        app_log.info("Script exit successfully")
        exit()
