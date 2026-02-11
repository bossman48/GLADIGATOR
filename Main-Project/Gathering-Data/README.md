# Gathering-Data: Data Collection

## Overview
This component gathers data from various sources using APIs and processes it for graph construction.

### Data Sources:
- **DisGeNET**: Gene-disease associations via API
- **UMLS**: Disease information via API
- **BioGrid**: Gene-gene associations
- **UniProt**: Protein sequence information

### Important Notes
:warning: **DisGeNET API is currently unavailable**. Please use source files in the `source-files` folder instead. :warning:

## Configuration
Before running the data gathering programs, you must create a `config.py` file that stores required information for accessing UMLS and DisGeNET APIs.

### API Requirements
- **UMLS**: Apikey is required to access [UMLS](https://uts-ws.nlm.nih.gov/rest/content/) server. You can research in this [documentation](https://documentation.uts.nlm.nih.gov/rest/search/)
- **DisGeNET**: Email and password are used to enroll to DisGeNET. You can research in this [documentation](https://www.disgenet.org/api/)

### Config File Location
:warning: Your `config.py` file must be inside of the `./Main-Project/Gathering-Data/` folder. :warning:

### Config File Structure
Inside of the `config.py` file, include the following:

```python
config = {
    "email": "example@example.com",
    "password": "example",
    "apikey": "example-apikey"
}
```

## Commands
### Gather DisGeNET Information
```bash
python3 gather_gene_disease_information.py
```

### Gather UMLS Disease Information
```bash
python3 gather_disease_data_from_umls.py
```

## Important Notes
- ***python*** keyword is used to call ***python3*** in some machines. If your machine is like that, you can change ***python3*** keyword with ***python*** keyword.