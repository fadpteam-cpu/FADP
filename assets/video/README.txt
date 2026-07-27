FADP — HERO VIDEO
=================

CURRENT STATE
  The home page hero is wired to:

    "Stunning Aerial View of London Cityscape" by Gül Işık
    https://www.pexels.com/video/stunning-aerial-view-of-london-cityscape-28988731/
    Free to use, no attribution required, commercial use permitted.

  It is loaded from Pexels' CDN as a fallback source. The page tries
  a LOCAL file first:

      assets/video/hero.mp4        <- checked first
      Pexels CDN URL               <- used only if the local file is absent

RECOMMENDED: SELF-HOST IT
  Hotlinking someone else's CDN is fragile — the URL can change, and
  some CDNs block off-site requests. Downloading takes one click and
  makes the hero reliable and faster:

    1. Open the Pexels link above
    2. Click "Free download", choose the 1920x1080 version
    3. Rename the file to           hero.mp4
    4. Put it in this folder        assets/video/hero.mp4
    5. Commit and push

  The local file automatically takes priority. Nothing else to change.

  Check the file size first. If it is over ~12 MB, compress it:

    ffmpeg -i download.mp4 -vf scale=1920:-2 -c:v libx264 -crf 30 \
           -preset slow -an -movflags +faststart hero.mp4

  Or use handbrake.fr with the "Fast 1080p30" preset, quality RF 28-30,
  and remove the audio track.

THE POSTER STILL
  Set in build_pages.py under IMG['hero']. It currently points at the
  matching frame from the same Pexels clip, so the hero looks correct
  before the video loads and for reduced-motion visitors. If you swap
  the video, swap the poster to match its opening frame.

REPLACING IT LATER WITH YOUR OWN FOOTAGE
  Same process: name it hero.mp4, drop it here, update IMG['hero'] to
  a still from it.

  What works: a slow, steady shot. A gentle pan across an interior,
  light moving through a space, a slow push toward a window.
  What does not: fast cuts, handheld shake, people looking at camera.

  Spec: H.264 MP4, 1080p, 10-20s looping, no audio, under ~8 MB.
  The video loads before anything else a visitor sees, so size matters
  more than resolution.
