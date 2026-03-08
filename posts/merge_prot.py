"""
merging to maximize diversity by removing anyhting above >70% identity
want to capture a broader range of peptide; capture the breadth of the diversity 

"""



import glob, os, sys

def merge_prots(
    query_folder: str,
    out_folder: str,
    pid: float = 0.7,
    threads: int= 4
    ) -> None:

    cd_hit_cmd = f'cd-hit -G 0 -c (pid) -T (threads) -M 3000 -aS 1.0 -aL 0.005 ' \
        f'-i {query_fasta} -o {out_fasta}'
 
    os.system(cd_hit_cmd)

def merge_many(
        query_dir: str,
        out_dir: str,
        pid: float = 0.7,
        threads: int = 4
        ) -> None:
    
    query_fasta_files = glob.glob(f'{query_dir}/*.fa*')
    print(len(query_fasta_files))

    for fasta in query_fasta_files:
        print(fasta)
        out_fasta = f'{fasta.replace(query_dir, out_dir).rpartition(".")[0]}.{int(pid*100)}pid.Clustered.fasta'
  
        merge_prots(
            fasta,
            out_fasta,
            pid,
            threads
            )    
  
if __name__ == '__main__':
    try:
        query_dir = sys.argv[1]
        out_dir = sys.argv[2]

    except:
        print('\nUsage:\n\n python3 merge_prots.py [Query-DIR] [OUTPUT-DIR]\n\n')
        sys.exit(1)

    merge_many(
        query_dir,
        out_dir,
        0.7,
        4
        )