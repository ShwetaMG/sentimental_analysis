def handler():
	num=box.get()
	try:
		num=int(num)
		if num % 2 ==0:
	        	text="even"
		else:
			text="odd"
		label.config(text=text)

	except Exception as e:
		label.config(text=f"{num} not number")
	
			
import tkinter as tk
root = tk.Tk()
box = tk.Entry(root)
btn = tk.Button(root,text="submit",fg="yellow",bg="red",command=handler)
box.grid(row=0,column=0)
btn.grid(row=0,column=1)
label =tk.Label(root,text=" ")
label.grid(row=1,column=0)

root.mainloop()