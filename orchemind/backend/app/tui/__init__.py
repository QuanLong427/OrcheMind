"""OrcheMind TUI — 全屏终端应用（textual 驱动）。

与 ``app/cli/``（传统滚动 CLI）并行。``orchemind chat`` 默认启动 TUI；
现有 CLI 路径可通过 ``--legacy`` 参数回退。

复用 ``app/services/stream_service.py`` 的 ``OrcheMindStreamClient`` + ``StreamEvent``
数据层，仅替换呈现层：StreamEvent → textual Widget 渲染。
"""

from orchemind.backend.app.tui.app import OrcheMindTUI

__all__ = ["OrcheMindTUI"]
