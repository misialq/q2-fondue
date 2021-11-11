# q2-fondue 
![CI](https://github.com/bokulich-lab/q2-fondue/actions/workflows/ci.yml/badge.svg)

## Installation

Before q2-fondue is available *via* conda, you can use the following instructions to install it on your machine into an existing conda environment:

* Create and activate a conda environment with the required dependencies:
```shell
conda create -y -n fondue \
   -c qiime2 -c conda-forge -c bioconda -c defaults \
  qiime2 q2cli q2-types "entrezpy>=2.1.2" "sra-tools==2.9.6" xmltodict "tzlocal==2.1"

conda activate fondue
```
* Install q2-fondue and refresh the QIIME 2 CLI cache. 
```shell
pip install git+https://github.com/bokulich-lab/q2-fondue.git

qiime dev refresh-cache
```

The current q2-fondue version supports QIIME 2 **v2021.4** or higher.


## Usage
### Fetching metadata

To fetch metadata associated with a number of run or project IDs, execute the following command:

```shell
qiime fondue get-metadata \
              --m-accession-ids-file metadata_file.tsv \
              --p-n-jobs 1 \
              --p-email your_email@somewhere.com \
              --o-metadata output_metadata.qza
```

where:
- `--m-accession-ids-file` is a TSV containing run or project IDs
- `--p-n-jobs` is a number of parallel download jobs (defaults to 1)
- `--p-email` is your email address (required by NCBI)
- `--o-metadata` is the output metadata artifact

The resulting artifact will contain a TSV file containing all the available metadata fields
for all of the requested runs.

### Fetching sequences

To get single-read and paired-end sequences associated with a number of run or project IDs, execute this command:
```shell
qiime fondue get-sequences \
              --m-accession-ids-file metadata_file.tsv \
              --p-email your_email@somewhere.com \
              --o-single-reads output_dir_single \
              --o-paired-reads output_dir_paired
```

where:
- `--m-accession-ids-file` is a TSV containing run or project IDs
- `--p-email` is your email address (required by NCBI)
- `--o-single-reads` is the output artifact containing single-read sequences
- `--o-paired-reads` is the output artifact containing paired-end sequences

The resulting artifact will contain the `fastq.gz` files of the sequences, `metadata.yml` and `MANIFEST` files. If one of the provided IDs only contains sequences of one type (e.g. single-read sequences) then the other artifact (e.g. artifact with paired-end sequences) contains empty sequence files with dummy ID starting with `xxx_`.

### Fetching metadata and sequences

To fetch both sequence-associated metadata and sequences associated with the provided run or project IDs, execute this command:

```shell
qiime fondue get-all \
              --m-accession-ids-file metadata_file.tsv \ 
              --p-email your_email@somewhere.com \
              --output-dir output-dir-name
```
where:
- `--m-accession-ids-file` is a TSV containing accession numbers for all of the runs
- `--p-email` is your email address (required by NCBI)
- `--output-dir` directory where the downloaded metadata and sequences are stored as QIIME 2 artifacts

## License

q2-fondue is released under a BSD-3-Clause license. See LICENSE for more details.
