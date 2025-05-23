# tools/cellrank_macrostates_tool.py
from server import mcp
import scanpy as sc
import cellrank as cr

@mcp.tool()
def compute_macrostates(adata_path: str, n_states: int = 4) -> str:
    """
    Compute CellRank macrostates using GPCCA estimator.

    Args:
        adata_path: Path to the input .h5ad file
        n_states: Number of macrostates to identify

    Returns:
        Path to the updated AnnData object
    """
    adata = sc.read_h5ad(adata_path)
    kernel = cr.tl.kernels.CFLAREKernel(adata).compute_transition_matrix()
    estimator = cr.tl.estimators.GPCCA(kernel)
    estimator.compute_macrostates(n_states=n_states)
    estimator.write_to_adata()
    out_path = adata_path.replace(".h5ad", "_macrostates.h5ad")
    adata.write(out_path)
    return out_path