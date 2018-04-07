# Store-ipfs
A python script to store our contect over distributed decentralised netowrk using ipfs.

What is IPFS?

From Wikipedia:

InterPlanetary File System (IPFS) is a protocol and network designed to create a content-addressable, peer-to-peer method of storing and sharing hypermedia in a distributed file system. 
IPFS was initially designed by Juan Benet, and is now an open-source project developed with help from the community.
In simple it’s Amazon S3 on Blockchain. All of your information is available on decentralized network across nodes thus not only make the system scaleable but reliable as well since data which is fed in it will be there hence no chance of 404-File not found kind of errors.
So there can be many possibilities how you can use it, essentially for file storage, you can use as web hosting, for messaging system, possibilities are endless.

Installation:
Download the setup file from https://dist.ipfs.io/#go-ipfs
run to check if installed correctly :  ipfs --version
Now, initialise ur machine to use ipfs using : ipfs init
You'll get a key, save it....
by Use : ipfs daemon , You can have a web interface by visiting http://localhost:8080/ipfs by adding Hash of the file object
when you run ipfs refs local it prints the content exist on your local node

When you post a file on IPFS network, it’s spread across the connected nodes. IPFS provides garbage collection concept which eventually let the files get deleted. Or, if your node goes offline and not synced the data will be lost. In order for your data stay there forever, you pin your file by running the command:

ipfs pin add <hash_of_content> where hash of content are the entries you see above. When you do it, it’s not removed due to garbage collection process. You can also unpin by running ipfs pin rm <hash_content>

ipfsapi is python wrapper for the same, for more info visit:
https://github.com/ipfs/py-ipfs-api

