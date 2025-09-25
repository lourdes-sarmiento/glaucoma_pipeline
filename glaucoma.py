import pandas as pd
glaucoma_genes=["MYOC","CYP1B1","FOXC1","PITX2","TBK1","OPTN"]

def load_vcf(vcf_file):
    """Carga un archivo VCF y lo convierte en un DataFrame de pandas."""
    df=pd.read_csv(vcf_file, sep='\t', comment='#', header=None)
    df.columns=['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']
    return df

def filter_by_genes(df,genes):
    """Filtra variantes que contengan genes de interés en la columna INFO."""
    mask=df["INFO"].apply(lambda x: any(gene in x for gene in genes))
    return df[mask]

def save_results(df, output_file):
    """Guarda las variantes filtradas en un archivo TSV."""
    df.to_csv(output_file, sep='\t', index=False)

if __name__ == "__main__":
    #archivos de entrada y salida
    input_vcf="data/example.vcf"
    output_file="results/glaucoma_variants.csv"
    #cargar VCF
    print("Cargando archivo VCF...")
    vcf_df=load_vcf(input_vcf)
    #filtrar variantes  de genes asociados a glaucoma
    print("Filtrando variantes de genes asociados a glaucoma...")
    filtered_df=filter_by_genes(vcf_df, glaucoma_genes)
    #guardar resultados
    print(f"Guardando resultados en {output_file}...")
    save_results(filtered_df, output_file)
    print("Proceso Finalizado.")