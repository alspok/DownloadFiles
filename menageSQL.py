from Classes.MenageSQL import MenageSQL

def menageSQL() -> None:
    conn = MenageSQL().connectDB()

    pass

if __name__ == '__main__':
    menageSQL()