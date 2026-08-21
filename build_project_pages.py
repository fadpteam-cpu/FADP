# Individual project case-study pages. Run after build_pages.py.
import os
exec(open('build_pages.py').read().split("# ---------------------------------------------------------------- write")[0])


def project_page(slug, title, kicker, meta, images, body_html):
    gallery_html = ""
    for img in images:
        span = img.get('span', 'wide')
        cap = f'<figcaption>{img["caption"]}</figcaption>' if img.get('caption') else ''
        gallery_html += f'''
      <figure class="pd-fig pd-{span}">
        <img src="../{img["src"]}" alt="{img["alt"]}" loading="lazy">
        {cap}
      </figure>'''

    body = f'''
<div class="page-hero pd-hero">
  <div class="wrap">
    <div class="crumbs"><a href="../index.html">Home</a> &#183; <a href="../projects.html">Projects</a> &#183; {kicker}</div>
    <h1>{title}</h1>
    <p class="lede">{meta}</p>
  </div>
</div>

<section class="pd-gallery">
  <div class="wrap">
    {gallery_html}
  </div>
</section>

{f'<section class="pd-body"><div class="wrap"><div class="pd-copy">{body_html}</div></div></section>' if body_html else ''}
'''
    return (head(f'{title} &#183; FADP Architecture', meta, depth=1)
            + header('projects', depth=1) + body + cta_band(depth=1) + '\n' + footer(depth=1))


englehurst = dict(
    slug='englehurst',
    title='Englehurst',
    kicker='Residential extension',
    meta='A three-storey extension and rear return to a suburban house — brick, painted timber cladding and slate.',
    images=[
        {'src':'assets/img/projects/englehurst-front.jpg', 'alt':'Englehurst — front elevation at dusk',
         'caption':'Front elevation.'},
        {'src':'assets/img/projects/englehurst-rear.jpg', 'alt':'Englehurst — rear elevation at dusk',
         'caption':'Rear elevation.'},
        {'src':'assets/img/projects/englehurst-section.jpg', 'alt':'Englehurst — long section through the house',
         'caption':'Long section.'},
    ],
    body_html=''
)

os.makedirs('projects', exist_ok=True)
path = f"projects/{englehurst['slug']}.html"
open(path, 'w').write(project_page(**englehurst))
print(f"{path}  {os.path.getsize(path) // 1024}KB")
