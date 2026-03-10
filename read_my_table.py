import boto3
from boto3.dynamodb.conditions import Key

REGION = "us-east-1"
TABLE_NAME = "Songs"

def get_table():
    #returns a reference to the dynamodb Music table

    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_song(song):
    #prints the song passed to it
    name = song.get("Name", "Unknown Title")
    artist = song.get("Artist", "Unknown Artist")

    print(f"  Name  : {name}")
    print(f"  Artist: {artist}")
    print()

def print_all_songs():
    #prints all songs in the table
    table = get_table()

    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No songs found. Make sure DynamoDB is connecter correctly and contains items")
        return
    
    print(f"Found {len(items)} song(s): \n")
    for song in items:
        print_song(song)

def main():
    print("=-=-=-=-= Reading from DynamoDB =-=-=-=-=\n")
    print_all_songs()

if __name__ == "__main__":
    main()