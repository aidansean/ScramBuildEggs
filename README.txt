==========================================================================================
  (c) Aidan Randle-Conde 2015
  aidan.randleconde@gmail.com
  https://github.com/aidansean/ScramBuildEggs
==========================================================================================

==========================================================================================
Quick start:
==========================================================================================
To use this tool, copy the .sh and .py files to your working directory.
Then do:
> source build.sh

This will pipe the output of "scram b -j4" onto a file called build.log (so you can
always get the raw log file if you need it.)

the python file then parses the log file and formats the output to be a bit easier for the
user to read.

==========================================================================================
Overview
==========================================================================================
This script is designed to do a few things:

- Add colour so the user has an idea which errors are similar.  (So far the colours are
  not arranged in any coherent order.)
- Make the file name and line number of the error stand out.  (The user can quickly 
  browse to the error message and fix it without even reading the error message.)
- Wrap the output to ~80 characters to make lines easier to read.  (Whether this makes
  things easier for the user is a matter of taste.  Aidan can't stand very long lines,
  and they make is eyes glaze over.)

==========================================================================================
  FAQ:
==========================================================================================
Is this thing complete?
  Nope.  Nowhere near.
    
Can I help?
  Yes please!  For it and pull request improvements.
    
Sometimes the lines wrap in such a way that I can't tell where the error was.
  Yeah, this isn't perfect and it needs to be fixed.
    
Do the colours mean anything?
  So far no, they just help the user identify similar error messages.  If you get a lot of
  the cyan messages together then you probably missed to declare a whole block of
  variables.

Will this thing change/evolve over time?
  Definitely.  This was put together one Sunday afternoon to make debugging a little
  easier to do.  There's a lot of scope for improving things.

Shouldn't this be fully customisable?
  Sure.  There is a special class that parses each error message.  If you think you can
  improve that then please do.

