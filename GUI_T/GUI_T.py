# Tim Do 
# Oregon State University 
# College of EECS
# February 7th, 2024

import customtkinter                                                                                                # Customtkinter; python UI library
import tkinter as tk                                                                                                # tkinter; python UI library

customtkinter.set_appearance_mode("dark")                                                                           # Dark Background
customtkinter.set_default_color_theme("dark-blue")                                                                  # Dark Blue Theme

root = customtkinter.CTk()                                                                                          # Root Element
root.geometry("469x540")                                                                                            # Window Size
root.title("EJ16 GUI")                                                                                              # Name of Window
root.resizable(width=False, height=False)                                                                           # Unchangeable Window Size to prevent user error

def sliding(v):                                                                                                     # Define Function to Create Voltage Slider
    my_labelV.configure(text=(v, "Volts"))                                                                          # NOTE: NEED "{:3g}".format(value) to have 3 sig figs
    print (v, "Volts has been applied!")                                                                            # Print Out Selected Voltage on Console

### FRAME FOR SLIDERS                                                                                   
oneFrame = customtkinter.CTkFrame(master=root)                                                                      # Contain Elements Inside Frame
oneFrame.pack(pady = 10, padx = 10, fill="both")                                                                    # Spacing for Frame Around Sliders

my_labelV = customtkinter.CTkLabel(master=oneFrame, text="Select Voltage:", font=("", 21))                          # Title for Voltage Slider                        
my_labelV.pack(pady=20)                                                                                             # Spacing for Title of Voltage Slider                            

my_slider= customtkinter.CTkSlider(master=oneFrame,                                                                 # Voltage Slider                            
    from_=2,                                                                                                        # Minimum Voltage Allowed                                
    to=14,                                                                                                          # Maximum Voltage Allowed                     
    command=sliding,                                                                                                # Call function to slide                       
    width=400,                                                                                                      # Width of Slider Bar
    height=35,                                                                                                      # Height of Slider Bar                                         
    border_width=15,                                                                                                # Thickness of Slider Bar
    fg_color="white",                                                                                               # Color of Voltage Slider Passive
    progress_color="yellow")                                                                                        # Color of Voltage Slider Active

my_slider.pack(pady=20)                                                                                             # Spacing around Voltage Slider
my_slider.set(2)                                                                                                    # Starting Value of Voltage Slider

def sliding(i):                                                                                                     # Define Function to Create Current Slider
    my_labelI.configure(text=(i, "Amps"))                                                                           # Display Selected Current on GUI
    print (i, "Amps has been applied!")                                                                             # Print Out Selected Current on Console
    
my_slider= customtkinter.CTkSlider(master=oneFrame,                                                                 # Current Slider
    from_=0,                                                                                                        # Minimum Amperage Allowed
    to=1.5,                                                                                                         # Maximum Amperage Allowed
    command=sliding,                                                                                                # Call function to slide
    width=400,                                                                                                      # Width of Slider Bar
    height=35,                                                                                                      # Height of Slider Bar
    border_width=15,                                                                                                # Thickness of Slider Bar
    fg_color="white",                                                                                               # Color of Current Slider Passive
    progress_color="blue")                                                                                          # Color of Current Slider Active

my_slider.pack(pady=20)                                                                                             # Spacing around Current Slider
my_slider.set(0)                                                                                                    # Starting Value of Current Slider

my_labelI = customtkinter.CTkLabel(master=oneFrame, text="Select Current:", font=("", 21))                          # Title for Current Slider
my_labelI.pack(pady=20)                                                                                             # Spacing for Title of Current Slider

def adjust():                                                                                                       # Define Function to Apply Settings
    spg=entry1.get()                                                                                                # Get data from Voltage Entry Text Box
    fpg=entry2.get()                                                                                                # Get data from Current Entry Text Box
    print(spg, "volts and", fpg, "amps have been applied!")                                                         # Print out onto Console Volts and Amps

### FRAME FOR LABEL, TEXT BOX, AND BUTTON
twoFrame = customtkinter.CTkFrame(master=root)                                                                      # Contain Elements Inside Frame
twoFrame.pack(pady = 10, padx = 10, fill="both")                                                                    # Spacing for Frame Around Sliders

label = customtkinter.CTkLabel(master=twoFrame, text="Voltage and Current Adjuster", font=("", 19))                 # Label for Bottom Frame
label.pack(pady=12, padx=10)                                                                                        # Spacing for Aforementioned Label

entry1 = customtkinter.CTkEntry(master=twoFrame, placeholder_text="Enter Voltage")                                  # Entry Text Box for Voltage
entry1.pack(pady=12, padx=10)                                                                                       # Spacing for Aforementioned Text Box
    
entry2 = customtkinter.CTkEntry(master=twoFrame, placeholder_text="Enter Current")                                  # Entry Text Box for Current
entry2.pack(pady=12, padx=10)                                                                                       # Spacing for Aforementioned Text Box
  
button = customtkinter.CTkButton(master=twoFrame, text="Apply", command=adjust)                                     # Button to Apply Settings
button.pack(pady=12, padx=10)                                                                                       # Spacing for Aforementioned Button

root.mainloop()                                                                                                     # Loop