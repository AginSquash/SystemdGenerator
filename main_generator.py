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

def createNewService():
    print(locale.enter_new_name)
    file_name = str(input()) + ".service"
    if os.path.isfile(working_dir + file_name):
        print(locale.error_exist)
        return False

    print(locale.Description)
    description = str( input() )
    if description == "":
        description = file_name
    print(locale.ExecStart)
    execStart = str( input() )
    if execStart == "":
        print(locale.error_execStart)
        return False

    constructor = open("service_constructor.conf", "r")
    constr_work = str(constructor.read())
    constr_work = constr_work.replace("%Description%", description)
    constr_work = constr_work.replace("%ExecStart%", execStart)

    write_file = working_dir + file_name
    service_file = open(write_file, "w")
    service_file.write(constr_work)
    service_file.close()
    print(locale.successful_create)

    os.system("sudo systemctl start " + file_name)
    print(locale.isSuccesRun)
    isOk = str( input() ).lower()
    if isOk == "y":
        os.system("sudo systemctl enable " + file_name)
    return True

if __name__ == "__main__":
    check_root()
    main()
