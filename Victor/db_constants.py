"""
Defines database entries/functions as formatable strings.
Add any frequently used database statements here, then use .format().
Values are not escaped in this file! (ie surrounded by ''), so the escape 
function defined here must be used instead.
example usage:
```
from db_constants import *
entry = VEHICLES_ENTRY.format(vin=1234, make=escape('Chevrolet'), model=escape('silverado'), year=1969, color=escape('hot pink'))
cursor.execute("INSERT INTO vehicles VALUES {}".format(entry))
```
"""

BIRTHS_ENTRY = "({regno},  {fname}, {lname}, {regdate}, {regplace}, {gender}, {f_fname}, {f_lname}, {m_fname}, {m_lname})"

PERSONS_ENTRY = "({fname}, {lname}, {bdate}, {bplace}, {address}, {phone})"

MARRIAGES_ENTRY = "({regno}, {regdate}, {regplace}, {p1_fname}, {p1_lname}, {p2_fname}, {p2_lname})"

VEHICLES_ENTRY = "({vin}, {make}, {model}, {year}, {color})"

REGISTRATIONS_ENTRY = "({regno}, {regdate}, {expiry}, {plate}, {vin}, {fname}, {lname})"

TICKETS_ENTRY = "({tno}, {regno}, {fine}, {violation}, {vdate})"

DEMERITNOTICES_ENTRY = "({ddate}, {fname}, {lname}, {points}, {desc})"

PAYMENTS_ENTRY = "({tno}, {pdate}, {ammount})"

USERS_ENTRY = "({uid}, {pwd}, {utype}, {fname}, {lname}, {city})"

def escape(string):
    return "'" + string + "'"