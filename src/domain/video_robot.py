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
            align = config[sentence_index].get('align')
            position = config[sentence_index].get('position')
            size = config[sentence_index].get('size')

            # Create text clip
            text_clip = TextClip(sentence.text, color='white', font="Amiri-Bold", size=size, fontsize=65, method='caption', align=align).set_duration(5).set_start(3).set_position(position).crossfadein(2)

            # # Creating image clip
            image_clip = ImageClip(image.full_path).set_duration(8)

            # # Overlay text on image clip
            sentence_clip = CompositeVideoClip([image_clip, text_clip])

            clips_list.append(sentence_clip)

        # Concatenate video clips
        concat_clip = concatenate_videoclips(clips_list, method="compose")
        concat_clip.write_videofile("test.mp4", fps=24)
