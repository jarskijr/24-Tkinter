"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Jacob Jarski.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk
import random


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    # -------------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------

    frame1 = ttk.Frame(root, padding=20)
    frame1.grid()

    # -------------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------

    print_hello_button = ttk.Button(frame1, text='Print Hello')

    # -------------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------
    print_hello_button['command'] = (lambda: print('Hello'))
    print_hello_button.grid(row = 0, column = 0)


    # -------------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------
    sample_entry_box = ttk.Entry(frame1)
    sample_entry_box.grid(row = 1, column = 0)
    picky_hello_button = ttk.Button(frame1, text = 'Picky Hello')
    picky_hello_button['command'] = (lambda: picky_hello(sample_entry_box))
    picky_hello_button.grid(row = 2, column = 0)


    second_entry_box = ttk.Entry(frame1)
    second_entry_box.grid(row = 1, column = 1)
    third_button_function = ttk.Button(frame1, text = 'Print amount of times')
    third_button_function['command'] = (lambda: print_times(second_entry_box, sample_entry_box))
    third_button_function.grid(row = 2, column = 1)




    # -------------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # -------------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------

    root.mainloop()

def picky_hello(input_of_picky_hello):
    input_of_picky_hello = input_of_picky_hello.get()
    if input_of_picky_hello == 'ok':
        print('Hello')
    else:
        print('Goodbye')
def print_times(amount_of_times, input_of_picky_hello):
    number_of_times_input = amount_of_times.get()
    string_to_print = input_of_picky_hello.get()
    for k in range(int(number_of_times_input)):
        print(string_to_print)
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
