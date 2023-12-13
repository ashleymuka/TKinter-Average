'''
Author: Ashley Muka
Assignment Title: TKinter Averages
Assignment Description:create a python program to help calculate
the average of three test scores. Program should gave a GUI
Due Date:11/10/2023
Date Created:11/08/2023
Date Last Modified:11/10/2023

'''


import tkinter as tk
import tkinter.font as tkFont

#process and output
class TestScoreApp:
    def __init__ (self, root):
        self.root = root
        self.root.title("Test Average Calculator")
        self.create_widgets()


    def create_widgets(self):
        
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        label_font = tkFont.Font(family="Arial", size=20, weight="bold")

        score1_label = tk.Label(input_frame, text="Test Score 1:", font=label_font)
        self.score1_entry = tk.Entry(input_frame, font=label_font)
        
        score2_label = tk.Label(input_frame, text="Test Score 2:", font=label_font)
        self.score2_entry = tk.Entry(input_frame, font=label_font)
        
        score3_label = tk.Label(input_frame, text="Test Score 3:", font=label_font)
        self.score3_entry = tk.Entry(input_frame, font=label_font)
    
        calculate_button = tk.Button(input_frame, text="Calculate Average", command=self.calculate_average)
        
        self.average_label = tk.Label(self.root, text="", font=label_font)

        quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)


        score1_label.grid(row=0, column=0)
        self.score1_entry.grid(row=0, column=1)
        score2_label.grid(row=1, column=0)
        self.score2_entry.grid(row=1, column=1)
        score3_label.grid(row=2, column=0)
        self.score3_entry.grid(row=2, column=1)
        calculate_button.grid(row=3, columnspan=2)
        self.average_label.pack(pady=10)
        quit_button.pack(pady=10)


    def calculate_average(self):
#input        
        score1 = float(self.score1_entry.get())
        score2 = float(self.score2_entry.get())
        score3 = float(self.score3_entry.get())

        average = (score1 + score2 + score3) / 3

        self.average_label.config(text=f"Average: {average:.2f}")

    
if __name__ == "__main__":
    
    root = tk.Tk()
    app = TestScoreApp(root)
    root.mainloop()

