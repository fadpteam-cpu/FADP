FADP — HERO VIDEO
=================

Drop your hero film in this folder named exactly:

    hero.mp4

The home page will pick it up automatically. Until a file is here,
the hero shows the poster still instead, so the page always looks
correct.

SPECIFICATION
  Format      MP4 (H.264) — the most widely supported
  Resolution  1920x1080 is plenty; 4K is unnecessary and slow
  Length      10-20 seconds, seamlessly looping if possible
  Frame rate  24 or 25 fps
  Audio       none needed (the video plays muted by design)
  File size   aim under 8 MB, 12 MB absolute maximum

WHY THE SIZE LIMIT
  The video loads before anything else a visitor sees. A 40 MB file
  means several seconds of blank hero on a normal connection, which
  costs more than the video gains. Compress hard.

COMPRESSING
  Free and simple: handbrake.fr
    - Preset: "Web > Gmail Medium 5 Minutes 480p30" then raise the
      resolution to 1080p, or use "Fast 1080p30"
    - Set constant quality around RF 28-30
    - Remove the audio track entirely
  Or with ffmpeg:
    ffmpeg -i input.mov -vf scale=1920:-2 -c:v libx264 -crf 30 \
           -preset slow -an -movflags +faststart hero.mp4

WHAT WORKS WELL
  A slow, steady shot. A gentle pan across an interior, light moving
  through a space, a slow push toward a window. Avoid fast cuts,
  handheld shake, and anything with people looking at camera.

THE POSTER STILL
  Set in build_pages.py in the IMG dictionary under 'hero'. It shows
  before the video loads and on reduced-motion devices, so it should
  be a frame that resembles the video's opening.
