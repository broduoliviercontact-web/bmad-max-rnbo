---
title: "Video Engine"
source: https://docs.cycling74.com/userguide/jitter/video_engine/
source_path: /userguide/jitter/video_engine/
scraped_at: 2026-05-29T17:40:09.252668+00:00
scope: Cycling 74 Max User Guide
---

# Video Engine

Source: https://docs.cycling74.com/userguide/jitter/video_engine/

## Extracted Text

# Video Engine
The Video Engine is responsible for interfacing with the operating system to manages access to video hardware devices and to video files on disk.
## Changing the Video Engine
Max's Video Engine preference allows users to switch the backend video implementation for all video objects.
Objects affected include jit.movie , jit.record , jit.playlist , and jit.matrixset . Still image loading may be affected by the video engine for jit.matrix and jit.gl.texture . Individual jit.movie , jit.grab and jit.record objects may override the Video Engine application preference by typing`@engine`, followed by the engine name argument, into the Max object box.
Objects previously initialized are unaffected by a preference change, therefore open patches should be closed and reopened after switching the video engine.
## Platform Specifics
Max ships with support for two video engines on Mac platforms, avf (AVFoundation - the default) and viddll (Viddll - FFmpeg), and two on Windows, viddll (the default) and qt (DirectShow). The DirectShow based engine is named qt for historical reasons, and has limited functionality. Windows users wishing to install third-party codecs for the qt engine should follow the instructions here . The viddll engine utilizes the FFmpeg library to provide support for a wide variety of file formats and codecs. Both avf and viddll engines provide native playback support for HAP encoded video files.
## Codec and Format Support
Common supported codecs for movie file reading with jit.movie and jit.playlist and file writing with jit.record and jit.matrixset :
- H264
- Photo-Jpeg
- ProRes (422 and 4444)
- Animation ( viddll only)
- Many additional formats and codecs when using viddll
Supported image types for file reading with jit.matrix and jit.gl.texture :
- JPEG
- PNG
- TIFF
- GIF
## jit.grab
The jit.grab object is unaffected by the video engine preference. On Mac, jit.grab will use AVFoundation as the video digitizer, and on Windows DirectX is used. Additionally both platforms include native support for Blackmagic video input devices. See the Blackmagic tab of the jit.grab help file for more information.
