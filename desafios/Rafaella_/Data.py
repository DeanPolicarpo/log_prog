#1
from datetime import date, timedelta
hj= date.today()
#2 dias depois
dps= hj+ timedelta(days=2)
print(dps.strftime('%d/%m/%y'))

#2
from datetime import date, timedelta
hj= date.today()
print(hj.strftime('%d/%m/%y'))