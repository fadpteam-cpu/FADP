FADP — HERO VIDEO
=================

CURRENT
  assets/video/hero.mp4        0.90 MB   H.264, 1920x1080, 30fps, 8.3s, no audio
  assets/img/hero-poster.jpg   0.16 MB   opening frame, shown before playback

  Source: "Stunning Aerial View of London Cityscape" by Gül Işık
  https://www.pexels.com/video/stunning-aerial-view-of-london-cityscape-28988731/
  Pexels licence: free to use, no attribution required, commercial use fine.

  The original download was 9.04 MB at 9.2 Mbps — far more than a
  background video under a dark scrim needs. Re-encoded at CRF 30 with
  faststart, it is 90% smaller with no visible difference at this scale.

REPLACING IT WITH YOUR OWN FOOTAGE
  1. Encode and drop in as assets/video/hero.mp4:

       ffmpeg -i yourfile.mov -vf scale=1920:-2 -c:v libx264 -crf 30 \
              -preset slow -pix_fmt yuv420p -an -movflags +faststart \
              assets/video/hero.mp4

     (or handbrake.fr, "Fast 1080p30" preset, quality RF 28-30, audio removed)

  2. Regenerate the poster from the new file so the first frame matches:

       ffmpeg -ss 0.2 -i assets/video/hero.mp4 -frames:v 1 \
              -vf scale=1600:-2 -q:v 6 assets/img/hero-poster.jpg

  3. Commit and push. No code changes needed.

WHY THESE SETTINGS
  -crf 30        aggressive but invisible under the hero's gradient scrim
  -an            strips audio; the video plays muted by design
  +faststart     moves the index to the front so playback can begin
                 before the file has fully downloaded
  -pix_fmt yuv420p  required for Safari and older devices

TARGETS
  Under 1 MB is ideal, 2 MB is the sensible ceiling. The hero video
  loads before anything else a visitor sees, so weight costs more than
  resolution gains.

WHAT WORKS ON SCREEN
  Slow, steady movement — an aerial drift, a gentle pan across an
  interior, light moving through a space. Avoid fast cuts, handheld
  shake, and people looking at camera.

FALLBACK BEHAVIOUR
  - Before the video loads: the poster shows
  - prefers-reduced-motion: video is paused in JS, poster stays visible
  - Missing or unplayable file: poster stays visible
  The hero is never blank.
