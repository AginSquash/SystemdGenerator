import os
import locale

working_dir = "/etc/systemd/system/"

def check_root():
    if not os.access(working_dir, 2):
        print(locale.error_root)
        sys.exit(1)

def main():
    print(locale.hello_msg)
    for True:
        if input() == '1':
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
    print("Succeful!")

if __name__ == "__main__":
    check_root()
    main()