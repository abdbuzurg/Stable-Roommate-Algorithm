CHOICES = []
for i in range(10):
    CHOICES.append((i+1,str(i+1)))


COUNTRIES = tuple()
countries = ['Kyrgyzstan','Tajikistan','Kazakhstan']
for i in range(len(countries)):
    COUNTRIES += ((i,countries[i]),)

year = ['Preparatory','Freshman','Sophomore','Junior','Senior']
YEAR = ((0,'Preparatory'),(1,'Freshman'),(2,'Sophomore'),(3,'Junior'),(4,'Senior'))

sleep_time = ['9', '9:30', '10', '10:30','11', '11:30','12', '12:30','1', '1:30']
SLEEP_TIME = []
for i in range(len(sleep_time)):
    SLEEP_TIME.append((i,sleep_time[i]))

wake_time=['5','5:30','6','6:30','7','7:30','8','8:30','9','9:30']
WAKE_TIME = []
for i in range(len(wake_time)):
    WAKE_TIME.append((i,wake_time[i]))

SIZE = tuple()
size = ['XS','S','M','L','XL','XXL']
for i in range(len(size)):
    SIZE += ((i,size[i]),)

CAMPUSES = tuple()
campuses = ['Naryn','Khorog','Tekeli']
for i in range(len(campuses)):
    CAMPUSES += ((i,campuses[i]),)

gender = ['male', 'female']
