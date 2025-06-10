import subprocess
import platform

def ssh_cmd(os_type):
    try:
        if os_type == "windows":
            print("Detected Windows OS. Attempting to terminate all Python processes...")
            subprocess.Popen('taskkill /IM /F python.exe', shell=True)
            print("Command executed: taskkill /IM /F python.exe")
        else:
            print("Detected Unix-like OS. Attempting to terminate all Python processes...")
            subprocess.Popen('killall python', shell=True)
            print("Command executed: killall python")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Determine the operating system type
    os_type = platform.system().lower()
    print(f"Operating system detected: {os_type}")

    # Call the ssh_cmd function with the detected OS type
    ssh_cmd(os_type)

if __name__ == "__main__":
    print("Starting the script to terminate Python processes...")
    main()
    print("Script execution completed.")
