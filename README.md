#  WHO phylogenies from Sep 2019 - Feb 2020

### Folders' map

Main folder contains all the jupyter notebook files (`*.ipynb`) and the general report. For Yamagata there are two old notebooks (2019b) because the final file was the merger of both.

- `h1_2020a/`: H1N1 files. It contains python scripts to prepare the data.
  - `treesub/`. treesub output (not included in the repository except the jupyter notebook required files).
- `h3_2020a/`: H3N2 files. 
- `vic_2020a/`: Victoria files.
- `yam_2020a/`: Yamagata files.
- `data/`: json dictionaries with styles used.
- `gisaid/`: Files downloaded from Gisaid. Not included because it can't have public access. However, acknowledgement tables are attached.
  - `*configuration_gisaid/`. Screenshot of the Gisaid website.
  
 ### Steps:
 
  1.Download data and references from Gisaid. Remove duplicates (in case egg&cell samples, normally we select only egg).
  
  2.Receive metadata from WHO. Prepare the table with the same structure (i.e. headers) than one of the csv's used for the last trees (e.g. h1_2020a/H1fortreelastHI_ready.csv). First column must contain the same IDs than the fasta.
  
  3.Run `1.checkIDrec.py`. It checks if all the records ID from the fasta are included in the metadata.
  
  4.Align fasta file (`mafft input_fasta > output_fasta`) and extract only the region of interest (e.g H1N1p GACACATTATG....TGTAGAATATGT).
  
  5.Run treesub. Generate subs.csv: `python 2.build_subs.py subsitutions.tsv subs.csv`.
  
  6.Run jupyter: `notebook jupyter` and format tree (fix size and positions is required).
  
  7.Final polishing using Illustrator.
  
  Optionally, RAxML and treesub can be run to optimize the likelihood of time-scaled phylogenies.
  
 ###  Dependences:
  
   - Baltic3 `https://github.com/Don86/baltic3`
   - automata `https://github.com/Don86/automata`
 
 ### Acknowledgements
  
  We gratefully acknowledge the authors, originating and submitting laboratories of the sequences from GISAID’s EpiFlu™ Database on which this research is based. 
  Shu, Y., McCauley, J. (2017) GISAID: Global initiative on sharing all influenza data – from vision to realityEuroSurveillance, 22(13) doi:10.2807/1560-7917.ES.2017.22.13.30494PMCID:PMC5388101
  
  -------------------------------------------------------------------------------------------------
  
Copyright (C) February/2020. Don Teng, Vijaykrishna Dhanasekaran and Miguel Grau Lopez. WHO Collaborating Centre for Reference and Research on Influenza.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
