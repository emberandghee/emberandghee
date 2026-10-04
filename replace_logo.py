import os
avatar = 'https://yt3.googleusercontent.com/4z_wMQUzqF0RgH5k11_nK7fdQGyEoxQ68n9TKwxqM7a9ULBhvEGHCmbe9Q9DL03LqvpuF89_gA=s900-c-k-c0x00ffffff-no-rj'
old = '<span class="text-orange-600 font-bold text-lg">E&G</span>'
new = f'<img src="{avatar}" alt="Ember and Ghee Logo" class="w-full h-full object-cover" />'

for root, _, files in os.walk('src'):
    for f in files:
        if f.endswith('.astro'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            if old in content:
                content = content.replace(old, new)
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(content)
