# 0x03. Caching

# Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/r-LG3tieR1UO4LRlruYCuQ) , **without the help of Google**:

# General

## What a caching system is
* A caching system is a system that contains cashing algorithms that the hardware on the computer can be used to manage a cache of information on the computer.

## What FIFO means
* **FIFO**(First In First Out): This behaves the same way as a FIFO Queue without regard to how often or how many times they were accessed.

## What LIFO means
* **LIFO**(Last In First Out): this behaves the same as a LIFO in which cache events the block that is most recently added.

## What LRU means
* **LRU**(Least Recently Used): This discards the block that is the least recently Used. However, this requires that you keep track of what was used when, which is expensive if one wants to make sure the algorithm always discards the least recently used item.

## What MRU means
* **MRU**(Most Recently Used): This contrasts **LRU** because it discards the block that is the most recently been used. This is better for finding older items.

## What LFU means
* **LFU**(Least Frequently Used): This is similar to **LRU** but instead of storing a value of how recently the block was accessed we keep a count of how many times it was accessed.

## What the purpose of a caching system
* Caching systems are put in place to gain efficiency in terms of pulling data from a web server. The data is stored locally depending on the kind and is used to quickly access familiar elements on a web page without latency.

## What limits a caching system have
Caching systems are not great at keeping data long term.
Cache devices cannot be shared.
