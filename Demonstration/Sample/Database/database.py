import time, random
from .utils import generate_password, STYLE, write_in
from .GracefulInterruptHandler import GracefulInterruptHandler

class AdminCredentials:
    def __init__(self, username: str = "admin", password: str = None):
        self.username = username
        self.password = password if password else generate_password(12)

class Database:
    def __init__(self,
                 admin: AdminCredentials = AdminCredentials(),

                 shards: int = 512,
                 page_size: int = 4096,

                 read_heads: int = 12,
                 write_heads: int = 12,

                 l1cache: int = 128,
                 l2cache: int = 128,

                 backup: int = 24 * 7,

                 sequential_write: int = False
                ):
        self.admin = admin

        self.shards = shards
        self.page_size = page_size

        self.read_heads = read_heads
        self.write_heads = write_heads

        self.l1cache = l1cache
        self.l2cache = l2cache

        self.backup = backup

        self.sequential_write = sequential_write

    def serve(self, host = "127.0.0.1", port = 8000):
        print( "[!] Loading Database Configuration...")

        print(f"[i] Shards: {write_in(self.shards, 'M', style=[STYLE.OKBLUE])}")
        print(f"[i] Page Size: {write_in(self.page_size, 'M', style=[STYLE.OKBLUE])}")
        print(f"[i] Read Head: {write_in(self.read_heads, 'M', style=[STYLE.OKBLUE])}")
        print(f"[i] Write Head: {write_in(self.write_heads, 'M', style=[STYLE.OKBLUE])}")
        print(f"[i] L1 Cache: {write_in(self.l1cache, 'M', style=[STYLE.OKBLUE])}")
        print(f"[i] L2 Cache: {write_in(self.l2cache, 'M', style=[STYLE.OKBLUE])}")
        print(f"[i] Backup Policy: {write_in('Every', self.backup, 'Hours', style=[STYLE.OKBLUE])}")
        if self.sequential_write:
            print(f"[w] {STYLE.WARNING}Sequential Write is \"Enabled\"{STYLE.ENDC}")

        print( "[!] Loading Admin Account...")
        print(f"[i] Admin [{write_in(self.admin.username, style=[STYLE.OKBLUE])}@{write_in(self.admin.password, style=[STYLE.HEADER])}]")

        print(f"[+] Database started listening at {host}:{port}")
        print(f"[ ] ===== Database Logs =====")

        with GracefulInterruptHandler() as sig:
            while not sig.interrupted:
                try:
                    time.sleep(random.randint(1, 500) / 100)
                    print(
                        random.choice(
                            [
                                "[+] New Row Added",
                                "[=] Row Updated",
                                "[-] Row Deleted",
                                f"{STYLE.FAIL}[x] Row Not Found{STYLE.ENDC}",
                                f"{STYLE.FAIL}[x] Login Credential Mismatch{STYLE.ENDC}",
                            ]
                        )
                    )
                except KeyboardInterrupt as kex:
                    pass
        print("[i] Database is gracefully shutting down...")