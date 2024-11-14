from tkinter import *
import tkinter as tk
import random
import time

# Function to swap two bars that will be animated
def swap(pos_0, pos_1):
    bar11, _, bar12, _ = canvas.coords(pos_0)
    bar21, _, bar22, _ = canvas.coords(pos_1)
    canvas.move(pos_0, bar21-bar11, 0)
    canvas.move(pos_1, bar12-bar22, 0)

worker = None 

# Insertion Sort
def _insertion_sort():
    global barList
    global lengthList
    for i in range(len(lengthList)):
        cursor = lengthList[i]
        cursorBar = barList[i]
        pos = i
        while pos > 0 and lengthList[pos - 1] > cursor:
            lengthList[pos] = lengthList[pos - 1]
            barList[pos], barList[pos - 1] = barList[pos - 1], barList[pos]
            swap(barList[pos], barList[pos-1])   
            yield                                       
            pos -= 1                                   
        lengthList[pos] = cursor
        barList[pos] = cursorBar
        swap(barList[pos], cursorBar)

# Bubble Sort
def _bubble_sort():
    global barList
    global lengthList
    for i in range(len(lengthList) - 1):
        for j in range(len(lengthList) - i - 1):
            if(lengthList[j] > lengthList[j + 1]):
                lengthList[j], lengthList[j + 1] = lengthList[j + 1], lengthList[j]
                barList[j], barList[j + 1] = barList[j + 1], barList[j]
                swap(barList[j + 1], barList[j])
                yield        

# Selection Sort
def _selection_sort():
    global barList    
    global lengthList
    for i in range(len(lengthList)):
        min = i
        time.sleep(0.5)
        for j in range(i + 1, len(lengthList)):
            if(lengthList[j] < lengthList[min]):
                min = j
        lengthList[min], lengthList[i] = lengthList[i], lengthList[min]
        barList[min], barList[i] = barList[i], barList[min]
        swap(barList[min], barList[i])
        yield

# Triggering Functions
def insertion_sort():     
    global worker
    worker = _insertion_sort()
    animate()
    time_complexity_label.config(text="Time Complexity: O(n^2)")

def selection_sort():     
    global worker
    worker = _selection_sort()
    animate()    
    time_complexity_label.config(text="Time Complexity: O(n^2)")

def bubble_sort():     
    global worker
    worker = _bubble_sort()
    animate()    
    time_complexity_label.config(text="Time Complexity: O(n^2)")

# Animation Function
def animate():      
    global worker
    if worker is not None:
        try:
            next(worker)
            window.after(10, animate)    
        except StopIteration:            
            worker = None
        finally:
            window.after_cancel(animate) 

# Generator function for generating data
def generate():
    global barList
    global lengthList
    canvas.delete('all')
    barstart = 5
    barend = 15
    barList = []
    lengthList = []

    # Creating a rectangle with muted pastel colors for bars
    for bar in range(0, (number)):
        randomY = random.randint(1, 360)
        bar = canvas.create_rectangle(barstart, randomY, barend, 365, fill='#82CFFD', width=2)
        barList.append(bar)
        barstart += 10
        barend += 10

    # Getting length of the bar and appending into length list
    for bar in barList:
        bar = canvas.coords(bar)
        length = bar[3] - bar[1]
        lengthList.append(length)

    # Maximum is colored Red
    # Minimum is colored Black
    for i in range(len(lengthList)-1):
        if lengthList[i] == min(lengthList):
            canvas.itemconfig(barList[i], fill='#FF6F61')  # Soft red for minimum
        elif lengthList[i] == max(lengthList):
            canvas.itemconfig(barList[i], fill='#333')  # Dark gray for maximum

# Accept number of inputs
def Accept_value():
   global number
   t1 = int(a.get())
   number = t1
   input_frame.pack_forget()  # Hide input screen
   sorting_ui()  # Go to sorting screen after input
   generate()  # Generate bars after accepting input

# Modern UI design
def create_ui():
    # Main window
    window = tk.Tk()
    window.title('Sorting Visualizer')
    window.geometry('1000x500')
    window.configure(bg='#F0F0F0')  # Light background color
    window.state('zoomed')  # Windowed full-screen mode

    return window

# Input window UI design
def input_ui():
    global a, input_frame
    input_frame = Frame(window, bg='#F0F0F0')
    input_frame.pack(fill=BOTH, expand=True)

    # Add the name, registration number, and university details
    name_label = Label(input_frame, text="Gautam Kakkar", font=("Arial", 12), fg='#333', bg='#F0F0F0')
    name_label.pack(pady=5)

    reg_label = Label(input_frame, text="23FE10CSE00152", font=("Arial", 12), fg='#333', bg='#F0F0F0')
    reg_label.pack(pady=5)

    uni_label = Label(input_frame, text="Manipal University Jaipur", font=("Arial", 12), fg='#333', bg='#F0F0F0')
    uni_label.pack(pady=5)

    # Add the new label for the mini project
    project_label = Label(input_frame, text="OOPS using Python (CS2122) Mini Project", font=("Arial", 12), fg='#333', bg='#F0F0F0')
    project_label.pack(pady=5)

    # Labels with your details
    label = Label(input_frame, text="Enter Number of Bars:", font=("Arial", 14), fg='#333', bg='#F0F0F0')
    label.pack(pady=20)

    # Input for number of bars
    a = Entry(input_frame, width=20, font=("Arial", 14))
    a.pack(pady=10)

    button = Button(input_frame, text="Submit", command=Accept_value, bg="#82CFFD", fg="white", font=("Arial", 12, "bold"))
    button.pack(pady=20)

# Main Sorting Window with Canvas and Buttons
def sorting_ui():
    global canvas, barList, lengthList, worker, time_complexity_label
    window.configure(bg='#F0F0F0')

    canvas = tk.Canvas(window, width=1000, height=400, bg="#E8E8E8", bd=0, highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Buttons with modern style
    insert = tk.Button(window, text='Insertion Sort', command=insertion_sort, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), relief="flat")
    insert.grid(row=1, column=0, padx=10, pady=20)

    select = tk.Button(window, text='Selection Sort', command=selection_sort, bg="#FF5722", fg="white", font=("Arial", 12, "bold"), relief="flat")
    select.grid(row=1, column=1, padx=10, pady=20)

    bubble = tk.Button(window, text='Bubble Sort', command=bubble_sort, bg="#00BCD4", fg="white", font=("Arial", 12, "bold"), relief="flat")
    bubble.grid(row=1, column=2, padx=10, pady=20)

    shuffle = tk.Button(window, text='Shuffle', command=generate, bg="#FFC107", fg="white", font=("Arial", 12, "bold"), relief="flat")
    shuffle.grid(row=1, column=3, padx=10, pady=20)

    # Time Complexity Label
    time_complexity_label = Label(window, text="Time Complexity: O(n^2)", font=("Arial", 12), fg="#333", bg="#F0F0F0")
    time_complexity_label.grid(row=2, column=0, columnspan=4, pady=10)

    # Reset button
    reset_button = Button(window, text="Reset", command=reset, bg="#9E9E9E", fg="white", font=("Arial", 12, "bold"), relief="flat")
    reset_button.grid(row=3, column=3, padx=10, pady=20)

# Reset the screen to initial state without adding another canvas or bar down
def reset():
    global worker, barList, lengthList
    worker = None
    canvas.delete('all')  # Clear all content in the canvas
    generate()  # Redraw the bars
    time_complexity_label.config(text="Time Complexity: O(n^2)")  # Reset time complexity label

# Main Program Execution
window = create_ui()
input_ui()
window.mainloop()
