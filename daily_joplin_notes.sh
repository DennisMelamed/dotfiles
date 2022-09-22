#joplin_p='joplin --profile ~/.config/joplin-desktop'
joplin --profile ~/.config/joplin-desktop use 'Daily Notes'
todays_date=$(date +%Y-%m-%d -d today)
yesterdays_date=$(date +%Y-%m-%d -d yesterday)
joplin --profile ~/.config/joplin-desktop cp "$yesterdays_date"
joplin --profile ~/.config/joplin-desktop ren "$yesterdays_date" "$todays_date"
