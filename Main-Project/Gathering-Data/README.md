if you want to run code, please run this command in terminal/command prompt

Your config.py file must be inside of the ./Main-Project/Gathering-Data/ folder.

Inside of the config.py file is mention in below


	config = {
		"email":"example@example.com",
		"password":"example",
		"apikey":"example-apikey"
	}

apikey is used to gather data from "https://uts-ws.nlm.nih.gov/rest/content/", you can look this link(https://documentation.uts.nlm.nih.gov/rest/search/)
email and password is used to enroll to the Disgenet, you can look this link(https://www.disgenet.org/api/).


if you want to gather Disgenet informations, you should this command that mentioned in below.
***python gather_gene_disease_information.py***

if you want to gather diseases informations, you should this command that mentioned in below.
***python gather_disease_data_from_umls.py***


*	Note: python keyword call Python3 *