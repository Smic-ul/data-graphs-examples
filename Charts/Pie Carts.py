import matplotlib.pyplot as plt


nationality = ['Czech', 'German', 'Slovak', 'Polish']
students = [60, 23, 21, 34]

pairs = zip(students, nationality)
pairs = sorted(list(pairs))
students, nationality = zip(*pairs)

explode = [0, 0, 0.2, 0]

plt.pie(students, labels=nationality, autopct='%.2f%%', explode=explode, counterclock=False, startangle=90)
plt.title("Student Nationality")
plt.show()
