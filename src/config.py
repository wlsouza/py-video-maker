# General #
general = {
    'video_language_prefix': 'en',  # Prefix of language ex: portuguese = 'pt', English = 'en'
    'video_resolution': (1920, 1080)  # Tuple with Width, Height (in pixels)
}

# Text Robot #
text_robot = {
    'max_sentences': 7
}

# Image Robot #
image_robot = {}

# Video Robot #
video_robot = {
    'text_clip': {
        0: {
            'size': (1920, 400),  # Size of image
            'align': 'South',  # Position of text at image
            'position': ('center', 'bottom'),  # Position of image at video
            'start': 2,  # Seconds to start text_clip
            'duration': 5  # Duration of text_clip
        },
        1: {
            'size': (1920, 1080),
            'align': 'South',
            'position': ('center', 'bottom'),
            'start': 2,
            'duration': 5
        },
        2: {
            'size': (800, 1080),
            'align': 'West',
            'position': ('left', 'center'),
            'start': 2,
            'duration': 5
        },
        3: {
            'size': (1920, 400),
            'align': 'South',
            'position': ('center', 'bottom'),
            'start': 2,
            'duration': 5
        },
        4: {
            'size': (1920, 1080),
            'align': 'South',
            'position': ('center', 'bottom'),
            'start': 2,
            'duration': 5
        },
        5: {
            'size': (800, 1080),
            'align': 'West',
            'position': ('left', 'center'),
            'start': 2,
            'duration': 5
        },
        6: {
            'size': (1920, 400),
            'align': 'South',
            'position': ('center', 'bottom'),
            'start': 2,
            'duration': 5
        }
    },
    'image_clip': {
        'size': (1920, 1080),
        'duration': 8  # Duration of image_clip
    }
}