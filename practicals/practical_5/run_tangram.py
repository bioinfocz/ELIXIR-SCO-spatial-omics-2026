# TANGRAM
# BM

import anndata as ad
import pandas as pd

spatial_wd = '/exports/humgen/bmanzato/spatial_workshop'

adata_sc = ad.read_h5ad(f"{spatial_wd}/SpaGE_data/sc_adata_1percent.h5ad")

genes = pd.read_csv(f"{spatial_wd}/abc_download_root/metadata/WMB-10X/gene.csv",index_col=0)
adata_sc.var = genes
# Reset the index to turn the current index into a column
adata_sc.var.reset_index(inplace=True)
adata_sc.var.set_index('gene_symbol', inplace=True)

adata_section = ad.read_h5ad(f"{spatial_wd}/abc_download_root/expression_matrices/Zhuang-ABCA-1/adata_section80.h5ad")


import tangram as tg

markers = list(set.intersection(set(adata_sc.var_names), set(adata_section.var_names)))

tg.pp_adatas(adata_sc, adata_section, genes=markers)

assert "training_genes" in adata_sc.uns
assert "training_genes" in adata_section.uns

print(f"Number of training_genes: {len(adata_sc.uns['training_genes'])}")

ad_map = tg.map_cells_to_space(
    adata_sc,
    adata_section,
    mode="cells",
    density_prior="rna_count_based",
    num_epochs=500,
    device="cuda:0",
)

ad_map.write_h5ad('/exports/humgen/bmanzato/spatial_workshop/ad_map_tangram.h5ad')

adata_section.write_h5ad('/exports/humgen/bmanzato/spatial_workshop/adata_section_tangram.h5ad')

ad_ge = tg.project_genes(adata_map=ad_map, adata_sc=adata_sc)

ad_ge.write_h5ad('/exports/humgen/bmanzato/spatial_workshop/ad_ge.h5ad')
















