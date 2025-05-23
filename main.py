# main.py
from server import mcp

from tools.cellrank_kernel_tool import compute_cellrank_kernel
from tools.cellrank_macrostates_tool import compute_macrostates
from tools.cellrank_fate_tool import compute_fate_probabilities
from tools.cellrank_plot_tool import plot_fate_probabilities

# MCP 서버 실행
if __name__ == "__main__":
    mcp.run()
