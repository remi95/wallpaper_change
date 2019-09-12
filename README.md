# Wallpaper change

Simple **python** script to change your wallpaper.   
You need a _folder_ with images you want as wallpaper.

I recommend you to automate this script with your crontab.

## Usage

**Custom your images folder path**   

```bash
git clone https://github.com/remi95/wallpaper_change.git
cd wallpaper_change
# Edit the `wallpaper_change.py` file to adapt the _imagesFolder_ variable to your folder location.
```

**Run the script as cron**

```bash
crontab -e
# Add the following line and change path/to/script.
# If you want, you can change time. Here, the script change wallpaper every 5 minutes.
*/5 * * * * /path/to/script/wallpaper_change.py
```