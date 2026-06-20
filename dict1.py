students_scores={'a':90,'b':89,'c':79,'d':95,'e':70}
tot=sum(students_scores.values())
avg=tot/len(students_scores)
above_avg={}
def new_func(students_scores, avg, above_avg):
    for name,score in students_scores.items():
        if score>avg:
            above_avg[name]=score
    print(above_avg)

new_func(students_scores, avg, above_avg)
