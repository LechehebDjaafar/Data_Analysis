# ----------------Info Developer-------------
# -Last Name : Lecheheb
# -First Name : Djaafar
# -Country : Algeria
# -age : 26
# -Skills : Python - HTML - CSS - C
# -instagram : @ddos_attack_co
# ------------Fallowed Me for instagram-------

'''
فلنفترض أن لدينا المعادلات التالية:
aX + bY + cZ = k1
a2X + b2Y + c2Z = k2
a3X + b3Y + c3Z = k3
و منه نستخرج هذه المصفوفة
[a  b   c] [X]    [k1]
[a2 b2 c2] [Y] == [k2]
[a3 b3 c3] [Z]    [k3]

مثال:
3X + Y + 7 Z = 5
6X + 2Y + 9 Z = 2
X + Y +  Z = 4
'''

import numpy as np
from tkinter import *

# إعداد النافذة
root = Tk()
root.title("Solve a matrix using gauss")
root.geometry("400x300")  # تحديد حجم نافذة التطبيق

# دالة لإنشاء وتخصيص عناصر Label
def create_label(root, text, rows, columns):
    Label(root, text=text, font=("Arial", 14)).grid(row=rows, column=columns)

# دالة لتنفيذ الحل وعرض النتائج
def display_solution(fun, r):
    root.geometry('700x300')
    t = r
    lists = fun()
    c = 0
    for n in lists:
        for i in n:
            create_label(root, i, r, c)
            c += 1
        c = 0
        r += 1
    tex = f"X = {x:.2f}, Y = {y:.2f}, Z = {z:.2f}"
    Label(root, text=tex, font=("Arial", 14)).grid(row=t - 1, column=8)

# دالة لإنشاء وتخصيص مدخلات المعادلات
def create_entries():
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, R1, R2, R3
    rows = 0
    columns = 0
    a1 = Entry(root, width=3, font=("Arial", 14))
    a1.grid(row=rows, column=columns)
    columns += 1
    create_label(root, 'X', rows, columns)
    columns += 1
    a2 = Entry(root, width=3, font=("Arial", 14))
    a2.grid(row=rows, column=columns)
    columns += 1
    create_label(root, 'Y', rows, columns)
    columns += 1
    a3 = Entry(root, width=3, font=("Arial", 14))
    a3.grid(row=rows, column=columns)
    columns += 1
    create_label(root, 'Z', rows, columns)
    columns += 1
    create_label(root, '==', rows, columns)
    R1 = Entry(root, width=3, font=("Arial", 14))
    R1.grid(row=rows, column=columns + 1)
    columns = 0
    # #################################################
    rows = 1
    a4 = Entry(root, width=3, font=("Arial", 14))
    a4.grid(row=rows, column=columns)
    columns += 1
    create_label(root, 'X', rows, columns)
    columns += 1
    a5 = Entry(root, width=3, font=("Arial", 14))
    a5.grid(row=rows, column=columns)
    columns += 1
    create_label(root, 'Y', rows, columns)
    columns += 1
    a6 = Entry(root, width=3, font=("Arial", 14))
    a6.grid(row=rows, column=columns)
    columns += 1
    create_label(root, 'Z', rows, columns)
    columns += 1
    create_label(root, '==', rows, columns)
    R2 = Entry(root, width=3, font=("Arial", 14))
    R2.grid(row=rows, column=columns + 1)
    columns = 0
    # ##############################################3##333
    rows = 2
    a7 = Entry(root, width=3, font=("Arial", 14))
    a7.grid(row=rows, column=columns)
    columns += 1
    create_label(root, 'X', rows, columns)
    columns += 1
    a8 = Entry(root, width=3, font=("Arial", 14))
    a8.grid(row=rows, column=columns)
    columns += 1
    create_label(root, 'Y', rows, columns)
    columns += 1
    a9 = Entry(root, width=3, font=("Arial", 14))
    a9.grid(row=rows, column=columns)
    columns += 1
    create_label(root, 'Z', rows, columns)
    columns += 1
    create_label(root, '==', rows, columns)
    columns += 1
    R3 = Entry(root, width=3, font=("Arial", 14))
    R3.grid(row=rows, column=columns)

    button_run = Button(root, text="Run", font=("Arial", 14), command=lambda: display_solution(check_list, rows + 2))
    button_run.grid(row=rows + 1, column=0)

# إنشاء مدخلات المعادلات
create_entries()

# مثال:
# 3X + Y + 7 Z = 5
# 6X + 2Y + 9 Z = 2
# X + Y +  Z = 4

# دالة لتنفيذ حسابات المعادلات
def check_list():
    global x, y, z

    # تعريف المصفوفة
    square_matrix = [[int(a1.get()), int(a2.get()), int(a3.get())],
                     [int(a4.get()), int(a5.get()), int(a6.get())],
                     [int(a7.get()), int(a8.get()), int(a9.get())]]

    constants = [int(R1.get()), int(R2.get()), int(R3.get())]

    print(f"{square_matrix[0][0]}X + {square_matrix[0][1]}Y + {square_matrix[0][2]}Z = {constants[0]}")
    print(f"{square_matrix[1][0]}X + {square_matrix[1][1]}Y + {square_matrix[1][2]}Z = {constants[1]}")
    print(f"{square_matrix[2][0]}X + {square_matrix[2][1]}Y + {square_matrix[2][2]}z = {constants[2]}")

    # حل المعادلات
    solution = np.linalg.solve(square_matrix, constants)

    # قيم x و y و z
    x, y, z = solution
    print("=" * 60)
    print(f"X = {x:.2f}, Y = {y:.2f}, Z = {z:.2f}")
    print("=" * 60)

    print(f"{square_matrix[0][0] * x:.2f} + {square_matrix[0][1] * y:.2f} + {square_matrix[0][2] * z:.2f} = {constants[0]}")
    print(f"{square_matrix[1][0] * x:.2f} + {square_matrix[1][1] * y:.2f} + {square_matrix[1][2] * z:.2f} = {constants[1]}")
    print(f"{square_matrix[2][0] * x:.2f} + {square_matrix[2][1] * y:.2f} + {square_matrix[2][2] * z:.2f} = {constants[2]}")

    lists = [
        [f"{square_matrix[0][0] * x:.2f}", f"{square_matrix[0][1] * y:.2f}", f"{square_matrix[0][2] * z:.2f}", "==",
         f"{constants[0]}"],
        [f"{square_matrix[1][0] * x:.2f}", f"{square_matrix[1][1] * y:.2f}", f"{square_matrix[1][2] * z:.2f}", "==",
         f"{constants[1]}"],
        [f"{square_matrix[2][0] * x:.2f}", f"{square_matrix[2][1] * y:.2f}", f"{square_matrix[2][2] * z:.2f}", "==",
         f"{constants[2]}"]
    ]
    return lists

# دالة الدخول الرئيسية لعرض النافذة
mainloop()
