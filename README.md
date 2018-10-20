# ScholarCitation4HugoAcademics

I created this based on a project which I do not remember now, but when I found it again on github I will properly cite it here.

This project is to put citation count button on your publications on webpages created with Hugo Academic them for HUGO.

To use it, follow the steps bellow:

--- The easy part ---

1 - copy the bin folder to your website root folder.
2 - Edit bin/build-site.sh and replace <SCHOLAR ID> by your own id. It apers on url https://scholar.google.com.br/citations?user=<SCHOLAR ID>&hl=en&authuser=1
  
3 - If you are using netlify, on site settings, build & deploy, set your build command to ./bin/build-site.sh.
This script will install some python packages, run a python script, which scraps google scholar and save a file named citecount.json. Then, the script move citecount.json to a folder named data on your repo.

4 - If you are not using netlify, you must run the extractscholar.py on your own. For this, just do: python extractscholar.py <SCHOLAR ID>. Remainds to use your scholar id as argument. Then, manually copy citecount.json to a data folder on your website root folder.
  
5 - Edit the file theme/academic/layouts/partials/publication_links.html and add the following lines in the end of the file:

{{ with $.Params.gs_id }}
	{{ range where $.Site.Data.citecount "id" "==" $.Params.gs_id }}
		{{ if ge .citecount 1 }}
			<a class="btn btn-outline-primary my-1 mr-1{{ if $is_list }} btn-sm{{end}}" href="{{ .url }}" target="_blank" rel="noopener">Cited by {{ .citecount }}</a>
		{{ end }}
	{{end}}
{{end}}

--- The boring part ---

6 - Edit each of your papers and add the paper id with the identifier of your paper on google scholar.

gs_id = "<paper id>"
To get the key of each paper open your google scholar page and using a javascript developer tool (ctrl + shift + c in firefox) read the url on each paper link.
  For instance:
  
  /citations?view_op=view_citation&hl=en&user=<scholar id>&authuser=1&citation_for_view=<scholar id>:<paper id>

For each paper with at least 1 citation you add the key on its md file, will appear a button link written Cited by <number>. This button is a link which opens a google scholar paper page.
  
I hope it can be useful for anyone!
