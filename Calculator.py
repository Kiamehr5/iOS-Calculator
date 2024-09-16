import tkinter as tk

window = tk.Tk()

window.title("Calculator")

lbl_result = tk.Label(window, text = "0", width = 30, height = 3, bg = "#6D6D6D", fg="white")
lbl_result.grid(row = 0, column = 0, columnspan = 4)

def clear():
    lbl_result.config(text = "")

def sum(equation):
    flag = False
    if equation[0] == "-":
           equation = equation.removeprefix('-')
           flag = True
       
    if "+" in equation:
                    num1, num2 = equation.split("+")
                    try:
                        if flag:
                            num1 = f"-{num1}"
                        result = int(num1) + int(num2)
                    except ValueError:
                        if flag:
                            num1 = f"-{num1}"
                        result = float(num1) + float(num2)
                        
    elif "-" in equation:
                    num1, num2 = equation.split("-")
                    try:
                        if flag:
                            num1 = f"-{num1}"
                        result = int(num1) - int(num2)
                    except ValueError:
                        if flag:
                            num1 = f"-{num1}"
                        result = float(num1) - float(num2)
    else:
                    num1, num2 = equation.split("x")
                    try:
                        if flag:
                            num1 = f"-{num1}"
                        result = int(num1) * int(num2)
                    except ValueError:
                        if flag:
                            num1 = f"-{num1}"
                        result = float(num1) * float(num2)
           
    lbl_result.config(text = f"{result}")

def is_decimal(current):
    for i in current[::-1]:
        if i == ".":
            return False
        elif i in ["+", "-", "x"]:
            return True
    return True

def func(btn_txt):
    first = True
    count = 0
    current = lbl_result["text"]
    flag = True
    if current == "0":
        lbl_result.config(text = btn_txt)
        flag = False
        # lbl_result["text"] += btn_txt

    else:
        if btn_txt in ["-", "+", "x"]:    
            for i in lbl_result['text'][::-1]:
                if (count == 0) and (i == "."):
                    flag = False
                    return
                count += 1
                      
            if "+" in lbl_result["text"]:
                if "+" == btn_txt:
                    flag = False
                    return
                elif btn_txt != "+":
                    lbl_result.config(text = lbl_result['text'].replace("+", btn_txt))
                    flag = False

                
            elif "-" in lbl_result["text"]:
                if "-" == btn_txt:
                    flag = False
                    return
                elif btn_txt != "-":
                     lbl_result.config(text = lbl_result['text'].replace("-", btn_txt))
                     flag = False
            
            elif "x" in lbl_result["text"]:
                if "x" == btn_txt:
                    flag = False
                    return
                elif btn_txt != "x":
                    lbl_result.config(text = lbl_result['text'].replace("x", btn_txt))
                    flag = False

        elif btn_txt == ".":
            for i in lbl_result['text'][::-1]:
                if i in ["+", "-", "x"]:
                    if first:
                        flag = False
                        return
                first = False
            flag = is_decimal(lbl_result['text'])
            
            

                
    if flag:
        lbl_result["text"] += btn_txt


btn_0 = tk.Button(window, text = "0", command = lambda:func("0"),
                  height = 3, fg = "white", bg = "#333333")
btn_0.grid(row = 4, column = 1, sticky = "nsew")

btn_1 = tk.Button(window, text = "1", command = lambda:func("1"),
                  height = 3, fg = "white", bg = "#333333")
btn_1.grid(row = 3, column = 0, sticky = "nsew")

btn_2 = tk.Button(window, text = "2", command = lambda:func("2"),
                  height = 3, fg = "white", bg = "#333333")
btn_2.grid(row = 3, column = 1, sticky = "nsew")

btn_3 = tk.Button(window, text = "3", command = lambda:func("3"),
                  height = 3, fg = "white", bg = "#333333")
btn_3.grid(row = 3, column = 2, sticky = "nsew")

btn_4 = tk.Button(window, text = "4", command = lambda:func("4"),
                  height = 3, fg = "white", bg = "#333333")
btn_4.grid(row = 2, column = 0, sticky = "nsew")

btn_5 = tk.Button(window, text = "5", command = lambda:func("5"),
                  height = 3, fg = "white", bg = "#333333")
btn_5.grid(row = 2, column = 1, sticky = "nsew")

btn_6 = tk.Button(window, text = "6", command = lambda:func("6"),
                  height = 3, fg = "white", bg = "#333333")
btn_6.grid(row = 2, column = 2, sticky = "nsew")

btn_7 = tk.Button(window, text = "7", command = lambda:func("7"),
                  height = 3, fg = "white", bg = "#333333")
btn_7.grid(row = 1, column = 0, sticky = "nsew")

btn_8 = tk.Button(window, text = "8", command = lambda:func("8"),
                  height = 3, fg = "white", bg = "#333333")
btn_8.grid(row = 1, column = 1, sticky = "nsew")

btn_9 = tk.Button(window, text = "9", command = lambda:func("9"),
                  height = 3, fg = "white", bg = "#333333")
btn_9.grid(row = 1, column = 2, sticky = "nsew")

btn_plus = tk.Button(window, text = "+", command = lambda:func("+"),
                     height = 3, fg = "white", bg = "#ff9f0c")
btn_plus.grid(row = 1, column = 3, sticky = "nsew")

btn_minus = tk.Button(window, text = "-", command = lambda:func("-"),
                  height = 3, fg = "white", bg = "#ff9f0c")
btn_minus.grid(row = 2, column = 3, sticky = "nsew")

btn_mult = tk.Button(window, text = "x", command = lambda:func("x"),
                  height = 3, fg = "white", bg = "#ff9f0c")
btn_mult.grid(row = 3, column = 3, sticky = "nsew")

btn_clear = tk.Button(window, text = "C", command = clear,
                 height = 3, fg = "white", bg = "#333333")
btn_clear.grid(row = 4, column = 0, sticky = "nsew")

btn_dot = tk.Button(window, text = ".", command = lambda:func("."),
                  height = 3, fg = "white", bg = "#333333")
btn_dot.grid(row = 4, column = 2, sticky = "nsew")

btn_sum = tk.Button(window, text = "=", command = lambda:sum(lbl_result["text"]),
                  height = 3, fg = "white", bg = "#ff9f0c")
btn_sum.grid(row = 4, column = 3, sticky = "nsew")

window.mainloop()
