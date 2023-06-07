from Database.database import Database, AdminCredentials

syslog = Database(
    admin = AdminCredentials(
        username="AdminUser",
        password="MyRandomDummyPassword"
    ),
    shards = 128,
    page_size = 1024,
    read_heads = 6,
    write_heads=24,
    sequential_write = True
)

syslog.serve(
    host = "127.0.0.1",
    port=4444
)