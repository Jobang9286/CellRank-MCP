# tools/cellrank_fate_tool.py
from server import mcp
import scanpy as sc
import cellrank as cr

@mcp.tool()
def compute_fate_probabilities(adata_path: str) -> str:
    """
    Compute fate probabilities and store them in adata.

    Args:
        adata_path: Path to the input .h5ad file

    Returns:
        Path to the updated AnnData object
    """
    adata = sc.read_h5ad(adata_path)
    kernel = cr.tl.kernels.CFLAREKernel(adata).compute_transition_matrix()
    estimator = cr.tl.estimators.GPCCA(kernel)
    estimator.compute_fate_probabilities()
    estimator.write_to_adata()
    out_path = adata_path.replace(".h5ad", "_fate.h5ad")
    adata.write(out_path)
    return out_path
