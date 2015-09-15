# budweiser

###Distributed file archiving state machine for messy directories

----

Ensuring N servers all mirror the same ever changing file system is handled perfectly by rsync. When compression is required accross the mirrors and files are renamed and metadata changed, shit gets messy. There are probably a hundred better ways to deal with the problem but this works for me.

- Subscribers communicate via Redis channels
- Each node keeps a current state (idle, compressing, collecting etc..)
- Nodes check state of it's peers by asking in the channel
- File system changes are turn based
- All peers must be idle for a job to start
- Nodes requesting changes whilst a peer is busy will go into a wait/pending state
- Verbose communication and state broadcasts allows peers to health check peers
- Sysadmins can monitor nodes via a realtime web interface (websockets)
