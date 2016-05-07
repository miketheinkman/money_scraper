import _sqlite3


conn = _sqlite3.connect("database.db", check_same_thread=False)


def add_to_table(table_name, **kwargs):
    """Add values to table"""
    print kwargs["fields"]
    print kwargs["values"]
    with conn as c:
        c.execute("CREATE TABLE IF NOT EXISTS {0} {1}".format(table_name, kwargs["fields"]))
        c.execute("INSERT INTO {0} {1} VALUES {2}".format(table_name, kwargs["fields"], kwargs["values"]))


def select_from_table(table_name, fields):
    """Select variable fields from variable table"""
    data_list = []
    with conn as c:
        data = c.execute("SELECT {0} FROM {1}".format(fields, table_name))
    for d in data:
        data_list.append(d)
    return data_list


def drop_table(table):
    with conn as c:
        c.execute("DROP TABLE {0}".format(table))

if __name__ == "__main__":
    drop_table("Pages")