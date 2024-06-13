# Gathering-Data
This part is used to gather information from UMLS and DisGeNet via using API. 

:warning:

DisGeNet API is not available at this moment. Please use source files in source-files folder. 

:warning:

Before run this programs, you must build config.py file that store required information when access UMLS and DisGeNet API.

Apikey is required to access [UMLS](https://uts-ws.nlm.nih.gov/rest/content/) server. Apikey is used to gather data from [UMLS](https://uts-ws.nlm.nih.gov/rest/content/) server, you can research in this [documentation](https://documentation.uts.nlm.nih.gov/rest/search/)

Email and password is used to enroll to the Disgenet, you can research in this [documentation](https://www.disgenet.org/api/).

:warning:

Your config.py file must be inside of the ./Main-Project/Gathering-Data/ folder.

:warning:

Inside of the config.py file is mention in below

	config = {
		"email":"example@example.com",
		"password":"example",
		"apikey":"example-apikey"
	}


:warning:


if you want to gather DisGeNet informations, you should this command that mentioned in below.
```
	python3 gather_gene_disease_information.py
```

---


if you want to gather diseases informations from UMLS, you should this command that mentioned in below.

```
	python3 gather_disease_data_from_umls.py
```



:warning:

***python*** keyword is used to call ***python3*** in some machines. If your machine is like that, you can change ***python3*** keyword with ***python*** keyword.