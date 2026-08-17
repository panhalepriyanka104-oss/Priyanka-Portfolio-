from pathlib import Path

p = Path('index.html')
text = p.read_text(encoding='utf-8')

linkedin = 'https://www.linkedin.com/posts/qksgroup_abm-ugcPost-6960834994986471424-p2Bz/?utm_source=share&utm_medium=member_desktop&rcm=ACoAACd64D8BtYkaAlUCj_lV8bN53JE-Pljbv6E'

if '6960834994986471424' not in text:
    if '<div class="research-grid">' in text:
        card = '''\n      <article class="research-card">\n        <div class="tag">Speaking &amp; Webinars · Account-Based Marketing</div>\n        <h4>QKS Group — ABM Webinar</h4>\n        <p>Webinar highlight featuring Priyanka speaking on Account-Based Marketing, demonstrating analyst communication, thought leadership and the ability to translate research into an audience-ready discussion.</p>\n        <a href="{}" target="_blank" rel="noopener">Watch webinar highlight →</a>\n      </article>'''.format(linkedin.replace('&','&amp;'))
        text = text.replace('<div class="research-grid">', '<div class="research-grid">' + card, 1)
    elif '<div class="pubs">' in text:
        card = '''<article class="pub"><small>Speaking &amp; Webinars · ABM</small><h4>QKS Group — ABM Webinar</h4><p>Webinar highlight featuring Priyanka speaking on Account-Based Marketing, demonstrating analyst communication, thought leadership and the ability to translate research into an audience-ready discussion.</p><a href="{}" target="_blank" rel="noopener">Watch webinar highlight →</a></article>'''.format(linkedin.replace('&','&amp;'))
        text = text.replace('<div class="pubs">', '<div class="pubs">' + card, 1)

p.write_text(text, encoding='utf-8')
