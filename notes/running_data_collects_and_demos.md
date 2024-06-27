# Intro

A bunch of these things are probably obvious. Data collects can be really complex though - hardware, software, travel, multiple people from different organizations, etc. all interacting - so its nice to have some reminders of stuff thats easy to forget. These are mostly things that I've failed to do in the past. No data collect ever goes perfectly, but hopefully these notes save some heartache down the road.

# Hardware


## Transporting Hardware

### Container
- If you're traveling to the field-site, test-fit & pack the equipment in the whatever you're using to transport it
- Do so at ~2 days before going, so you can remedy any issues
- If luggage for air travel, ensure that fragile/sensitive components are in carry-ons
- Be aware of what you can/can't bring through security, and consider what things may look like on the TSA x-ray machines
    - e.g. it might look like a circuit board & battery to you, to TSA it looks like a bunch of wires connected to a block of something...
- If traveling as a team, distribute equipment among members, with some thought to what happens if a piece of luggage gets lost
    - e.g. if you have two identical cameras to bring, split between people so if person A is delayed, at least you have 1 camera
    - similarly with tools, if you have two sets of allen keys, split them up
- This is still applicable for car travel!
    - make sure the equipment fits in the vehicle
    - verify that fragile things can be placed such that they don't move/break if braking or going over a pothole
- Minimizing bags is good - each person only has two hands and a single back, it looks more professional if you walk in with a few neatly packed items instead of a bunch of bags/loose gear



### Protecting gear
- Rule of thumb: better to over-protect equipment than to under-protect
- Take things apart and pack them neatly 
    - Maximally unscrew stuff from your mounting systems:
        - a camera in a box surrounded by bubble wrap is way less likely to break than the same camera bolted to a piece of wood and shoved in a backpack
        - balance this with setup/calibration-time when onsite: if your stereo system takes hours to align and calibrate camera locations relative to each other, maybe its better to pack the assembled & calibrated system in some bubble wrap than to take things apart and pack individually...
        - keep in mind that you'll likely have to re-calibrate onsite anyway, things like to move when in transit
    - sliding around inside a container is the enemy - shove some bubble wrap/foam/cords/something in the way so your expensive sensor doesn't bash against the sides of the box its in


## Designing/building hardware
- When desigining hardware mountings, reduce degrees of freedom
    - Make one obvious way things should attach, add indications of how that should happen in obvious places
        - e.g. written on a mounting block: "Use 1" 1/4-20 bolts (3) to attach camera with lens pointing along this arrow"
        - In above case, make it obvious how to align the camera along the arrow, e.g. another bolt that means the camera can't spin, or a perpendicular surface that you can press it up against

- Label everything (with a label maker if you have one), including who owns it (e.g. your company name or your initials)
    - Power cables w/ what they charge/power
    - Data cables w/ what they connect to
    - Devices w/ what they do, if not obvious
    - Ports/pins w/ what should plug into them
- Fasteners
    - Minimize the types/variety of fasteners you're using 
    - stick to e.g. allen heads (generally prefer over phillips, and you can have a many sizes of driver in 1 tool)
    - on the other hand, finding a screwdriver onsite tends to be easier than finding an allen key. Just hope its the right size of screwdriver...
    - stick to a consistent size of them (e.g. try to use only 5mm allen heads)

- Manage your cables - easier to handle a bundle of wires than N individual ones getting tangled up
- Attaching one device to another can be helpful, even if its with zipties
    - e.g. if sensor A and sensor B always move together, and they both have power bricks, attach the bricks to each other and bundle the calbes. Two devices to find a spot to rest have turned into one
    - You can always detach them if its annoying
- Put messy cabling configurations in a box if possible and attach the things inside to the walls of the box
    - looks more professional
    - reduces the chance that something comes unplugged/gets tangled in something else
- Protect connections - if it looks like it could get jostled and unplug at any second, it probably will
    - Screw-in connectors can help
- Thin wires like to break, use stress-relief and protect any thing/fragile wiring
- Wooden plates, brackets, and standoffs can get you pretty far in terms of a stable, consistent mounting system for sensors
- Command strips (especially the ones with the plasticy velcro-like stuff, duolock), are an awesome choice for connecting things securely, but removeably if their alignment isn't as important. You can even use them to attach something like a wireless reciever or a dongle to the back of your laptop so you can carry them both easily.
- CAD is your friend and is probably worth the learning curve. OpenSCAD might be a good choice if you're more of a software person than hardware
        



# Software
- [ ] Assume you won't have a network connection
    - Good way to test is to turn off all networking on the equipment you're bringing, and put your phone in a different room. Can you do your entire procedure with no issues?
    - Logins w/ 2FA are a key thing to watch out for - what if you can't pull your phone out/it doesn't have signal?
- [ ] What happens if someone else has to run the experiment?
    - Is anything tied to your user account on a computer? e.g. if you're out sick at the hotel, can your teammate login to the systems and be able to run everything without knowing your password?  
    - Test this - things like symlinks can make it seem like everything is accessible, but the file the link points to is actually owned by a different user and only they can access it
    - Virtual environments are another thing to watch out for on both this and the previous point - the python executable might be a link to a different user's python, and you might not be able to recreate the environment w/o a network connection

- [ ] When designing experiments, reduce degrees of freedom
    - Running an experiment should take e.g. a single line at the command prompt
    - `python experiment_runner.py ./configs/experiment1.json` is better than:
        1. Open a terminal and run `python camera1_runner.py`
        2. Open a terminal and run `python camera2_runner.py`
        3. Open a terminal and run `python other_sensor_runner.py`
        4. Open GUI `Data Recorder` and hit the record button
        5. Open GUI `Data visualizer` and configure it to show these data streams
        6. etc. etc.
    - Tools like `roslaunch`, `tmux`/`tmuxinator`, and even `subprocess.Popen` in python can be useful for this

- [ ] Have a way to visualize the data you're collecting.
    - This can be as simple as `tail`-ing logs 


# Data
- [ ] File backups are your friend
    - External hard drives are good for onsite backups (to be performed as frequently as reasonable)
        - I try to plan my experiments so I can have the last experiment backing up while the current one is running
        - Or, plan time during the day that is dedicated backup time (e.g. lunch breaks)
        - N+1 hard drives for backup is better than N
    - Estimate how much data you'll produce - ensure that your backup strategy can transfer that amount in the time you've alloted
    - Overnight backups to a remote storage location (e.g. a server back at home) is useful, hard drives can fail (especially in transit)
        - This depends on your hotel/site network speed - if slow, prioritize data you'd really cry over if it dissapeared
- [ ] Be thoughtful about the nature of the data and where it can go
    - e.g. if doing an overnight backup to a network server of ITAR data, is your connection to the server appropriate for ITAR data?
    - Hotel/cafe/random networks are like hotel safes - not all that secure...

- [ ] 
        

# Day/Week-before

- [ ] Do a maximally complete run-through. Preferably >2 days before, so you have a chance to fix discovered issues
    - Repeat at least the relevant sections of your run-through if you do fix something, don't assume you fixed it correctly
- [ ] Do make a document describing how the event should go - I organize mine as follows:

### Equipment Packing Checklist
- Sensors
- Tools
### Equipment Charging Checklist ("make sure the following are charging every chance you get")
### Experiment/demo action list
### Expected output files/data, backup schedule
### Troubleshooting advice (gotchas, frequent errors, debug steps)

# Pre-Departure Checks

# Onsite Checks

# Onsite Advice
- [ ] Breathe.
