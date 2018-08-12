import datetime

now = datetime.datetime.now()
birthday = ''
while(1):
    birthday = input('what is ur birthday dd-mm-yyy: ').split('-')
    if len(birthday) == 3:
        then = datetime.date(int(birthday[2]),int(birthday[1]),int(birthday[0]))
        now = datetime.date(now.year, now.month, now.day)
        delta = now - then
        delta = delta.days
        if delta < 0:
            print("you're gonna be born in", delta*(-1), "days")
        elif delta > 0:
            print("you've lived", delta, "days")
            print("you've lived", delta//30, "months", delta%30, "days")
            print("you've lived", delta//30//12, "years", (delta//30)%12, "months", delta%30, "days")
        break
    else:
        print('wrong date format')
		
		

	

