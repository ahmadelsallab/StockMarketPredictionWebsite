'''
Created on Aug 23, 2014

@author: Ahmad
'''

# Include the DataSift library
import datasift
 
# Create a client
client = datasift.Client('ahmad.elsallab', 'e26d3b4078106c2e8224bc042d7c7493')


# Declare a filter in CSDL, looking for content mentioning music
csdl = 'interaction.content contains "تاسي"'
#csdl = 'twitter.text contains "twitter"'
#csdl = 'twitter.text contains "مصر"'
 
# Compile the filter
fltr = client.compile(csdl)

# Open the log file
logFile = open('test_stream_1.txt', 'w', encoding='utf-8')
logFile.close()
logFile = open('test_stream_1.txt', 'w', encoding='utf-8')
# Handler: Message deleted by user
@client.on_delete
def on_delete(interaction):
    print("You must delete this to be compliant with T&Cs: ", interaction)
 
# Handler: Connection was closed
@client.on_closed
def on_close(wasClean, code, reason):
    print("Stream subscriber shutting down because ", reason)
 
# Handler: Picks up any error, warning, information messages from the platform
@client.on_ds_message
def on_ds_message(msg):
    print('DS Message %s' % msg)
 
# Handler: Connected to DataSift
@client.on_open
def on_open():
    print("Connected to DataSift")
    @client.subscribe(fltr['hash'])
    def on_interaction(interaction):
        print("Recieved interaction")       
        logFile.write("Recieved interaction: " + interaction['twitter']['text'] + '\n')
 
# Start streaming
#client.start_stream_subscriber()
#1408752000 = 23/8/2014 00:00:00
#client.historics_preview.create("fa10040e7593e93d0d0037c4033288db", 1408752000, 'twitter.text,wordCount,10', ['twitter'])
#client.historics_preview.create("fa10040e7593e93d0d0037c4033288db", 1408752000, "interaction.author.link,targetVol,hour;twitter.user.lang,freqDist,10;twitter.user.followers_count,numStats,hour;interaction.content,wordCount,10", ['twitter'])
client.historics_preview.create("fa10040e7593e93d0d0037c4033288db", 1408752000, "interaction.content,wordCount,10", ['twitter'])
