from pathlib import Path
import sys

p = Path(__file__).parent
sys.path.insert(0, str(p))

import user

if __name__ == "__main__":
    app = user.Application()
    app.start()
