# Wallpaper change

Simple **python** script to change your wallpaper.   
You need a _folder_ with images you want as wallpaper.

I recommend you to automate this script with your crontab.

## Usage

`git clone https://github.com/remi95/wallpaper_change.git`

Edit the `wallpaper_change.py` file to adapt the _imagesFolder_ variable to your folder location.

Edit your crontab with `crontab -e`   
Add and adapt the following `*/5 * * * * /path/to/script/wallpaper_change.py`    
It will change your wallpaper every 5 minutes.
