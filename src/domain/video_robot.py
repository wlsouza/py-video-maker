# !/usr/bin/python
# -*- coding: UTF-8 -*-

import textwrap
from moviepy.editor import *
from src.config import video_robot as config


class VideoRobot:

    def __init__(self, video):
        self.video = video

    def run(self):
        self.compose_video()

    def compose_video(self):
        images_list = []
        clips_list = []

        for sentence_index, sentence in enumerate(self.video.sentences):
            image = sentence.treated_image

            # Getting configs
            text_clip_align = config['text_clip'][sentence_index].get('align')
            text_clip_position = config['text_clip'][sentence_index].get('position')
            text_clip_size = config['text_clip'][sentence_index].get('size')
            text_clip_start = config['text_clip'][sentence_index].get('start')
            text_clip_duration = config['text_clip'][sentence_index].get('duration')
            image_clip_duration = config['image_clip'].get('duration')
            image_clip_size = config['image_clip'].get('size')

            # Create text clip
            text_clip = TextClip(sentence.text, color='white', font="Amiri-Bold", size=text_clip_size, fontsize=65, method='caption', align=text_clip_align)
            text_clip = text_clip.set_duration(text_clip_duration).set_start(text_clip_start).set_position(text_clip_position).crossfadein(2)  # Apply settings and effects

            # Create image clip
            image_clip = ImageClip(image.full_path).set_duration(4)
            image_clip_fx = image_clip.fx(vfx.colorx, 0.4).crossfadein(1).set_duration(image_clip_duration).set_position(('center', 'center')).resize(lambda t: 1 + 0.1 * (t-1.5) if t > 1.5 else 1)

            sentence_clip = concatenate_videoclips([image_clip, image_clip_fx], padding=-1,  method="compose")

            # Overlay text on image clip
            sentence_clip = CompositeVideoClip([sentence_clip, text_clip])
            sentence_clip = sentence_clip.crossfadein(1)  # Apply settings and effects

            # Append result in a list of clips
            clips_list.append(sentence_clip)

        # Concatenate video clips
        concat_clip = concatenate_videoclips(clips_list, padding=-1,  method="compose")  # padding=-N is necessary due to the crossfade(N) effect
        concat_clip.write_videofile("test.mp4", fps=15)
