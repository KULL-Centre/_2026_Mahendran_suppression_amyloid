import pandas as pd
from argparse import ArgumentParser
import time
import numpy as np
import itertools
import glob
import difflib

def get_overlap(s1, s2):
    s = difflib.SequenceMatcher(None, s1, s2)
    pos_a, pos_b, size = s.find_longest_match(0, len(s1), 0, len(s2))
    sequence = ['-']*len(s1)
    sequence[pos_a:pos_a+size] = list(s1)[pos_a:pos_a+size]
    return ''.join(sequence),size

parser = ArgumentParser()
parser.add_argument('--batch',nargs='?',const='', type=int)
args = parser.parse_args()
batch = args.batch

t0 = time.time()

df_idrome = pd.read_csv('IDRome_DB.csv',index_col=0)

df_larks = pd.DataFrame(columns=['fasta_LARKS','fasta_IDRome','ndx_alignment',
                                 'score','seq','N_alignment','N_LARKS','f_LARKS','f_match'])

for filename in glob.glob('data/*.tsv')[batch:batch+200]:
    df = pd.read_csv(filename,sep='\t',header=None,
                     skiprows=1,index_col=0,
                     names=['tiles','C1','C2','C3','C4'])
    fasta_LARKS = pd.read_csv(filename,sep='\t').columns[0].upper()
    scores = []
    for seq_name in df_idrome.index:
        fasta_IDRome = df_idrome.loc[seq_name].fasta
        scores.append(get_overlap(fasta_LARKS, fasta_IDRome)[1])
    ndx_alignment = np.argmax(scores)
    fasta_IDRome = df_idrome.iloc[ndx_alignment].fasta
    seq, N_alignment = get_overlap(fasta_LARKS, fasta_IDRome)
    df_larks.loc[filename,'fasta_LARKS'] = fasta_LARKS
    df_larks.loc[filename,'fasta_IDRome'] = fasta_IDRome
    df_larks.loc[filename,'ndx_alignment'] = ndx_alignment
    df_larks.loc[filename,'score'] = np.max(scores)
    df_larks.loc[filename,'seq'] = seq
    df_larks.loc[filename,'N_alignment'] = N_alignment
    df['tiles_seq'] = [seq[i:i+6] for i in range(len(seq)-5)]
    df_matching_tiles = df[~df.tiles_seq.str.contains('-')]
    df_larks.loc[filename,'N_LARKS'] = df_matching_tiles.query('C2<4 or C3<10 or C4<-3').shape[0]
    df_larks.loc[filename,'f_LARKS'] = df_larks.loc[filename,'N_LARKS']/df_matching_tiles.index.size
    df_larks.loc[filename,'f_match'] = N_alignment/len(fasta_IDRome)

df_larks.to_csv(f'larks_{batch:d}.csv.gz')

print('Time: {:.3f} h'.format((time.time()-t0)/3600))
