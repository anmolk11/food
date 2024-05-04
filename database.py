import sqlite3

def insert_item(item : str,type : str) -> None:
    try:
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        insert_query = "INSERT INTO food_items (item,type) VALUES (?,?)"
        cursor.execute(insert_query, (item,type,))
        conn.commit()
        print("Items inserted successfully!")

    except sqlite3.Error as e:
        print("Error:", e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    week_days = ['Sev Tamatar','Ballor','Poha','Gawar Phali','Gobhi','Allu - Dry','Allu - Liquid','Khichdi','Sabudana','Kadhi','Baingan','Karela']
    week_end = ['Daal Bati/Bafla','Paneer','Allu Paratha']

    for item in week_days:
        insert_item(item,'WD')
    for item in week_end:
        insert_item(item,'WE')



