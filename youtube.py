# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:27:16 2020

@author: asus
"""

from apiclient.discovery import build 

# Arguments that need to passed to the build function 
DEVELOPER_KEY = "AIzaSyBIgaNGrZHf0bOh3VjdN67PtcYTBwYVrX0"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating Youtube Resource Object 
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
										developerKey = DEVELOPER_KEY) 


def youtube_search_location(query, max_results = 5): 
	
	# calling the search.list method to retrieve youtube search results 
	search_location= youtube_object.search().list(q =query, type ='video', 
										location ='36.8667295, 10.2978906', 
							locationRadius ='1000km', part = "id, snippet", 
										maxResults = max_results).execute() 
	
	# extracting the results from search response 
	results = search_location.get("items", []) 

	# empty list to store video metadata 
	videos = [] 
	
	# extracting required info from each result object 
	for result in results: 

		# video result object 
		videos.append(result["id"]["videoId"]) 
	video_ids = ", ".join(videos) 
	video_response = youtube_object.videos().list(id = video_ids, part ='snippet,recordingDetails').execute() 
		
	search_videos = [] 
	for video_result in video_response.get("items", []): 
		search_videos.append("% s, (% s, % s)" %(video_result["snippet"]["title"], 
						video_result["recordingDetails"]["location"]["latitude"], 
					video_result["recordingDetails"]["location"]["longitude"])) 

	print ("Videos:\n", "\n".join(search_videos), "\n") 
	
if __name__ == "__main__": 
	youtube_search_location('carrefour', max_results = 100) 
