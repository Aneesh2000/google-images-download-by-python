# importing google_images_download module 
from google_images_download import google_images_download 

# creating object 
response = google_images_download.googleimagesdownload() 
def downloadimages(query):
	# keywords is the search query
	# format is the image file format
	# limit is the number of images to be downloaded
	# print urs is to print the image file url
	# size is the image size which can
	# be specified manually ("large, medium, icon")
	# aspect ratio denotes the height width ratio
	# of images to download. ("tall, square, wide, panoramic")
	arguments = {"keywords": query,
				"format": "jpg",
				"limit":4,
				"print_urls":True,
				"size": "medium",
				"aspect_ratio": "panoramic"}
	try: 
		response.download(arguments) 
	
	# Handling File NotFound Error	 
	except FileNotFoundError: 
		arguments = {"keywords": query, 
					"format": "jpg", 
					"limit":4, 
					"print_urls":True, 
					"size": "medium"} 
					
		# Providing arguments for the searched query 
		try: 
			# Downloading the photos based 
			# on the given arguments 
			response.download(arguments) 
		except: 
			pass

#taking the word to be searched as user input
user_input = input("Enter a word to be searched : ")
downloadimages(user_input) 
