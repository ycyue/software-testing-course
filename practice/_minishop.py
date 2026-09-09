"""Start an isolated MiniShop for practice drills. Stdlib only; does not touch teaching data/."""

from __future__ import annotations

import logging
import sys
import tempfile
import threading
from http.server import ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MINISHOP = ROOT / "project" / "minishop"
if str(MINISHOP) not in sys.path:
    sys.path.insert(0, str(MINISHOP))

import server  # noqa: E402


class MiniShopLab:
    def __enter__(self) -> "MiniShopLab":
        self._tmp = tempfile.TemporaryDirectory()
        tmp = Path(self._tmp.name)
        self.db_path = tmp / "minishop.sqlite"
        self.log_path = tmp / "app.log"
        server.reset_db(self.db_path)
        server.configure_logging(self.log_path)
        server.MiniShopHandler.db_path = self.db_path
        server.MiniShopHandler.log_path = self.log_path
        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), server.MiniShopHandler)
        self.port = self.httpd.server_address[1]
        self.base_url = f"http://127.0.0.1:{self.port}"
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()
        return self

    def __exit__(self, *exc) -> None:
        self.httpd.shutdown()
        self.httpd.server_close()
        self.thread.join(timeout=2)
        logger = logging.getLogger("minishop")
        for handler in list(logger.handlers):
            handler.close()
            logger.removeHandler(handler)
        self._tmp.cleanup()
