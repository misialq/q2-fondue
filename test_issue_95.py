# ----------------------------------------------------------------------------
# Copyright (c) 2022, Bokulich Laboratories.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import time

from qiime2.plugins import fondue

from qiime2 import Artifact


LOG_LEVEL = 'TRACE'
EMAIL = "mziemski@ethz.ch"

def run_main():
    ids = Artifact.import_data(
        "NCBIAccessionIDs", "ids-small.tsv"
    )

    print("Fetching sequences (1)...")
    seqs = fondue.methods.get_sequences(
        accession_ids=ids,
        email=EMAIL,
        n_jobs=7,
        n_fasterq_jobs=2,
        log_level=LOG_LEVEL,
        mode="large",
    )
    del seqs
    time.sleep(300)

    print("Fetching sequences (2)...")
    seqs = fondue.methods.get_sequences(
        accession_ids=ids,
        email=EMAIL,
        n_jobs=9,
        n_fasterq_jobs=4,
        log_level=LOG_LEVEL,
        mode="large",
    )
    del seqs
    time.sleep(300)

    print("Fetching sequences (3)...")
    seqs = fondue.methods.get_sequences(
        accession_ids=ids,
        email=EMAIL,
        n_jobs=7,
        n_fasterq_jobs=1,
        log_level=LOG_LEVEL,
        mode="large",
    )
    del seqs
    time.sleep(300)

    print("Fetching sequences (4)...")
    seqs = fondue.methods.get_sequences(
        accession_ids=ids,
        email=EMAIL,
        n_jobs=6,
        n_fasterq_jobs=1,
        log_level=LOG_LEVEL,
        mode="regular",
    )


if __name__ == "__main__":
    run_main()
