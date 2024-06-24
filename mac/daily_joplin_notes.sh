/opt/homebrew/bin/joplin --profile ~/.config/joplin-desktop use 'Daily Notes'
todays_date=$(date +%Y-%m-%d)
yesterdays_date=$(date -v -1d +%Y-%m-%d)
/opt/homebrew/bin/joplin --profile ~/.config/joplin-desktop cp "$yesterdays_date"
/opt/homebrew/bin/joplin --profile ~/.config/joplin-desktop ren "$yesterdays_date" "$todays_date"
