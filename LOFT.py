import datetime

STOP_CHECK_TIME = 210 # 3 часа 30 минут в минутах

WORKDAY = 'workday' #с пон по пт
WEEKEND = 'weekend' #сб и вс

STOPCHECKS = {
    WORKDAY: 350, 
    WEEKEND: 450 
}

workdays = [1,2,3,4,5]
weekend = [6,7]


def _get_price_from_time(time_spent,minutes_discount,percent_discount,items,day):
    if day in workdays:
    	return _get_price_from_workday(time_spent,minutes_discount,percent_discount)
    else:
    	return _get_price_from_weekend(time_spent,minutes_discount,percent_discount)



def _get_price_from_workday(time_spent,minutes_discount, percent_discount):
    assert minutes_discount < time_spent,\
    'Minutes discount is more than time spent'
    if time_spent >= STOP_CHECK_TIME + minutes_discount:
        return STOPCHECKS[WORKDAY]
    time_spent = time_spent - minutes_discount
    if time_spent > 60:
        time_spent -= 60
        price = time_spent * 1.5 + 120
    else:
        price = time_spent * 2
    return price * (1 - percent_discount/100)
        


def _get_price_from_weekend(time_spent, minutes_discount, percent_discount):
    assert minutes_discount < time_spent,\
      'Minutes discount is more than time spent'
    if time_spent >= STOP_CHECK_TIME + minutes_discount:
        return STOPCHECKS[WEEKEND]
    time_spent = time_spent - minutes_discount
    
    if time_spent >= 60:
        time_spent -= 60
        price = time_spent * 2 + 150
        return price * (1 - percent_discount / 100)
    else:
        price = time_spent * 2.5
        return price * (1 - percent_discount / 100)

   		 
def _get_price_from_items(items):
	return sum(int(item) * count for item, count in items.items())
    

def get_total(time_spent, minutes_discount, percent_discount, items, day):
    print('Cymma -',_get_price_from_time(time_spent, minutes_discount, percent_discount, items, day),'+',_get_price_from_items(items))

#--------------------------------------------------------------------------------***----------------------------------------------------------------------------------------
def test_for_total_price():
    return get_total(delta,min_discount,per_discount,TEST_ITEMS,num_week)

time_come = datetime.datetime(2017,12,16, 11,45,0)


print(time_come)
time_gone = datetime.datetime.now()

print(time_gone)
delta =time_gone - time_come

per_discount = 0

min_discount = 0

delta = delta.total_seconds()//60
print('Количество минут -',delta - min_discount)

num_week = time_come.isoweekday() #номер дня от 1 до 7
print('Номер дня недели -',num_week)

TEST_ITEMS = {
    '450': 0,
    '600': 0

}

test_for_total_price()




