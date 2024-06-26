import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os



class BareboneBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("bc.calc")

        # Janela amarela
        self.root.configure(bg='yellow')

        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)
        self.text_area2 = tk.Text(self.root, height=10, width=50)
        self.text_area2.pack(pady=10)

        # Botões
        self.build_button = tk.Button(self.root, text="open", command=self.build_kernel)
        self.build_button.pack(pady=5)

        self.run_button = tk.Button(self.root, text="save", command=self.run_kernel)
        self.run_button.pack(pady=5)

        self.copy_button = tk.Button(self.root, text="run", command=self.copy_file)
        self.copy_button.pack(pady=5)
        self.text_area.delete(1.0, tk.END)
        self.text_area2.delete(1.0, tk.END)
        self.text_area.insert(tk.END,"(8.00*8.00)+8.00\n10.00\n10.00",True)

    def execute_command(self, command,show:bool):
        try:
            
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
            self.text_area2.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if show:
                self.text_area2.insert(tk.END,f"Error executing command:\n{e.output}")

    def build_kernel(self):
        self.text_area2.delete(1.0, tk.END)
        filename = tk.filedialog.askopenfilename(title="Select file")
        f1=open(filename,"r")
        txts=f1.read()
        
        f1.close()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, txts,True)
        
    
    def run_kernel(self):
        
        filename = tk.filedialog.asksaveasfilename(title="Select file")
        txts=self.text_area.get("1.0", "end-1c")
        f1=open(filename,"w")
        f1.write(txts)
        f1.close()
        txts=self.text_area2.get("1.0", "end-1c")
        f1=open(filename+".out","w")
        f1.write(txts)
        f1.close()
        self.text_area2.delete(1.0, tk.END)
    def copy_file(self):
        self.text_area2.delete(1.0, tk.END)
        totals:float=0
        txts=self.text_area.get("1.0", "end-1c")
        txts=txts.replace("\r","\n")
        txts=txts.replace("\n\n","\n")
        txs1=txts.split("\n")
        self.text_area2.insert(tk.END, "0.00\n",True)
        for n in txs1:
            try:
                nn:float=eval(n.strip())
                nnn=" = "+str(nn)+"\n"
                totals=totals+nn;
                nnn=str(totals)+nnn
                self.text_area2.insert(tk.END, nnn,True)
            except:
                self.text_area2.insert(tk.END,"error : "+n,True)
        

if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
