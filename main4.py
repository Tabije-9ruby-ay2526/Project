from pyscript import display

creator = {
    'name': 'Joaquin Tabije',
    'tagline': 'Marvel Geek, Baller, Gym Freak, YOLO.',
    'about': 'Im an impulsive person and will do anything for the plot and fun.',
    'quote': 'If you obey all the rules, you miss all the fun.',
    'quote_by': 'Katharine Hepburn'
}

interests = ['Basketball', 'Gym', 'Marvel']
hobbies = ['Playing Basketball', 'weight lifting', 'doomscrolling']
dreams = ['To live life the fullest with the same people who inspired me to live the life I was meant to live']

quote = creator.get('quote')
quote_by = creator.get('quote_by')

display('Meet Me', target='output')
display(creator.get('name'), target='output')
display(creator.get('tagline'), target='output')

display('About me', target='output')
display(creator.get('about'), target='output')

display('Interests', target='output')
display(', '.join(interests), target='output')

display('Hobbies', target='output')
display(', '.join(hobbies), target='output')

display('Dreams', target='output')
display(', '.join(dreams), target='output')

display(f'"{quote}" - {quote_by}', target='output')