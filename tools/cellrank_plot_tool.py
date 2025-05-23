# tools/cellrank_plot_tool.py
from server import mcp
import scanpy as sc
import cellrank as cr

@mcp.tool()
def plot_fate_probabilities(adata_path: str) -> None:
    """
    Generate and save fate probability plots.

    Args:
        adata_path: Path to the input .h5ad file
    """
    adata = sc.read_h5ad(adata_path)
    cr.pl.fate_probabilities(adata, same_plot=False, ncols=2, save="_fate.png")
