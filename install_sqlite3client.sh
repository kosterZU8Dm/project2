if command -v sqlite3 >/dev/null 2>&1; then
    echo "SQLite3 is already installed"
else
    echo "SQLite3 is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install sqlite3
fi
