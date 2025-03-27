import pandas as pd
import dataframe as df
data = {
    'Student_id' : [101,101,101,101,101,102,102,102,102,103,103,103,103,103,104,104,104,104,104],
    'Attendace_Date':['2024-03-01','2024-03-02','2024-03-03','2024-03-04','2024-03-05','2024-03-02','2024-03-03',
                      '2024-03-04','2024-03-05','2024-03-05','2024-03-06','2024-03-07','2024-03-08','2024-03-09','2024-03-01',
                      '2024-03-02','2024-03-03','2024-03-04','2024-03-05'],
    'Status' :['absent','absent','absent','absent','present','absent',
               'absent','absent','absent','absent','absent','absent','absent',
               'absent','present','present','absent','present','present']
}
df = pd.df(data)
count =0
absent_streak=[]
for student_id, group in df.groupby('Student_id'):
    group = group.reset_index(drop=True)
    absence_start =0
    absence_end = 0
    for i in range(len(group)):
        if group['Status'][i] == 'absent':
            if count == 0:
                absence_start = group['Attendance_Date'][i]
            absence_end = group['Attendance_Date'][i]
            count = count+1
        else:
            if count > 3:
                absent_streak.append({
                    'student_id': student_id,
                    'absence_start_date':absence_start,
                    'absence_end_date': absence_end,
                    'count':count

                })
result = pd.df(absent_streak)
print(result)
data = {
    student_id :[101,102,103,104,105],
    student_name:['Alice Johnson','Bob Smith','Charlie Brown','David Lee','Eva white'],
    parent_email :['alice_parent@gmail.com','bob_parent@gmail.com','invalid_email.com',
                   'invalid_email.com','eva_white@example.com']
}
df = pd.df(data)
df['valid_email']=""
for i in parent_email:
    for j in range(len(parent_email)):
        if j[i] == @:
            valid_email.append(i)




