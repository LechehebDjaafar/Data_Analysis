import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialize variables
points = []
covariance_matrix = None
eigenvalues = None
eigenvectors = None

# تحديد عدد الأرقام العشرية المطلوبة
decimal_places = 2

def generate_point():
    """
    تقوم بإنشاء نقطة جديدة بإحداثيات عشوائية ولون عشوائي، وتضيفها إلى قائمة النقاط.
    """
    x = round(np.random.uniform(0, 50), decimal_places)
    y = round(np.random.uniform(0, 50), decimal_places)
    
    # إنشاء لون عشوائي
    color = np.random.rand(3,)  # RGB values
    
    points.append((x, y, color))
    
    # طباعة إحداثيات النقطة المولدة ولونها وقائمة كل النقاط
    print(f"Generated point:\nX = {x}, Y = {y}, Color = {color}")
    print("All points:")
    for i, point in enumerate(points):
        print(f"Point({i}): X = {point[0]}, Y = {point[1]}, Color = {point[2]}")
    
    plot_points()

def calculate_covariance():
    """
    تقوم بحساب مصفوفة التشابه (Covariance Matrix) إذا كان هناك على الأقل نقطتين.
    """
    global covariance_matrix
    if len(points) < 2:
        print("At least two points are needed to calculate covariance.")
        return

    # استخدام حلقة for لاستخراج الإحداثيات من كل نقطة بشكل فردي
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    
    points_array = np.array([x_values, y_values])
    covariance_matrix = np.cov(points_array, rowvar=False)
    
    # طباعة مصفوفة التشابه
    print("Covariance Matrix:")
    print(covariance_matrix)

def calculate_eigen():
    """
    تقوم بحساب القيم الذاتية والقوائم الذاتية لمصفوفة التشابه.
    """
    global eigenvalues, eigenvectors
    if covariance_matrix is None:
        print("Calculate covariance matrix first.")
        return

    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    
    # طباعة القيم الذاتية والقوائم الذاتية
    print("Eigenvalues:")
    print(eigenvalues)
    print("Eigenvectors:")
    print(eigenvectors)
    
    # رسم الخطوط الممثلة للأوتوفيكتورات
    plot_vectors()

def plot_vectors():
    """
    تقوم برسم الخطوط الممثلة للأوتوفيكتورات على الرسم البياني.
    """
    if eigenvectors is not None:
        # حساب متوسط الإحداثيات
        x_values = [point[0] for point in points]
        y_values = [point[1] for point in points]
        origin = (np.mean(x_values), np.mean(y_values))
        
        for i, vector in enumerate(eigenvectors.T):
            plt.quiver(*origin, *vector[:2], angles='xy', scale_units='xy', scale=1, color=f'C{i}', label=f'Eigenvector {i+1}')

        plt.legend()
        canvas.draw()

def change_position():
    """
    تقوم بتغيير مواقع النقاط بإحداثيات عشوائية جديدة.
    """
    if len(points) == 0:
        print("No points to change.")
        return

    new_points = [(round(np.random.uniform(0, 10), decimal_places), round(np.random.uniform(0, 10), decimal_places), np.random.rand(3,)) for _ in points]
    points.clear()
    points.extend(new_points)
    
    # طباعة قائمة النقاط بعد تغيير المواقع
    print("Changed positions of points:")
    for i, point in enumerate(points):
        print(f"Point({i}): X = {point[0]}, Y = {point[1]}, Color = {point[2]}")
    
    plot_points()

def plot_points():
    """
    تقوم برسم النقاط على الرسم البياني.
    """
    ax.clear()
    if points:
        for point in points:
            ax.scatter(point[0], point[1], color=point[2], s=50)  # رسم النقطة بلونها
        ax.set_title('Points Visualization')
        
        # إذا كانت الأوتوفيكتورات محسوبة، رسم الخطوط الممثلة لها
        if eigenvectors is not None:
            plot_vectors()
        
        canvas.draw()

def exit_program():
    """
    تقوم بإنهاء تشغيل البرنامج.
    """
    exit()

# Create main window
root = tk.Tk()
root.title("Point Operations")

# تعيين لون خلفية النافذة إلى اللون الأسود
root.configure(bg='black')
# Create buttons using grid
button_generate = tk.Button(root, text="Generate Point",bg='Red',width=30,height=5, command=generate_point)
button_covariance = tk.Button(root, text="Calculate Covariance",bg='Red',width=30,height=5, command=calculate_covariance)
button_eigen = tk.Button(root, text="Calculate Eigenvalues/Vectors",bg='Red',width=30,height=5, command=calculate_eigen)
button_change_position = tk.Button(root, text="Change Point Positions",bg='Red',width=30,height=5, command=change_position)
button_exit = tk.Button(root, text="Exit",bg='Red',width=30,height=5, command=exit_program)

# استخدام خاصية column بدلاً من row لتحديد ترتيب الأزرار عموديًا
button_generate.grid(row=0, column=0, pady=5)
button_covariance.grid(row=1, column=0, pady=5)
button_eigen.grid(row=2, column=0, pady=5)
button_change_position.grid(row=3, column=0, pady=5)
button_exit.grid(row=4, column=0, pady=5)

# Create a figure and axis for plotting using grid
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=1, rowspan=5)

# Start the Tkinter main loop
root.mainloop()
