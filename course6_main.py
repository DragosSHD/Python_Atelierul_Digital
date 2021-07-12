# Tkinter Side

import tkinter
from course6_fields import Field


def save_grade(firstname, lastname, email, subject_name, grade):
    print(firstname, lastname, email, subject_name, grade)


window = tkinter.Tk()
window.mainloop()
window.geometry('800x600')
window.title('Custom title')

inner_frame = tkinter.Frame(window, bg='#ff0000', width='300', height='300')
inner_frame.pack()

label = tkinter.Label(inner_frame, text='Student first name')
label.pack()

first_name_field = Field(inner_frame, 'Firstname')
last_name_field = Field(inner_frame, 'Lastname')
email_field = Field(inner_frame, 'Subject name')
subject_name_field = Field(inner_frame, 'Subject Name')
student_grade_field = Field(inner_frame, 'Grade')

save_btn = tkinter.Button(inner_frame, text='Save Grade', command=lambda: save_grade(
    first_name_field.entry(),
    last_name_field.entry(),
    email_field.entry(),
    subject_name_field.entry(),
    student_grade_field.entry()
))
save_btn.pack()

window.mainloop()


