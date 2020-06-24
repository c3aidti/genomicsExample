# genomicsExample

An interesting genomics task is producing a phylogenetic tree. In this example, we extract some Coronavirus genomes from the C3 COVID-19 Datalake and produce their phylogenetic tree.

## Python Implementation

Since the genomic sequences are available through the C3 Public API, we will first fetch the sequences through this interface, then use the ClustalW suite to perform multi-sequence-alignment, then some phylogenetics packages to build the phylogenetic tree.

To use the python implementation, either install all necessary packages listed in `env.yaml` or use `conda` to create an environment from this definition file with the command:

```
conda env create -f ./env.yaml -p ./venv
```

I've included a fully realized environment that I used to develop and test this example in the file `env-concrete.yaml`. That's here for future information and is not likely to work on your system as is. You may be able to delete a couple low level dependencies and conda may be able to solve a new environment for you though.

## C3 Implementation

Coming soon...
