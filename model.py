import genanki as anki


my_model = anki.Model(
    1607392318,
    'Basic',
    fields=[
        {'name': 'Count'},
        {'name': 'Note'},
        {'name': 'MyMedia'},                                 
    ],
    templates=[
        {
            'name': 'Card {{Count}}',
            'qfmt': 'Card {{Count}}',             
            'afmt': '{{FrontSide}}<hr>{{Note}}<br>{{MyMedia}}',
            },
        ]
    )