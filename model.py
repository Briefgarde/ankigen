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
            'name': '{{Count}}',
            'qfmt': '<p>{{Count}}</p>',             
            'afmt': '{{FrontSide}}<hr>{{Note}<br>{{MyMedia}}',
            },
        ],
    css=
    """
    p {
    font-weight: bold;
    text-align: center;
    font-size: 20px; 
    }
    .red {
    color : red;
    }
    """
    )