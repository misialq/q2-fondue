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


def run_main():
    ids = Artifact.import_data(
        "NCBIAccessionIDs", "ids-small.tsv"
    )

    print("Fetching sequences (1)...")
    seqs = fondue.methods.get_sequences(
        accession_ids=ids,
        email="mziemski@ethz.ch",
        n_jobs=7,
        n_fasterq_jobs=2,
        log_level="TRACE",
        mode="large",
    )
    del seqs
    time.sleep(300)

    print("Fetching sequences (2)...")
    seqs = fondue.methods.get_sequences(
        accession_ids=ids,
        email="mziemski@ethz.ch",
        n_jobs=9,
        n_fasterq_jobs=4,
        log_level="TRACE",
        mode="large",
    )
    del seqs
    time.sleep(300)

    print("Fetching sequences (3)...")
    seqs = fondue.methods.get_sequences(
        accession_ids=ids,
        email="mziemski@ethz.ch",
        n_jobs=7,
        n_fasterq_jobs=1,
        log_level="TRACE",
        mode="large",
    )
    del seqs
    time.sleep(300)

    print("Fetching sequences (4)...")
    seqs = fondue.methods.get_sequences(
        accession_ids=ids,
        email="mziemski@ethz.ch",
        n_jobs=6,
        n_fasterq_jobs=1,
        log_level="TRACE",
        mode="regular",
    )


if __name__ == "__main__":
    run_main()
