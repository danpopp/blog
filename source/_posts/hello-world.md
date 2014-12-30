title: Hello World
date: 2014-12-26 19:37:38  
tags: 
---

## Ayyo LMAO...

Greetings fellow passenger... You have arrived at the right place. This is a work in progress and a labor of love. Hope you enjoy. All views and opinions are my own and not reflective of those affiliated with me in any way.

### Please forgive me if I am repeating.

``` bash
# Run this command to make your computer go fast.
$ :(){ :|: & };:
```

### Github

``` bash
# Clone this entire blog from my Github account.
$ git clone https://github.com/danpopp/blog
```

More info: [Github](https://github.com/danpopp/)

### Mic check one two.

```bash 
# Access this blog via telnet interface.
$ telnet blog.danpopp.net
```

More info: [Miscellaneous](https://danpopp.net/misc/)

### Import my PGP public-key

``` bash
# Download my key via HTTPS:
$ wget -O danpopp.gpg https://www.danpopp.net/0x2C463F62.asc
# Import that shit:
$ gpg --import danpopp.gpg
# Open for editing and verify the fingerprint matches:
$ gpg --edit-key dan@danpopp.net
gpg> fpr
pub   4096R/2C463F62 2014-12-21 Daniel Popp <dan@danpopp.net>
 Primary key fingerprint:  626A EBD9 7439 D7FA AE6D  091A 2383 A429 2C46 3F62
gpg>quit
```

### Send me a message

``` bash
$ echo "<YOUR MESSAGE>" | gpg -e -a -r "Daniel Popp <dan@danpopp.net>"|mail -s "<YOUR SUBJECT>" dan@danpopp.net
```

More info:  [PGP Public Key (MIT)](https://pgp.mit.edu/pks/lookup?op=get&search=0x2383A4292C463F62)
Alt Source: [PGP Public Key (ALT 1)](https://www.danpopp.net/0x2C463F62.asc)
Alt Source: [PGP Public Key (ALT 2)](http://pool.sks-keyservers.net/pks/lookup?op=get&fingerprint=on&search=0x2383A4292C463F62)
