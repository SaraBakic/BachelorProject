# Bachelor project

This repository contains tasks that should be completed within the scope of Bachelor project. The project will be divided into several phases, each with a specific set of tasks. You should create your branch and push your solutions to given tasks to a folder **solutions** in your branch.
 
## Phase 1

First phase focuses on getting familiar with basic concepts and data formats used in bioinformatics. Students should complete a set of several smaller tasks as part of this phase.
The tasks include:
  * Parsing and analyzing FASTA and FASTQ files - Task related to this part is explained in subdirectory **1-FASTA-files**
  * Mapping a set of reads to a reference - Taks related to this part is explained in subdirectory **1-mapping**
  * Parsing and analyzing FAST5 files - Task related to this part is explained in subdirectory **1-FAST5-files**
  
  
The tasks are expected to be executed in linux environment, probably using remote servers. Files that should be of help for this are:
  * **Linux.txt**
  * **Servers.txt**
 

## Phase 2

In the second phase of the project you will be focusing on understanding the basics of current approaches to the detection of epigenetic modifications. 
Current approaches are based on two sequencing technologies, WGBS (Whole Genome Bisulfite Sequencing) and ONT (Nanopore sequencing technology). To understand the pipelines of both approaches you will be reading and summarizing three topics:
 * [DNA Methylation and its basic function] (https://www.nature.com/articles/npp2012112)
   * This paper gives an introduction to a group of epigenetic modifications you will be focusing in the beginning
   * The information you should learn from this paper is the concept of methylation and where it occurs (i.e., what are CpG sites and islands)
   * I **do not** expect you to go into deep biological and chemical details
 * [An introduction to WGBS] (https://en.wikipedia.org/wiki/Bisulfite_sequencing)
   * Since most of scientific papers in this area are heavily biologically based, I believe this will give you a sufficient overview
   * I expect you go through sections: Introduction, 1.1.1, 1.2, 2, 3, 4
 * [DNA methylation-calling tools for Oxford Nanopore sequencing: a survey and human epigenome-wide evaluation] (https://genomebiology.biomedcentral.com/articles/10.1186/s13059-021-02510-z)
   * This paper gives an overview of approaches based on ONT Nanopore technology
   * I expect you to read first 9 pages of the paper, up to section "Benchmark datasets" (not included) to get a sense of the pipeline and existing tools
 
 
After reading the given literature, write a short summary of what you've read, shortly list what you've learned and note down the questions you have after reading these papers. Upload a pdf with the summaries to the repository.
