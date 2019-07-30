import os
import locale
import sys

working_dir = "/etc/systemd/system/"

def check_root():
    if not os.access(working_dir, 2):
        print(locale.error_root)
        sys.exit(1)

def main():
    print(locale.hello_msg)
    while True:
        if ( str( input() ) == '1' ):
            createNewService()
    #handle = open("/etc/systemd/system/test.service", "w")
    #handle.write("This is a test!")
    #handle.close()

def createNewService():
    print(locale.enter_new_name)
    file_name = str(input()) + ".service"
    if os.path.isfile(working_dir + file_name):
        print(locale.error_exist)
        return False
    print(locale.Description)
    description = str( input() )
    if description == None:
        description = file_name
    print(locale.ExecStartPre)
    execStartPre = str( input() )
    print(locale.ExecStart)
    execStart = str( input() )
    constructor = open("service_constructor.conf", "r")
    constructor.replace("%Descriptrion%", description)
    constructor.replace("%ExecStartPre%", execStartPre)
    constructor.replace("%ExecStart%", execStart)
    write_file = working_dir + file_name
    service_file = open(write_file, "w")
    service_file.write(constructor)
    service_file.close()
    print(local.successful_create)
    os.system("sudo systemctl start %s", file_name) #TODO CheckThis
    print(local.isSuccesRun)
    
    return True

if __name__ == "__main__":
    check_root()
    main()
