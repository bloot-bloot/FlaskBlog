CREATE TABLE IF NOT EXISTS products(  -- products-  таблица созданная в SQL

    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    name TEXT NOT NULL UNIQUE,
    quan FLOAT NOT NULL,
    quan_metric TEXT NOT NULL, 
    exp_data DATE NOT NULL,
    frige_id INTEGER,

    FOREIGN KEY(frige_id) REFERENCES frige(id) -- связование по внешнему ключу ( frige_id  теперь связан с id таблицы frige)
);
CREATE  IF NOT EXISTS frige(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT,
    type INTEGER CHECK( type IN (1,2)) NOT NULL DEFAULT 2  -- 1 - морозильная камера, 2 - холодильник.
);

CREATE TABLE IF NOT EXISTS group_products(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL UNIQUE);
