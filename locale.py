
hello_msg = "Hello!\nIt's SystemMD Generator!"
start_msg = "For new autorun file type '1'."
enter_new_name = "Enter name of you service-file (without '.service')"
Description = "Enter description for process. (For default it will be name of service file):"
ExecStartPre = "Enter command that will be run before main process (or skip this step):"
ExecStart = "Enter main process command:"
successful_create = "Successful creating service!"
isSuccesRun = "Is process successful running? (Y/n):"
working_dir = "Enter working directory (non required but recommend for Python-scripts):"
successful_autorun = 'If above you see the "Created symlink /etc/systemd/system" means the startup has been successfully configured'

end = "--------------------------------------------------"

#Errors
error_root = "[ERROR]: You need root permissions to run this!"
error_exist = "[ERROR]: This file already exist or empty filename!"
error_execStart = "[ERROR]: You need to enter procces command"