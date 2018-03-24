# Pcrd-Wiki

####Note
[Princess Connect Re:Dive Wiki Website On Azure](http://pcrd.azurewebsites.net) is synced with repo's master branch
and should be used only for develop.

[pcrxwiki.xyz](https://pcrxwiki.xyz) is the production site, updated manually by myself.

- Features:
  - [x] area map
  - [x] quest drop detail page
  - [x] equipment page
  - [ ] unit character page (avatar & skill data)
  - [ ] monsters page
  - [x] unit character equipment per rank
  - [ ] Beautify all pages
    
    
 ## For Developers
 
Database and static files are not contained in this repo, you should grab and plce it by yourself.

#### Database

Go to your android `/data/data/jp.co.cygames.princessconnectredive/files/manifest`
you could find a 3 Mb file, this is the sqlite database.
place it any where in project and edit `DATABASES` in `settings.py`.

#### Static files

Use `Unity Studio` to unpack resource in `/data/data/jp.co.cygames.princessconnectredive/files/`
Place it where you want and add it into `STATICFILES_DIRS`. 