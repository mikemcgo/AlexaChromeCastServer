### Developer: Mike McGookey

### Features:
  - This project is the the server application intended to be paired with AlexaChromeCastExtension
  - This server accepts post/put requests of twitch and youtube content ids so that they can be push to the chomecast by an alexa command
  - The server uses a redis instance to store data, providing durability on machine shutdown

thoughts
	name lists in redis with *-list (can be retrieved with keys *-list) lpush, lrange
	same for machines *-machines - http://stackoverflow.com/questions/32276493/how-to-store-and-retrieve-a-dictionary-with-redis - hmset, hgetall
	change password on redis config
	maybe make password dynamic/random on installation?
