import os
import locale

working_dir = "/etc/systemd/system/"

def check_root():
    try: 
        os.rename('/etc/foo', '/etc/bar')
    except IOError as e:
        if (e[0] == errno.EPERM): 
            print(locale.error_root)
            sys.exit(1) 
def main():
    print(locale.hello_msg)
    if input() == '1':
        createNewService()
    #handle = open("/etc/systemd/system/test.service", "w")
    #handle.write("This is a test!")
    #handle.close()

def createNewService():
    print(locale.enter_new_name)
    file_name = str(input()) + ".service"
    if not os.path.isfile(working_dir + file_name):
        print(locale.error_exist)
        return False
    print("Succeful!")

def test():
    ans = os.access(working_dir, 2)
    print(ans)

if __name__ == "__main__":
    #check_root()
    test()
    main()