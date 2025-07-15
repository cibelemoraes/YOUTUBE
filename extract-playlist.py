from googleapiclient.discovery import build


APIkey = "AIzaSyBQ4GOEz3BcqGZD35AjPO_eu4erINu07l0"  #chave da api do youtube

youtube = build('youtube', 'v3', developerKey=APIkey)
                
#criação da playlist

playlistId = 'PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj'
playlistName = 'Pop Music Playlist - Timeless Pop Songs'
nextPage_token = None

#listando os itens da playlist

playlistvideo = []

while True:
    response = youtube.plalistItems().list(part='snippet', playlistId= playlistId, maxResults= 50, pageToken=nextPage_token).execute()

    for item in response ['items']:
        snippet = item[' snippet']
        video_id = snippet[ 'resourceId']['videoId']


#chamando os dados dos videos

    video_response = youtube.videos().list(
        part='statistics',
        id=video_id
    ).execute()

    stats = video_response['items'][0]['statistics']
    