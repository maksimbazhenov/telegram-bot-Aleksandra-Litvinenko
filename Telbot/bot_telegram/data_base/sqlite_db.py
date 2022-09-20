import sqlite3 as sq
from create import bot

def sql_start():
    global base, cur
    base = sq.connect('car.db')
    cur = base.cursor()
    if base:
        print('База даных подключена')
    base.execute('CREATE TABLE IF NOT EXISTS PRICE_LIST (img TEXT, name TEXT PRIMARY KEY, discription TEXT, price TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO PRICE_LIST VALUES(?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * '
                           'FROM PRICE_LIST').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')


async def sql_read2():
    return cur.execute('SELECT * FROM PRICE_LIST').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM PRICE_LIST WHERE name==?',(data,))
    base.commit()