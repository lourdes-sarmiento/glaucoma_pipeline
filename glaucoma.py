import pandas as pd
glaucoma_genes=["MYOC","CYP1B1","FOXC1","PITX2","TBK1","OPTN"]
def load_vcf(vcf_file):
    """Carga un archivo VCF y lo convierte en un DataFrame de pandas."""
    df=pd.read_csv(vcf_file, sep='\t', comment='#', header=None)
    df.columns=['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']
    return df
