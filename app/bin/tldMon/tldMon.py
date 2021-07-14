import requests, urllib.request, time, zipfile, os, os.path, glob, base64, sys
from datetime import datetime, timedelta
# Uncomment for HTML Scrape method
# from bs4 import BeautifulSoup

#----------------------------------------------------------------------
def remove(path):
    """
    Remove the file or directory
    """
    if os.path.isdir(path):
        try:
            os.rmdir(path)
        except OSError:
            print ("Unable to remove folder: "+path)
    else:
        try:
            if os.path.exists(path):
                os.remove(path)
        except OSError:
            print ("Unable to remove file: "+path)
#----------------------------------------------------------------------
def cleanup(number_of_days, path):
    """
    Removes files from the passed in path that are older than or equal 
    to the number_of_days
    """
    time_in_secs = time.time() - (number_of_days * 24 * 60 * 60)
    for root, dirs, files in os.walk(path, topdown=False):
        for file_ in files:
            full_path = os.path.join(root, file_)
            stat = os.stat(full_path)
            
            if stat.st_mtime <= time_in_secs:
                remove(full_path)
#       Delete empty folder
#        if not os.listdir(root):
#            remove(root)
            
#----------------------------------------------------------------------

url = 'https://whoisds.com//whois-database/newly-registered-domains/<datezip>/nrd'
dts = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
url = url.replace('<datezip>',str(base64.b64encode( (dts+'.zip').encode("utf-8")), "utf-8") )

# response = requests.get(url)
# print(str(response.status_code)+' '+url)

domains = ''
pwdir = '/app/dat/tldMon/'
zipf = pwdir+'nrd_'+dts+'.zip'
txtf = pwdir+'domain-names.txt'
out = pwdir+'nrd_'+dts+'.log'

cleanup(7, pwdir)

if not os.path.exists(out):
    zip = requests.get(url)
    if zip.status_code == 200:
        with open(zipf,'wb') as f:
            f.write(zip.content)

        with zipfile.ZipFile(zipf, 'r') as zr:
            zr.extractall(pwdir)

        with open(txtf, 'r') as fr:
            domains += fr.read()

        os.remove(zipf)
        os.remove(txtf)
        if domains:
            with open(out,'w') as fw:
                fw.write(domains)
            # print(domains)




# Uncomment for HTML Scrape method
# url = 'https://whoisds.com/newly-registered-domains'
# response = requests.get(url)
# if response.status_code == 200:
	# soup = BeautifulSoup(response.text, "html.parser")
	# tables = soup.findAll('table')
	# pwdir = '/app/tldmon/'
	# out = pwdir+'nrd_'+datetime.now().strftime("%Y%m%d")+'.log'
	# for idx, t in enumerate(tables):
		# if 'Newly Registered Domains Free Download' in str(tables[idx]):
			# links = tables[idx].findAll('a')
			
			# domains = ''
			# for jdx, l in enumerate(links):
				# #IF there are no other log files it assumes first run
				# #on first run retrieve all lists.
				# if (glob.glob(pwdir+'nrd_*.log')) and (jdx > 0):
					# break
				
				# #Only need to gather once a day
				# if not os.path.exists(out):
					# # print(l.get('href'))
					
					# zipf = pwdir+'nrd_'+str(jdx)+'_'+datetime.now().strftime("%Y%m%d")+'.zip'
					# txtf = pwdir+'domain-names.txt'
					
					# zip = requests.get(l.get('href'))
					
					# with open(zipf,'wb') as f:
						# f.write(zip.content)
					
					# with zipfile.ZipFile(zipf, 'r') as zip_ref:
						# zip_ref.extractall(pwdir)
						
					# with open(txtf, 'r') as fr:
						# if jdx > 0:
							# domains += "\n"
						# domains += fr.read()
					
					# os.remove(zipf)
					# os.remove(txtf)
				
			
			# #Prevent Overwrite
			# if not os.path.exists(out):
				# with open(out,'w') as fw:
					# fw.write(domains)
			# # print(domains)


