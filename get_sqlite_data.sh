#!/bin/bash

db_path="./db.sqlite3"
table_name="blog_post"

# take all tables
all_tables_query="SELECT name FROM sqlite_master WHERE type='table';"
all_tables=$(sqlite3 "$db_path" "$all_tables_query")

# take names of column
columns_sql_query="PRAGMA table_info($table_name);"
column_names=$(sqlite3 "$db_path" "$columns_sql_query")

# take a table data
table_data_sql_query="SELECT * FROM $table_name;"
table_data=$(sqlite3 "$db_path" "$table_data_sql_query")

echo "all tables in sqlite_master:"
echo -e "$all_tables\n"

echo -e "column names for table $table_name:\n"
echo "$column_names"

echo -e "\ndata from $table_name table:\n"
echo "$table_data"