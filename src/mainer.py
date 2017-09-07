#we define our imports
import pygame
import pygame.midi 
import pyautogui as gui

inputStatus = 146
outputStatus = 130

#method to print out device info
def printDeviceInfo():
    #initialize the pygame midi
    pygame.midi.init()
    
    for i in range(pygame.midi.get_count()):
        r = pygame.midi.get_device_info(i)
        (interf, name, inputBool, output, opened) = r

        in_out = ""
        if inputBool:
            in_out = "(input)"
        if output:
            in_out = "(output)"
        
        print ("%2i: interface :%s:, name :%s:, opened :%s:  %s" %(i, interf, name, opened, in_out))
        
    #quit the pygame midi
    pygame.midi.quit()

#main method for the input functionality
def inputMain(deviceID = None):

    #we initialize pygame 
    pygame.init()
    pygame.fastevent.init()
    
    #we define these two objects to obtain and send I/O info
    #to the device
    event_get = pygame.fastevent.get
    event_post = pygame.fastevent.post

    #we initialize pygame MIDI
    pygame.midi.init()

    #we choose the midi device to be used
    if deviceID is None:
        inputID = pygame.midi.get_default_input_id()
    else:
        inputID = deviceID
    
    #we take the previously chosen midi device and make it our
    #input device
    inputDevice = pygame.midi.Input(inputID)
    
    #this while statement represents the execution of the program in runtime
    going = True
    while going:
        #we get all the I/O events that are occuring
        events = event_get()
        for e in events:

            #this event allows us to close out of the window
            if e.type in [pygame.QUIT]:
                going = False

            #this event considers taking midi input
            if e.type in [pygame.midi.MIDIIN]:

                print(e)

                #store the value of the key pressed
                keybind = e.data1
                #store the value of input vs. output
                status = e.status

                #set of conditional statements to tell which button was pressed
                if keybind == 36 and status == inputStatus:
                    print("Opening Google chrome")
                    gui.hotkey('win','1')

                elif keybind == 37 and status == inputStatus:
                    print("Opening Firefox")
                    gui.hotkey('win','2')

                elif keybind == 38 and status == inputStatus:
                    print("Opening Bash GUI")
                    gui.hotkey('win','3')

                elif keybind == 39 and status == inputStatus:
                    print("Opening Adobe Reader")
                    gui.hotkey('win','4')

                elif keybind == 40 and status == inputStatus:
                    print("Opening Word")
                    gui.hotkey('win','5')

                elif keybind == 41 and status == inputStatus:
                    print("Opening Notepad++")
                    gui.hotkey('win','6')

                elif keybind == 42 and status == inputStatus:
                    print("Opening TeX Studio")
                    gui.hotkey('win','7')

                elif keybind == 43 and status == inputStatus:
                    print("Opening Mathematica")
                    gui.hotkey('win','8')

                elif keybind == 44 and status == inputStatus:
                    print("Opening Eclipse")
                    gui.hotkey('win','9')

        if inputDevice.poll():
            midiEvents = inputDevice.read(10)
            # convert them into pygame events.
            midiEvs = pygame.midi.midis2events(midiEvents, inputDevice.device_id)

            for mE in midiEvs:
                event_post(mE)
        
    del inputDevice
    pygame.midi.quit()

    

#main method
def main():
      
    #print out the device info
    #printDeviceInfo()

    #run the input main
    inputMain(1)

#run the main method
if __name__ == "__main__":
    main()



