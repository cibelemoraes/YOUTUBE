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
#adicionando dados adicionais dos videos
    
    playlistvideo.append({
        'id_video': video_id,
        'titulo': snippet['title'],
        'description': snippet['description'],
        'data_publicacao':snippet['publishedAt'],
        'thumbnail_url': snippet['thumnails']['hight']['url'],
        'Qt_likes': stats.get('Qt_likes', 0),
        'Qt_view': stats.get('Qt_view', 0),
        'Qt_comentarios': stats.get('Qt_comentarios', 0)
        })
    
    nextPage_token = response.get('nextpagetoken')
    if not nextPage_token:
        break

print("Total de vídeos da Playlist ", len(playlistvideo))