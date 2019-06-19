# Pcrd-Wiki

## Features:

  - [x] area map
  - [x] quest drop detail page
  - [x] equipment pagedown
  - [x] unit character page (avatar & skill data)
  - [x] max level characters data table
  - [ ] PVP solution create, search and share _(in develop)_
  - [ ] monsters page
  - [x] unit character equipment per rank
  - [ ] Beautify all pages
  - [ ] Gacha Simulator
  - [ ] International _(in develop)_
  - [ ] Wiki like edit and user account system
  
## Note

[Princess Connect Re:Dive Wiki Website On Azure](http://pcrd.azurewebsites.net) is synced with repo's master branch
and should be used **only** for develop.

[pcrxwiki.xyz](https://johnlyu.com) is the production site, updated manually by myself.


## For Developers

Database and static files are not contained in this repo, you should grab and plce it by yourself.

### Database

Go to your android `/data/data/jp.co.cygames.princessconnectredive/files/manifest`
you could find a file named `sha1("master.mdb")`, this is the sqlite database.
place it any where in project and edit `DATABASES` in `settings.py`.

### Static files

Use [AssetStudio](https://github.com/Perfare/AssetStudio) to unpack resource in `/data/data/jp.co.cygames.princessconnectredive/files/`  
Place it where you want and add it into `STATICFILES_DIRS`. 
