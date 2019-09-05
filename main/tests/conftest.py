from pytest import fixture


@fixture
def twelve_pocket_articles():
    return ({'status': 1, 'complete': 1, 'list': {
        '2024276337': {'item_id': '2024276337', 'resolved_id': '2024276337',
                       'given_url': 'https://www.medicalnewstoday.com/articles/320584.php',
                       'given_title': 'Acetaminophen in pregnancy: Is it really safe?',
                       'favorite': '0', 'status': '1',
                       'time_added': '1567509577',
                       'time_updated': '1567687834',
                       'time_read': '1567687834', 'time_favorited': '0',
                       'sort_id': 0,
                       'resolved_title': 'Is acetaminophen really safe in pregnancy?',
                       'resolved_url': 'https://www.medicalnewstoday.com/articles/320584.php',
                       'excerpt': "With up to 70 percent of pregnant American women reaching for acetaminophen to treat pain, infection, and fever, debate about the drug's safety is ongoing. New research has brought further risks to light.",
                       'is_article': '1', 'is_index': '0', 'has_video': '0',
                       'has_image': '1', 'word_count': '1271', 'lang': 'en',
                       'time_to_read': 6,
                       'amp_url': 'https://www.medicalnewstoday.com/articles/amp/320584',
                       'top_image_url': 'https://cdn1.medicalnewstoday.com/content/images/hero/320/320584/320584_1100.jpg',
                       'tags': {'private': {'item_id': '2024276337',
                                            'tag': 'private'}}, 'authors': {
                '75920337': {'item_id': '2024276337',
                             'author_id': '75920337',
                             'name': 'Yella Hewings-Martin PhD',
                             'url': 'https://www.medicalnewstoday.com/authors/yella-hewingsmartin-phd'}},
                       'image': {'item_id': '2024276337',
                                 'src': 'https://cdn1.medicalnewstoday.com/content/images/articles/320/320584/acetaminophen-and-pregnancy.jpg',
                                 'width': '0', 'height': '0'}, 'images': {
                '1': {'item_id': '2024276337', 'image_id': '1',
                      'src': 'https://cdn1.medicalnewstoday.com/content/images/articles/320/320584/acetaminophen-and-pregnancy.jpg',
                      'width': '0', 'height': '0', 'credit': '',
                      'caption': ''}},
                       'domain_metadata': {'name': 'Medical News Today',
                                           'logo': 'https://logo.clearbit.com/medicalnewstoday.com?size=800',
                                           'greyscale_logo': 'https://logo.clearbit.com/medicalnewstoday.com?size=800&greyscale=true'},
                       'listen_duration_estimate': 492},
        '2675608289': {'item_id': '2675608289', 'resolved_id': '2675608289',
                       'given_url': 'https://nickjanetakis.com/blog/4-use-cases-for-when-to-use-celery-in-a-flask-application',
                       'given_title': '4 Use Cases for When to Use Celery in a Flask Application — Nick Janetakis',
                       'favorite': '0', 'status': '1',
                       'time_added': '1567597691',
                       'time_updated': '1567687537',
                       'time_read': '1567687536', 'time_favorited': '0',
                       'sort_id': 1,
                       'resolved_title': '4 Use Cases for When to Use Celery in a Flask Application',
                       'resolved_url': 'https://nickjanetakis.com/blog/4-use-cases-for-when-to-use-celery-in-a-flask-application',
                       'excerpt': "Celery helps you run code asynchronously or on a periodic schedule which are very common things you'd want to do in most web projects.",
                       'is_article': '1', 'is_index': '0', 'has_video': '0',
                       'has_image': '1', 'word_count': '2624', 'lang': 'en',
                       'time_to_read': 12,
                       'top_image_url': 'https://nickjanetakis.com/assets/blog/cards/4-use-cases-for-when-to-use-celery-in-a-flask-application-7550d977a858f460af12673a49cc26582f401bf601a84ce702980e42e670a09e.jpg',
                       'authors': {'35853417': {'item_id': '2675608289',
                                                'author_id': '35853417',
                                                'name': 'Nick Janetakis',
                                                'url': ''}},
                       'image': {'item_id': '2675608289',
                                 'src': 'https://nickjanetakis.com/assets/blog/cards/4-use-cases-for-when-to-use-celery-in-a-flask-application-7550d977a858f460af12673a49cc26582f401bf601a84ce702980e42e670a09e.jpg',
                                 'width': '750', 'height': '422'},
                       'images': {
                           '1': {'item_id': '2675608289', 'image_id': '1',
                                 'src': 'https://nickjanetakis.com/assets/blog/cards/4-use-cases-for-when-to-use-celery-in-a-flask-application-7550d977a858f460af12673a49cc26582f401bf601a84ce702980e42e670a09e.jpg',
                                 'width': '750', 'height': '422',
                                 'credit': '', 'caption': ''}},
                       'listen_duration_estimate': 1016},
        '2712302873': {'item_id': '2712302873', 'resolved_id': '1380613543',
                       'given_url': 'https://pytest.org/en/latest/goodpractices.html#goodpractices',
                       'given_title': 'Good Integration Practices — pytest documentation',
                       'favorite': '0', 'status': '1',
                       'time_added': '1567453868',
                       'time_updated': '1567453870',
                       'time_read': '1567453870', 'time_favorited': '0',
                       'sort_id': 2,
                       'resolved_title': 'Good Integration Practices — pytest documentation',
                       'resolved_url': 'https://doc.pytest.org/en/latest/goodpractices.html',
                       'excerpt': 'For development, we recommend to use virtualenv environments and pip for installing your application and any dependencies as well as the pytest package itself. This ensures your code and dependencies are isolated from the system Python installation.  Where PACKAGENAME is the name of your package.',
                       'is_article': '1', 'is_index': '0', 'has_video': '0',
                       'has_image': '0', 'word_count': '603', 'lang': 'en',
                       'time_to_read': 3, 'listen_duration_estimate': 233},
        '2485170985': {'item_id': '2485170985', 'resolved_id': '2485170985',
                       'given_url': 'https://medium.com/@neilkakkar/a-framework-for-first-principles-thinking-522eff9d589c',
                       'given_title': 'A framework for first principles thinking | Neil Kakkar',
                       'favorite': '0', 'status': '1',
                       'time_added': '1567204697',
                       'time_updated': '1567261064',
                       'time_read': '1567261063', 'time_favorited': '0',
                       'sort_id': 3,
                       'resolved_title': 'A framework for First Principles Thinking',
                       'resolved_url': 'https://medium.com/@neilkakkar/a-framework-for-first-principles-thinking-522eff9d589c',
                       'excerpt': 'That was the first time I read about First Principles and it made me cry. Cry at…',
                       'is_article': '1', 'is_index': '0', 'has_video': '0',
                       'has_image': '1', 'word_count': '53', 'lang': 'en',
                       'top_image_url': 'https://miro.medium.com/max/1200/0*T2OmJbnLpqgiI-JX',
                       'authors': {'99142868': {'item_id': '2485170985',
                                                'author_id': '99142868',
                                                'name': 'Neil Kakkar',
                                                'url': ''},
                                   '114780189': {'item_id': '2485170985',
                                                 'author_id': '114780189',
                                                 'name': '/@neilkakkar',
                                                 'url': ''}},
                       'image': {'item_id': '2485170985',
                                 'src': 'https://miro.medium.com/fit/c/96/96/1*mu5JkgI3lw7ORnGnKDGmoA.jpeg',
                                 'width': '48', 'height': '48'}, 'images': {
                '1': {'item_id': '2485170985', 'image_id': '1',
                      'src': 'https://miro.medium.com/fit/c/96/96/1*mu5JkgI3lw7ORnGnKDGmoA.jpeg',
                      'width': '48', 'height': '48', 'credit': '',
                      'caption': ''},
                '2': {'item_id': '2485170985', 'image_id': '2',
                      'src': 'https://miro.medium.com/fit/c/1400/420/0*T2OmJbnLpqgiI-JX',
                      'width': '700', 'height': '210',
                      'credit': 'Benjamin Davies on Unsplash',
                      'caption': ''}}, 'domain_metadata': {'name': 'Medium',
                                                           'logo': 'https://logo.clearbit.com/medium.com?size=800',
                                                           'greyscale_logo': 'https://logo.clearbit.com/medium.com?size=800&greyscale=true'},
                       'listen_duration_estimate': 21},
        '2121396419': {'item_id': '2121396419', 'resolved_id': '2121396419',
                       'given_url': 'https://realpython.com/python-gil/',
                       'given_title': 'article-mobile.html',
                       'favorite': '0', 'status': '1',
                       'time_added': '1567165868',
                       'time_updated': '1567219353',
                       'time_read': '1567219352', 'time_favorited': '0',
                       'sort_id': 4,
                       'resolved_title': 'What is the Python Global Interpreter Lock (GIL)?',
                       'resolved_url': 'https://realpython.com/python-gil/',
                       'excerpt': 'The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter. This means that only one thread can be in a state of execution at any point in time.',
                       'is_article': '1', 'is_index': '0', 'has_video': '0',
                       'has_image': '1', 'word_count': '2107', 'lang': 'en',
                       'time_to_read': 10,
                       'top_image_url': 'https://files.realpython.com/media/python-gil-title.958a5bb2cecb.jpg',
                       'authors': {'85899498': {'item_id': '2121396419',
                                                'author_id': '85899498',
                                                'name': 'Abhinav Ajitsaria',
                                                'url': 'https://realpython.com/python-gil/#author'}},
                       'image': {'item_id': '2121396419',
                                 'src': 'https://realpython.com/static/pytrick-dict-merge.4201a0125a5e.png',
                                 'width': '738', 'height': '490'},
                       'images': {
                           '1': {'item_id': '2121396419', 'image_id': '1',
                                 'src': 'https://realpython.com/static/pytrick-dict-merge.4201a0125a5e.png',
                                 'width': '738', 'height': '490',
                                 'credit': '', 'caption': ''}},
                       'listen_duration_estimate': 816},
        '340082513': {'item_id': '340082513', 'resolved_id': '340082513',
                      'given_url': 'https://en.wikipedia.org/wiki/Wikipedia:Chesterton%27s_fence',
                      'given_title': "Wikipedia:Chesterton's fence - Wikipedia",
                      'favorite': '0', 'status': '1',
                      'time_added': '1567204721',
                      'time_updated': '1567216179',
                      'time_read': '1567216178', 'time_favorited': '0',
                      'sort_id': 5,
                      'resolved_title': "Wikipedia:Chesterton's fence",
                      'resolved_url': 'https://en.wikipedia.org/wiki/Wikipedia:Chesterton%27s_fence',
                      'excerpt': 'Chesterton\'s fence is the principle that reforms should not be made until the reasoning behind the existing state of affairs is understood. The quotation is from G. K. Chesterton\'s 1929 book The Thing, in the chapter entitled "The Drift from Domesticity":',
                      'is_article': '1', 'is_index': '0', 'has_video': '0',
                      'has_image': '1', 'word_count': '354', 'lang': 'en',
                      'authors': {'7331684': {'item_id': '340082513',
                                              'author_id': '7331684',
                                              'name': 'From Wikipedia, the free',
                                              'url': ''}},
                      'image': {'item_id': '340082513',
                                'src': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Essay.svg/30px-Essay.svg.png',
                                'width': '30', 'height': '36'}, 'images': {
                '1': {'item_id': '340082513', 'image_id': '1',
                      'src': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Essay.svg/30px-Essay.svg.png',
                      'width': '30', 'height': '36', 'credit': '',
                      'caption': ''},
                '2': {'item_id': '340082513', 'image_id': '2',
                      'src': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Blocked_road_-_geograph.org.uk_-_1024571.jpg/220px-Blocked_road_-_geograph.org.uk_-_1024571.jpg',
                      'width': '220', 'height': '165', 'credit': '',
                      'caption': "Just the fact there doesn't seem to be a reason for this fence to be here doesn't mean there isn't a reason."}},
                      'domain_metadata': {'name': 'Wikipedia',
                                          'logo': 'https://logo.clearbit.com/wikipedia.org?size=800',
                                          'greyscale_logo': 'https://logo.clearbit.com/wikipedia.org?size=800&greyscale=true'},
                      'listen_duration_estimate': 137},
        '2708991016': {'item_id': '2708991016', 'resolved_id': '2703188319',
                       'given_url': 'https://neilkakkar.com/things-I-learnt-from-a-senior-dev.html?utm_source=hackernewsletter&utm_medium=email&utm_term=fav',
                       'given_title': 'Things I Learnt from a Senior Software Engineer | Neil Kakkar',
                       'favorite': '0', 'status': '1',
                       'time_added': '1567180692',
                       'time_updated': '1567205606',
                       'time_read': '1567205605', 'time_favorited': '0',
                       'sort_id': 6,
                       'resolved_title': 'Things I Learnt from a Senior Software Engineer',
                       'resolved_url': 'https://neilkakkar.com/things-I-learnt-from-a-senior-dev.html',
                       'excerpt': 'A year ago, I started working full-time at Bloomberg. That’s when I imagined writing this post. I imagined myself to be full of ideas that I could spit out on paper when the time comes. Just one month in, I realised it won’t be that easy: I was already forgetting things I learnt.',
                       'is_article': '1', 'is_index': '0', 'has_video': '0',
                       'has_image': '1', 'word_count': '4431', 'lang': 'en',
                       'time_to_read': 20,
                       'top_image_url': 'https://neilkakkar.com/assets/images/github.png',
                       'authors': {'110257304': {'item_id': '2708991016',
                                                 'author_id': '110257304',
                                                 'name': 'Neil Kakkar',
                                                 'url': 'https://neilkakkar.com/about/'}},
                       'image': {'item_id': '2708991016',
                                 'src': 'https://neilkakkar.com/assets/images/github.png',
                                 'width': '0', 'height': '0'}, 'images': {
                '1': {'item_id': '2708991016', 'image_id': '1',
                      'src': 'https://neilkakkar.com/assets/images/github.png',
                      'width': '0', 'height': '0', 'credit': '',
                      'caption': ''},
                '2': {'item_id': '2708991016', 'image_id': '2',
                      'src': 'https://neilkakkar.com/assets/images/neil_code.jpeg',
                      'width': '0', 'height': '0', 'credit': '',
                      'caption': ''}}, 'listen_duration_estimate': 1715},
        '2535530830': {'item_id': '2535530830', 'resolved_id': '2535530830',
                       'given_url': 'https://realpython.com/intro-to-python-threading/',
                       'given_title': 'An Intro to Threading in Python – Real Python',
                       'favorite': '0', 'status': '1',
                       'time_added': '1567141440',
                       'time_updated': '1567167449',
                       'time_read': '1567167446', 'time_favorited': '0',
                       'sort_id': 7,
                       'resolved_title': 'An Intro to Threading in Python',
                       'resolved_url': 'https://realpython.com/intro-to-python-threading/',
                       'excerpt': 'Python threading allows you to have different parts of your program run concurrently and can simplify your design. If you’ve got some experience in Python and want to speed up your program using threads, then this tutorial is for you!',
                       'is_article': '1', 'is_index': '0', 'has_video': '0',
                       'has_image': '1', 'word_count': '8180', 'lang': 'en',
                       'time_to_read': 37,
                       'top_image_url': 'https://files.realpython.com/media/Intro-to-Threading_Watermarked.95b143d3ba6c.jpg',
                       'authors': {'108102716': {'item_id': '2535530830',
                                                 'author_id': '108102716',
                                                 'name': 'Jim Anderson',
                                                 'url': 'https://realpython.com/intro-to-python-threading/#author'}},
                       'image': {'item_id': '2535530830',
                                 'src': 'https://files.realpython.com/media/intro-threading-shared-database.267a5d8c6aa1.png',
                                 'width': '1623', 'height': '663'},
                       'images': {
                           '1': {'item_id': '2535530830', 'image_id': '1',
                                 'src': 'https://files.realpython.com/media/intro-threading-shared-database.267a5d8c6aa1.png',
                                 'width': '1623', 'height': '663',
                                 'credit': '', 'caption': ''},
                           '2': {'item_id': '2535530830', 'image_id': '2',
                                 'src': 'https://files.realpython.com/media/intro-threading-single-thread.85204fa11210.png',
                                 'width': '1383', 'height': '2901',
                                 'credit': '', 'caption': ''},
                           '3': {'item_id': '2535530830', 'image_id': '3',
                                 'src': 'https://files.realpython.com/media/intro-threading-two-threads-part1.c1c0e65a8481.png',
                                 'width': '1953', 'height': '1641',
                                 'credit': '', 'caption': ''},
                           '4': {'item_id': '2535530830', 'image_id': '4',
                                 'src': 'https://files.realpython.com/media/intro-threading-two-threads-part2.df42d4fbfe21.png',
                                 'width': '2013', 'height': '1641',
                                 'credit': '', 'caption': ''},
                           '5': {'item_id': '2535530830', 'image_id': '5',
                                 'src': 'https://files.realpython.com/media/intro-threading-two-threads-part3.18576920f88f.png',
                                 'width': '2013', 'height': '1551',
                                 'credit': '', 'caption': ''},
                           '6': {'item_id': '2535530830', 'image_id': '6',
                                 'src': 'https://realpython.com/static/pytrick-dict-merge.4201a0125a5e.png',
                                 'width': '738', 'height': '490',
                                 'credit': '', 'caption': ''}},
                       'listen_duration_estimate': 3166},
        '2705079041': {'item_id': '2705079041', 'resolved_id': '2705079041',
                       'given_url': 'https://abe-winter.github.io/wisdom/2019/08/26/rust-for-web.html',
                       'given_title': 'Picking rust for web',
                       'favorite': '0', 'status': '1',
                       'time_added': '1567000066',
                       'time_updated': '1567081571',
                       'time_read': '1567081570', 'time_favorited': '0',
                       'sort_id': 8,
                       'resolved_title': 'Picking rust for web',
                       'resolved_url': 'https://abe-winter.github.io/wisdom/2019/08/26/rust-for-web.html',
                       'excerpt': 'I’ve been staring at this energy efficiency across programming languages table for days. It can’t be right (why is typescript so much worse than javascript?) but a lot of it tracks with things I’ve observed from using these languages IRL. Also this web framework benchmarks project.',
                       'is_article': '1', 'is_index': '0', 'has_video': '0',
                       'has_image': '0', 'word_count': '1441', 'lang': 'en',
                       'time_to_read': 7, 'authors': {
                '91128179': {'item_id': '2705079041',
                             'author_id': '91128179', 'name': 'Abe Winter',
                             'url': ''}}, 'listen_duration_estimate': 558},
        '2700843201': {'item_id': '2700843201', 'resolved_id': '2700843201',
                       'given_url': 'https://m.signalvnoise.com/how-i-wrote-shape-up/',
                       'given_title': 'How I Wrote Shape Up - Signal v. Noise',
                       'favorite': '0', 'status': '1',
                       'time_added': '1567018682',
                       'time_updated': '1567018686',
                       'time_read': '1567018686', 'time_favorited': '0',
                       'sort_id': 9,
                       'resolved_title': 'How I Wrote Shape Up',
                       'resolved_url': 'https://m.signalvnoise.com/how-i-wrote-shape-up/',
                       'excerpt': 'Here’s a little behind-the-scenes look at the development of our newest book, Shape Up: Stop Running in Circles and Ship Work that Matters. In August 2018, Jason Fried (Basecamp’s founder and CEO) asked me to write a book about how we work.',
                       'is_article': '1', 'is_index': '0', 'has_video': '0',
                       'has_image': '1', 'word_count': '885', 'lang': 'en',
                       'time_to_read': 4,
                       'top_image_url': 'https://egbdmrh4mm2nyyyh-zippykid.netdna-ssl.com/wp-content/uploads/2019/08/IMG_4799.jpeg',
                       'authors': {'103414945': {'item_id': '2700843201',
                                                 'author_id': '103414945',
                                                 'name': 'Ryan Singer',
                                                 'url': 'https://m.signalvnoise.com/author/ryan-singer/'}},
                       'image': {'item_id': '2700843201',
                                 'src': 'https://i0.wp.com/m.signalvnoise.com/wp-content/uploads/2019/08/DycDkX1UcAAWhFB-3.jpeg?fit=640%2C447&ssl=1',
                                 'width': '0', 'height': '0'}, 'images': {
                '1': {'item_id': '2700843201', 'image_id': '1',
                      'src': 'https://i0.wp.com/m.signalvnoise.com/wp-content/uploads/2019/08/DycDkX1UcAAWhFB-3.jpeg?fit=640%2C447&ssl=1',
                      'width': '0', 'height': '0', 'credit': '',
                      'caption': ''},
                '2': {'item_id': '2700843201', 'image_id': '2',
                      'src': 'https://i1.wp.com/m.signalvnoise.com/wp-content/uploads/2019/08/DycDkX4UwAEQvbC-3.jpeg?fit=640%2C447&ssl=1',
                      'width': '0', 'height': '0', 'credit': '',
                      'caption': ''},
                '3': {'item_id': '2700843201', 'image_id': '3',
                      'src': 'https://i1.wp.com/m.signalvnoise.com/wp-content/uploads/2019/08/DycDkYDV4AAyr6W-2.jpeg?fit=640%2C447&ssl=1',
                      'width': '0', 'height': '0', 'credit': '',
                      'caption': ''},
                '4': {'item_id': '2700843201', 'image_id': '4',
                      'src': 'https://i1.wp.com/m.signalvnoise.com/wp-content/uploads/2019/08/DycDkX8VAAAlrGq-2.jpeg?fit=640%2C447&ssl=1',
                      'width': '0', 'height': '0', 'credit': '',
                      'caption': ''},
                '5': {'item_id': '2700843201', 'image_id': '5',
                      'src': 'https://i2.wp.com/m.signalvnoise.com/wp-content/uploads/2019/08/Book-systems.png?ssl=1',
                      'width': '0', 'height': '0', 'credit': '',
                      'caption': ''},
                '6': {'item_id': '2700843201', 'image_id': '6',
                      'src': 'https://i2.wp.com/m.signalvnoise.com/wp-content/uploads/2019/08/Dz5aVKLVYAAWK2D-2.jpeg?w=640&ssl=1',
                      'width': '0', 'height': '0', 'credit': '',
                      'caption': ''},
                '7': {'item_id': '2700843201', 'image_id': '7',
                      'src': 'https://i2.wp.com/m.signalvnoise.com/wp-content/uploads/2019/08/IMG_4799.jpeg?fit=640%2C390&ssl=1',
                      'width': '0', 'height': '0', 'credit': '',
                      'caption': ''}},
                       'domain_metadata': {'name': 'Basecamp',
                                           'logo': 'https://logo.clearbit.com/signalvnoise.com?size=800',
                                           'greyscale_logo': 'https://logo.clearbit.com/signalvnoise.com?size=800&greyscale=true'},
                       'listen_duration_estimate': 343},
        '2692536740': {'item_id': '2692536740', 'resolved_id': '2692536740',
                       'given_url': 'https://blog.atulr.com/nodegui-intro/',
                       'given_title': '? Announcing NodeGUI and React NodeGUI - Build native desktop apps with Jav',
                       'favorite': '0', 'status': '1',
                       'time_added': '1566489375',
                       'time_updated': '1566820044',
                       'time_read': '1566820043', 'time_favorited': '0',
                       'sort_id': 10,
                       'resolved_title': '? Announcing NodeGUI and React NodeGUI - Build native desktop apps with Javascript and CSS ?',
                       'resolved_url': 'https://blog.atulr.com/nodegui-intro/',
                       'excerpt': 'We’re very excited to announce the launch of NodeGUI and React NodeGUI! ? NodeGUI is an open source library for building cross platform native desktop applications with JavaScript and CSS like styling. NodeGui apps can run on Mac, Windows, and Linux from a single codebase.',
                       'is_article': '1', 'is_index': '0', 'has_video': '0',
                       'has_image': '1', 'word_count': '893', 'lang': 'en',
                       'time_to_read': 4, 'authors': {
                '93498662': {'item_id': '2692536740',
                             'author_id': '93498662', 'name': 'Atul R',
                             'url': 'https://www.atulr.com'}},
                       'image': {'item_id': '2692536740',
                                 'src': 'https://blog.atulr.com/67593393e839ebc164220306631e2ede/nodegui.svg',
                                 'width': '0', 'height': '0'}, 'images': {
                '1': {'item_id': '2692536740', 'image_id': '1',
                      'src': 'https://blog.atulr.com/67593393e839ebc164220306631e2ede/nodegui.svg',
                      'width': '0', 'height': '0', 'credit': '',
                      'caption': ''},
                '2': {'item_id': '2692536740', 'image_id': '2',
                      'src': 'https://blog.atulr.com/aa0133a07d7b6735125126a40fc97055/calculator_win.gif',
                      'width': '0', 'height': '250', 'credit': '',
                      'caption': ''},
                '3': {'item_id': '2692536740', 'image_id': '3',
                      'src': 'https://blog.atulr.com/fc664cb2148c98d6c1405ee0832d38b3/calculator_linux.gif',
                      'width': '0', 'height': '250', 'credit': '',
                      'caption': ''},
                '4': {'item_id': '2692536740', 'image_id': '4',
                      'src': 'https://blog.atulr.com/361956edd4ce5434869892bef38bfeee/calculator_mac.gif',
                      'width': '0', 'height': '250', 'credit': '',
                      'caption': ''},
                '5': {'item_id': '2692536740', 'image_id': '5',
                      'src': 'https://blog.atulr.com/434ea0d67369ef0de94b8b547f8535cb/output.gif',
                      'width': '0', 'height': '250', 'credit': '',
                      'caption': ''},
                '6': {'item_id': '2692536740', 'image_id': '6',
                      'src': 'https://blog.atulr.com/fc7d4b62154c0349de95b6bee6b04854/image_view_win.gif',
                      'width': '0', 'height': '250', 'credit': '',
                      'caption': ''},
                '7': {'item_id': '2692536740', 'image_id': '7',
                      'src': 'https://blog.atulr.com/cff49b306f38d7350ede3795e42320f7/image_view_linux.gif',
                      'width': '0', 'height': '250', 'credit': '',
                      'caption': ''},
                '8': {'item_id': '2692536740', 'image_id': '8',
                      'src': 'https://blog.atulr.com/c7c213209aa96a3071f2be02326e4515/image_view_mac.gif',
                      'width': '0', 'height': '250', 'credit': '',
                      'caption': ''},
                '9': {'item_id': '2692536740', 'image_id': '9',
                      'src': 'https://blog.atulr.com/ad030801e31a4e5e0cb1366982840321/kitchen.gif',
                      'width': '0', 'height': '350', 'credit': '',
                      'caption': ''}}, 'listen_duration_estimate': 346},
        '2647589396': {'item_id': '2647589396', 'resolved_id': '2647589396',
                       'given_url': 'https://madewithlove.be/one-job-many-roles-the-different-skills-needed-to-be-a-successful-cto/',
                       'given_title': 'One job, many roles. The different skills needed to be a successful CTO - m',
                       'favorite': '0', 'status': '1',
                       'time_added': '1566155364',
                       'time_updated': '1566819607',
                       'time_read': '1566819606', 'time_favorited': '0',
                       'sort_id': 11,
                       'resolved_title': 'One job, many roles. The different skills needed to be a successful CTO',
                       'resolved_url': 'https://madewithlove.be/one-job-many-roles-the-different-skills-needed-to-be-a-successful-cto/',
                       'excerpt': 'Some time ago I came across this article on Harvard Business School’s Working Knowledge blog about when founding CEOs need to go. It’s from 2005, but it is still just as relevant now.',
                       'is_article': '1', 'is_index': '0', 'has_video': '0',
                       'has_image': '0', 'word_count': '1516', 'lang': 'en',
                       'time_to_read': 7,
                       'top_image_url': 'https://madewithlove.be/wp-content/uploads/2019/06/blog-different-roles-of-the-cto@2x-100-1024x347.jpg',
                       'listen_duration_estimate': 587}}, 'error': None,
             'search_meta': {'search_type': 'normal'},
             'since': 1567718868},
            {'Date': 'Thu, 05 Sep 2019 21:27:48 GMT',
             'Content-Type': 'application/json',
             'Transfer-Encoding': 'chunked',
             'Connection': 'keep-alive', 'Server': 'Apache',
             'X-Frame-Options': 'SAMEORIGIN', 'Status': '200 OK',
             'X-Limit-Key-Limit': '10000',
             'X-Limit-Key-Remaining': '9996',
             'X-Limit-Key-Reset': '3303', 'X-Source': 'Pocket',
             'P3P': 'policyref="/w3c/p3p.xml", CP="ALL CURa ADMa DEVa OUR IND UNI COM NAV INT STA PRE"'})