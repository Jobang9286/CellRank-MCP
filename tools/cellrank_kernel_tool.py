# tools/cellrank_kernel_tool.py
from server import mcp
import scanpy as sc
import cellrank as cr

@mcp.tool()
def compute_cellrank_kernel(adata_path: str) -> str:
    """
    Compute CellRank transition kernel and save it to .uns.

    Args:
        adata_path: Path to the input .h5ad file

    Returns:
        Path to the updated AnnData object
    """
    adata = sc.read_h5ad(adata_path)
    kernel = cr.tl.kernels.CFLAREKernel(adata).compute_transition_matrix()
    adata.uns["cellrank_kernel"] = kernel.transition_matrix
    out_path = adata_path.replace(".h5ad", "_kernel.h5ad")
    adata.write(out_path)
    return out_path