# Name: اخبار المپیک
# URL:  https://quera.org/problemset/251439


from client import *

def message_callback(topic, message):
    print(f"Received message on topic {topic}: {message}")


server = OlympicsServer()

client = Client(server)

client.subscribe('sports/#', message_callback)

client.publish('sports/football', 'Football match result: Team A won!', qos=1)
client.publish('sports/football/worldcup', 'World Cup result: Team Z won!', qos=1)
client.publish('sports/basketball/nba', 'NBA result: Team Y won!', qos=1)

