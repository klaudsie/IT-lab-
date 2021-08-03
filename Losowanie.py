import psycopg2  #w cmd: pip install psycopg2-binary
from random import sample


conn = psycopg2.connect(
    host="kandula.db.elephantsql.com",
    database="tgrsoqqq",
    user="tgrsoqqq",
    password="ZODczqSesusc57IK_b5ngYgaZpGRTenH"
)

cursor = conn.cursor()

cursor.execute('select count(*) from "Rodzina"')
result = cursor.fetchone()
res1 = int(''.join(map(str, result)))

cursor.execute('select count(*) from "Czas wolny"')
result = cursor.fetchone()
res2 = int(''.join(map(str, result)))

cursor.execute('select count(*) from "Obowiązki domowe"')
result = cursor.fetchone()
res3 = int(''.join(map(str, result)))

cursor.execute('select count(*) from "Pieniądze"')
result = cursor.fetchone()
res4 = int(''.join(map(str, result)))

cursor.execute('select count(*) from "Fizyczna bliskość"')
result = cursor.fetchone()
res5 = int(''.join(map(str, result)))

SAMPLE_rodz = sample(range(1, res1), k=5)
varr1, varr2, varr3, varr4, varr5 = SAMPLE_rodz
SAMPLE_czas = sample(range(1, res2), k=5)
varc1, varc2, varc3, varc4, varc5 = SAMPLE_czas
SAMPLE_obow = sample(range(1, res3), k=5)
varo1, varo2, varo3, varo4, varo5 = SAMPLE_obow
SAMPLE_pien = sample(range(1, res4), k=5)
varp1, varp2, varp3, varp4, varp5 = SAMPLE_pien
SAMPLE_fiz = sample(range(1, res5), k=5)
varf1, varf2, varf3, varf4, varf5 = SAMPLE_fiz

rows_rodz = cursor.execute(
    'SELECT "Pytanie" FROM "Rodzina" WHERE "id"=' + str(varr1) + 'OR "id"=' + str(varr2) + 'OR "id"=' + str(
    varr3) + 'OR "id"=' + str(varr4) + 'OR "id"=' + str(varr5) + ';')
rodzina = []
Rodzina = cursor.fetchall()
family = ' '.join([str(elem) for elem in Rodzina])
family = family.replace("('", "").replace("',)", "")
rodzina1, rodzina2, rodzina3, rodzina4, *rest = family.split('?')
*rest, rodzina5, none = family.split('?')
for i in range(1,6):
    globals()['rodzina%s' % i] = globals()['rodzina%s' % i] + str("?")

rows_rodz = cursor.execute(
    'SELECT "Pytanie" FROM "Pieniądze" WHERE "id"=' + str(varp1) + 'OR "id"=' + str(varp2) + 'OR "id"=' + str(
    varp3) + 'OR "id"=' + str(varp4) + 'OR "id"=' + str(varp5) + ';')
pieniadze = []
pieniadze = cursor.fetchall()
money = ' '.join([str(elem) for elem in pieniadze])
money = money.replace("('", "").replace("',)", "")
pieniadze1, pieniadze2, pieniadze3, pieniadze4, *rest = money.split('?')
*rest, pieniadze5, none = money.split('?')
for i in range(1,6):
    globals()['pieniadze%s' % i] = globals()['pieniadze%s' % i] + str("?")

rows_rodz = cursor.execute('SELECT "Pytanie" FROM "Obowiązki domowe" WHERE "id"=' + str(varo1) + 'OR "id"=' + str(
    varo2) + 'OR "id"=' + str(varo3) + 'OR "id"=' + str(varo4) + 'OR "id"=' + str(varo5) + ';')
obowiazki = []
obowiazki = cursor.fetchall()
duty = ' '.join([str(elem) for elem in obowiazki])
duty = duty.replace("('", "").replace("',)", "")
obowiazki1, obowiazki2, obowiazki3, obowiazki4, *rest = duty.split('?')
*rest, obowiazki5, none = duty.split('?')
for i in range(1,6):
    globals()['obowiazki%s' % i] = globals()['obowiazki%s' % i] + str("?")

rows_rodz = cursor.execute(
    'SELECT "Pytanie" FROM "Czas wolny" WHERE "id"=' + str(varc1) + 'OR "id"=' + str(varc2) + 'OR "id"=' +
    str(varc3) + 'OR "id"=' + str(varc4) + 'OR "id"=' + str(varc5) + ';')
czas = []
czas = cursor.fetchall()
time = ' '.join([str(elem) for elem in czas])
time = time.replace("('", "").replace("',)", "")
czas1, czas2, czas3, czas4,  *rest = time.split('?')
*rest, czas5, none = time.split('?')
for i in range(1,6):
    globals()['czas%s' % i] = globals()['czas%s' % i] + str("?")

rows_rodz = cursor.execute(
    'SELECT "Pytanie" FROM "Fizyczna bliskość" WHERE "id"=' + str(varf1) + 'OR "id"=' + str(varf2) + 'OR "id"=' +
    str(varf3) + 'OR "id"=' + str(varf4) + 'OR "id"=' + str(varf5) + ';')
bliskosc = []
bliskosc = cursor.fetchall()
nearness = ' '.join([str(elem) for elem in bliskosc])
nearness = nearness.replace("('", "").replace("',)", "")
bliskosc1, bliskosc2, bliskosc3, bliskosc4, *rest = nearness.split('?')
*rest, bliskosc5, none = nearness.split('?')
for i in range(1,6):
    globals()['bliskosc%s' % i] = globals()['bliskosc%s' % i] + str("?")
